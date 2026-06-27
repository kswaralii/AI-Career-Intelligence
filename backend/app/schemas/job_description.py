from pydantic import BaseModel


class JobDescriptionRequest(BaseModel):
    job_description: str


class JobDescriptionResponse(BaseModel):
    job_description: str
    skills: dict