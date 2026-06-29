from fastapi import APIRouter

from app.schemas.salary import (
    SalaryPredictionRequest,
    SalaryPredictionResponse,
)

from app.services.salary_prediction_service import (
    SalaryPredictionService,
)

router = APIRouter(
    prefix="/salary",
    tags=["Salary Prediction"],
)


@router.post(
    "/predict",
    response_model=SalaryPredictionResponse,
)
async def predict_salary(
    request: SalaryPredictionRequest,
):

    return SalaryPredictionService.predict(
        request.model_dump()
    )