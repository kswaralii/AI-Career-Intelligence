from fastapi import FastAPI
from app.api.routes.ats import router as ats_router
from app.core.config import settings
from app.core.logging import logger
from app.api.routes.resume import router as resume_router
from app.api.routes.career import router as career_router
from app.api.routes.salary import router as salary_router
from app.api.routes.ai_coach import router as ai_coach_router
from app.utils.startup import clear_uploads
from app.utils.startup import startup_cleanup

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI Career Intelligence Platform API",
)

app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(career_router)
app.include_router(salary_router)
app.include_router(ai_coach_router)

@app.on_event("startup")
async def startup_event():

    startup_cleanup()

    logger.info("Startup cleanup completed.")

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