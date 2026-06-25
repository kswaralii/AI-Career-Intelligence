from pathlib import Path
import shutil

from fastapi import UploadFile

from app.utils.file_utils import (
    create_upload_directory,
    generate_unique_filename,
    UPLOAD_DIR,
)


class ResumeService:

    @staticmethod
    def save_resume(file: UploadFile):

        create_upload_directory()

        filename = generate_unique_filename(file.filename)

        destination = UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "original_filename": file.filename,
            "stored_filename": filename,
            "file_path": str(destination),
        }