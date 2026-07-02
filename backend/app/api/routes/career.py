from fastapi import APIRouter, HTTPException

from app.schemas.career import CareerRequest, CareerResponse
from app.services.career_engine import CareerEngine
from app.storage.resume_store import ResumeStore


router = APIRouter(
    prefix="/career",
    tags=["Career"]
)


@router.post(
    "/recommend",
    response_model=CareerResponse
)
async def recommend_career(
    request: CareerRequest,
):

    resume_data = ResumeStore.get(
        request.resume_id
    )

    if not resume_data:
        raise HTTPException(
            status_code=404,
            detail="Resume not found. Please upload your resume again."
        )

    resume_skills = resume_data.get(
        "extracted_skills",
        {}
    )

    if not resume_skills:
        return {
            "recommended_roles": []
        }

    return CareerEngine.recommend(
        resume_skills
    )