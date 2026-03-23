from fastapi import APIRouter
from services.pdf_service import generate_report

router = APIRouter()

@router.get("/report/pdf/{analysis_id}")
async def get_report(analysis_id: str):
    return await generate_report(analysis_id)