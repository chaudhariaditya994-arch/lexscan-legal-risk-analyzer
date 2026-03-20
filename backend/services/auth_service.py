from __future__ import annotations

import os
from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from fastapi import HTTPException
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token


JWT_SECRET = os.getenv("JWT_SECRET_KEY", "change-me")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "1440"))
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")


def create_access_token(payload: dict[str, Any]) -> str:
    data = payload.copy()
    data["exp"] = datetime.now(UTC) + timedelta(minutes=JWT_EXPIRE_MINUTES)
    return jwt.encode(data, JWT_SECRET, algorithm="HS256")


def verify_google_credential(credential: str) -> dict[str, Any]:
    if not GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=400, detail="GOOGLE_CLIENT_ID is not configured.")

    try:
        token_info = id_token.verify_oauth2_token(credential, google_requests.Request(), GOOGLE_CLIENT_ID)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=401, detail="Invalid Google credential.") from exc

    email = token_info.get("email")
    if not email:
        raise HTTPException(status_code=401, detail="Google profile did not include an email.")

    return {
        "userId": token_info.get("sub", email),
        "email": email,
        "name": token_info.get("name", email.split("@")[0]),
        "plan": "free",
    }
