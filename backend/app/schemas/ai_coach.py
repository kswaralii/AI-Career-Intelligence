from pydantic import BaseModel


class AICoachRequest(BaseModel):
    resume_skills: list[str]
    ats_score: int
    recommended_role: str
    missing_skills: list[str]


class AICoachResponse(BaseModel):
    advice: str