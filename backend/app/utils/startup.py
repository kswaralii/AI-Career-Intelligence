from app.storage.resume_store import ResumeStore
from app.utils.file_utils import UPLOAD_DIR


def startup_cleanup():
    """
    Clears uploads folder and ResumeStore
    every time the server starts.
    """

    if UPLOAD_DIR.exists():

        for file in UPLOAD_DIR.glob("*"):

            if file.is_file():

                file.unlink()

    ResumeStore.clear()