from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    pass

app = FastAPI(title="LEXSCAN API", version="1.0.0", lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
from routers import analyze, history, report, auth

app.include_router(analyze.router, prefix="/api", tags=["analysis"])
app.include_router(history.router, prefix="/api", tags=["history"])
app.include_router(report.router, prefix="/api", tags=["reports"])
app.include_router(auth.router, prefix="/auth", tags=["authentication"])

@app.get("/")
async def root():
    return {"message": "LEXSCAN API", "version": "1.0.0", "status": "running"}