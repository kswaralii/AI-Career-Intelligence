from fastapi import UploadFile
from app.services.recommendation_engine import RecommendationEngine
from app.services.resume_service import ResumeService
from app.services.job_description_service import JobDescriptionService
from app.services.ats_matcher import ATSMatcher


class ATSService:
    """
    Complete ATS Analysis Service.
    Processes the resume and job description,
    then compares their skills.
    """

    @staticmethod
    def analyze(resume: UploadFile, job_description: str):

        # Process Resume
        resume_result = ResumeService.save_resume(resume)

        # Process Job Description
        job_result = JobDescriptionService.extract_skills(
            job_description
        )

        # Compare Skills
        ats_result = ATSMatcher.match(
            resume_result["extracted_skills"],
            job_result["skills"]
        )

        recommendations = RecommendationEngine.recommend(
        ats_result["missing_skills"]
)

        # Return complete ATS analysis
        return {
    "ats_score": ats_result["ats_score"],
    "matched_skills": ats_result["matched_skills"],
    "missing_skills": ats_result["missing_skills"],
    "recommendations": recommendations,
    "resume_skills": resume_result["extracted_skills"],
    "job_skills": job_result["skills"],
}