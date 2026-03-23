from fastapi import APIRouter
from services.mongo_service import get_history, delete_history

router = APIRouter()

@router.get("/history/{user_id}")
async def get_user_history(user_id: str):
    return await get_history(user_id)

@router.delete("/history/{user_id}")
async def delete_user_history(user_id: str):
    return await delete_history(user_id)