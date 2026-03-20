from __future__ import annotations

import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.init_db import init_db
from routers.analyze import router as analyze_router
from routers.auth import router as auth_router
from routers.history import router as history_router
from routers.report import router as report_router
from services.cache_service import cache_service
from services.mongo_service import mongo_service

load_dotenv()

app = FastAPI(title="LEXSCAN Legal Risk Analyzer")

origins = [item.strip() for item in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",") if item.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(analyze_router)
app.include_router(history_router)
app.include_router(report_router)


@app.on_event("startup")
async def startup_event() -> None:
    await init_db()
    await cache_service.connect()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await cache_service.disconnect()
    await mongo_service.disconnect()


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
