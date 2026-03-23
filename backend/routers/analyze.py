from fastapi import APIRouter, UploadFile, File, HTTPException
from services.claude_service import analyze_document

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be PDF")
    content = await file.read()
    result = await analyze_document(content)
    return result