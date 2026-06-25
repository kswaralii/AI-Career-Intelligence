from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI Career Intelligence Platform API",
)


@app.on_event("startup")
async def startup_event():
    logger.info("Application started successfully.")


@app.get("/")
async def root():
    return {
        "message": "Welcome to the AI Career Intelligence Platform API",
        "version": settings.app_version,
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": settings.app_name,
        "version": settings.app_version,
    }