from fastapi import APIRouter, UploadFile, File, Form
from app.schemas.ats import (
    ATSRequest,
    ATSResponse,
)
from app.schemas.job_description import (
    JobDescriptionRequest,
    JobDescriptionResponse,
)
from app.schemas.ats import ATSResponse

from app.services.job_description_service import JobDescriptionService
from app.services.ats_service import ATSService


router = APIRouter(
    prefix="/ats",
    tags=["ATS"]
)


@router.post(
    "/job-description",
    response_model=JobDescriptionResponse
)
async def analyze_job_description(
    request: JobDescriptionRequest,
):

    return JobDescriptionService.extract_skills(
        request.job_description
    )


@router.post(
    "/analyze",
    response_model=ATSResponse
)
async def analyze_resume(
    request: ATSRequest,
):

    return ATSService.analyze(
        request.resume_id,
        request.job_description
    )