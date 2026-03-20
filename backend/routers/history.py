from __future__ import annotations

from fastapi import APIRouter, HTTPException

from services.mongo_service import mongo_service

router = APIRouter(prefix="/api/history", tags=["history"])


@router.get("/{userId}")
async def get_history(userId: str) -> dict[str, object]:
    items = await mongo_service.list_history(userId)
    return {"userId": userId, "items": items}


@router.delete("/{userId}")
async def delete_history(userId: str) -> dict[str, object]:
    deleted = await mongo_service.delete_history(userId)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="No history found for the user.")
    return {"userId": userId, "deleted": deleted}
