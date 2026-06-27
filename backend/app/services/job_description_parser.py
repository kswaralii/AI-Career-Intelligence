from app.services.nlp_processor import NLPProcessor
from app.services.skill_extractor import SkillExtractor


class JobDescriptionService:
    """
    Processes a job description and extracts technical skills.
    """

    @staticmethod
    def extract_skills(job_description: str):

        processor = NLPProcessor()

        nlp_result = processor.process_text(job_description)

        skills = SkillExtractor.extract(
            nlp_result["normalized_text"]
        )

        return {
            "job_description": job_description,
            "skills": skills
        }