from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.report_service import ReportService

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)


@router.get("/{resume_id}")
async def generate_report(resume_id: str):

    pdf_path = ReportService.generate(resume_id)

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="Resume_Report.pdf"
    )