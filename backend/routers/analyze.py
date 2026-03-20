from __future__ import annotations

import time
from base64 import b64encode

from fastapi import APIRouter, File, Form, HTTPException, Request, UploadFile

from middleware.rate_limit import enforce_plan_rate_limit
from services.cache_service import cache_service
from services.claude_service import analyze_pdf
from services.mongo_service import mongo_service

router = APIRouter(prefix="/api", tags=["analyze"])


@router.post("/analyze")
async def analyze(request: Request, file: UploadFile = File(...), userId: str | None = Form(default=None)) -> dict:
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF uploads are allowed.")

    user_id = userId or "anonymous-user"
    await enforce_plan_rate_limit(request=request, user_plan="free")

    started_at = time.perf_counter()
    file_bytes = await file.read()
    pdf_hash = cache_service.build_pdf_hash(file_bytes)

    cached_payload = await cache_service.get(pdf_hash)
    if cached_payload is not None:
        processing_ms = int((time.perf_counter() - started_at) * 1000)
        return {**cached_payload, "processingTimeMs": processing_ms, "cached": True}

    base64_pdf = b64encode(file_bytes).decode("utf-8")
    analysis = await analyze_pdf(base64_pdf)
    processing_ms = int((time.perf_counter() - started_at) * 1000)
    stored = await mongo_service.insert_analysis(
        user_id,
        {
            **analysis,
            "pdfHash": pdf_hash,
            "cached": False,
            "processingTimeMs": processing_ms,
        },
    )
    await cache_service.set(pdf_hash, stored)
    return {**stored, "processingTimeMs": processing_ms, "cached": False}
