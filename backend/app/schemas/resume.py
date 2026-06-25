from pydantic import BaseModel


class ResumeUploadResponse(BaseModel):
    original_filename: str
    stored_filename: str
    file_path: str
    extracted_text_preview: str
    extracted_skills: dict
    filtered_tokens: list[str]