from pathlib import Path
import shutil
from app.services.skill_extractor import SkillExtractor
from fastapi import UploadFile
from app.services.nlp_processor import NLPProcessor
from app.services.pdf_parser import PDFParser
from app.storage.resume_store import ResumeStore
from app.utils.file_utils import (
    create_upload_directory,
    generate_unique_filename,
    UPLOAD_DIR,
)


class ResumeService:
    @staticmethod
    def save_resume(file: UploadFile):
        """
        Save uploaded resume and extract text.
        """

        # Create uploads directory if it doesn't exist
        create_upload_directory()

        # Generate a unique filename
        filename = generate_unique_filename(file.filename)

        # Destination path
        destination = UPLOAD_DIR / filename

        # Save the uploaded PDF
        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract text from the saved PDF
        extracted_text = PDFParser.extract_text(str(destination))
        processor = NLPProcessor()

        nlp_result = processor.process_text(extracted_text)
        skills = SkillExtractor.extract(
    nlp_result["normalized_text"]
)
        # Return upload details and a preview of extracted text
        ResumeStore.save(
    filename,
    {
        "original_filename": file.filename,
        "stored_filename": filename,
        "file_path": str(destination),
        "extracted_text": extracted_text,
        "filtered_tokens": nlp_result["filtered_tokens"],
        "extracted_skills": skills,
    }
)

        return {
    "message": "Resume uploaded successfully.",
    "resume_id": filename,
}