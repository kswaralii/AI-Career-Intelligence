from pydantic import BaseModel


class LearningResource(BaseModel):
    skill: str
    resource: str
    platform: str
    url: str


class ATSResponse(BaseModel):
    ats_score: int
    matched_skills: list[str]
    missing_skills: list[str]
    recommendations: list[LearningResource]
    resume_skills: dict
    job_skills: dict