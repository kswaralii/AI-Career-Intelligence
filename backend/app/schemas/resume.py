from pydantic import BaseModel


class ResumeUploadResponse(BaseModel):
    message: str
    resume_id: str