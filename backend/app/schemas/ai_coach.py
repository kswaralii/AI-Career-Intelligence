from pydantic import BaseModel


class AICoachRequest(BaseModel):
    resume_id: str
    question: str


class AICoachResponse(BaseModel):
    advice: str