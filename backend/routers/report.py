from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from services.mongo_service import mongo_service
from services.pdf_service import build_report_pdf

router = APIRouter(prefix="/api/report", tags=["report"])


@router.get("/pdf/{id}")
async def report_pdf(id: str) -> StreamingResponse:
    analysis = await mongo_service.get_analysis(id)
    if analysis is None:
        raise HTTPException(status_code=404, detail="Analysis not found.")

    pdf_bytes = build_report_pdf(analysis)
    return StreamingResponse(iter([pdf_bytes]), media_type="application/pdf")
