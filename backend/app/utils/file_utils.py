from pathlib import Path
import uuid

UPLOAD_DIR = Path("uploads")


def create_upload_directory():
    """
    Create uploads directory if it doesn't exist.
    """
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def generate_unique_filename(filename: str) -> str:
    """
    Generate unique filename while preserving extension.
    """
    extension = Path(filename).suffix

    return f"{uuid.uuid4()}{extension}"