from pydantic import BaseModel


class CareerRequest(BaseModel):
    resume_id: str


class CareerRecommendation(BaseModel):
    role: str
    match_percentage: int


class CareerResponse(BaseModel):
    recommended_roles: list[CareerRecommendation]