from pydantic import BaseModel


class ResumeUploadResponse(BaseModel):
    original_filename: str
    stored_filename: str
    file_path: str