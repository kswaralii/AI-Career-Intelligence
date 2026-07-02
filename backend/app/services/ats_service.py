from app.services.job_description_service import JobDescriptionService
from app.services.ats_matcher import ATSMatcher
from app.services.recommendation_engine import RecommendationEngine
from app.storage.resume_store import ResumeStore


class ATSService:
    """
    Complete ATS Analysis Service.
    """

    @staticmethod
    def analyze(resume_id: str, job_description: str):

        resume = ResumeStore.get(resume_id)

        if resume is None:
            raise ValueError("Resume not found.")

        job = JobDescriptionService.extract_skills(
            job_description
        )

        ats_result = ATSMatcher.match(
            resume["extracted_skills"],
            job["skills"]
        )

        recommendations = RecommendationEngine.recommend(
            ats_result["missing_skills"]
        )

        return {
            "ats_score": ats_result["ats_score"],
            "matched_skills": ats_result["matched_skills"],
            "missing_skills": ats_result["missing_skills"],
            "recommendations": recommendations,
            "resume_skills": resume["extracted_skills"],
            "job_skills": job["skills"],
        }