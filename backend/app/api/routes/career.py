from fastapi import APIRouter, UploadFile, File

from app.schemas.career import CareerResponse
from app.services.resume_service import ResumeService
from app.services.career_engine import CareerEngine

router = APIRouter(
    prefix="/career",
    tags=["Career"]
)


@router.post(
    "/recommend",
    response_model=CareerResponse
)
async def recommend_career(
    resume: UploadFile = File(...)
):

    resume_result = ResumeService.save_resume(resume)

    recommendations = CareerEngine.recommend(
        resume_result["extracted_skills"]
    )

    return {
        "recommended_roles": recommendations
    }