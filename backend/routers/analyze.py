from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from services import claude_service, mongo_service, cache_service
import hashlib
import time
import base64

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...), userId: str = Form(None)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be PDF")
    content = await file.read()
    base64_pdf = base64.b64encode(content).decode()
    hash_obj = hashlib.sha256(content)
    pdf_hash = hash_obj.hexdigest()
    cached = cache_service.get_cached_pdf(pdf_hash)
    if cached:
        return {**cached, "cached": True}
    start_time = time.time()
    result = await claude_service.analyze_pdf(base64_pdf)
    processing_time = int((time.time() - start_time) * 1000)
    result["processingTimeMs"] = processing_time
    result["cached"] = False
    cache_service.cache_pdf(pdf_hash, result)
    if userId:
        await mongo_service.save_analysis(userId, result)
    return result