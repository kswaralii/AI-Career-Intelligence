from fastapi import APIRouter

from app.schemas.ai_coach import (
    AICoachRequest,
    AICoachResponse,
)

from app.services.ai_coach_service import (
    AICoachService,
)

router = APIRouter(
    prefix="/ai-coach",
    tags=["AI Career Coach"],
)


@router.post(
    "/chat",
    response_model=AICoachResponse,
)
async def chat(
    request: AICoachRequest,
):

    return AICoachService.get_career_advice(
        request.model_dump()
    )