from __future__ import annotations

from fastapi import APIRouter

from models.user import User
from services.auth_service import create_access_token, verify_google_credential

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/google")
async def google_auth(payload: dict[str, str]) -> dict[str, object]:
    user_data = verify_google_credential(payload["credential"])
    user = User(**user_data)
    token = create_access_token({"sub": user.userId, "email": user.email, "plan": user.plan})
    return {"user": user.model_dump(), "accessToken": token}
