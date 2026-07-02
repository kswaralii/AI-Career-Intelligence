from google import genai

from app.core.config import settings
from app.storage.resume_store import ResumeStore


class AICoachService:

    @staticmethod
    def get_career_advice(data: dict):

        resume = ResumeStore.get(data["resume_id"])

        if resume is None:
            return {
                "advice": "Resume not found. Please upload your resume again."
            }

        question = data["question"].strip()
        question_lower = question.lower()

        career_keywords = [
            "resume",
            "career",
            "placement",
            "job",
            "role",
            "skill",
            "project",
            "roadmap",
            "learn",
            "interview",
            "internship",
            "coding",
            "developer",
            "engineer",
            "data",
            "machine learning",
            "portfolio",
            "cv",
        ]

        if not any(keyword in question_lower for keyword in career_keywords):
            return {
                "advice": (
                    "I can help with career, resume, placements, projects, "
                    "learning roadmaps, and interview preparation. "
                    "Please ask a career-related question."
                )
            }

        client = genai.Client(
            api_key=settings.gemini_api_key
        )

        prompt = f"""
You are CareerPilot AI, a professional career coach for BE students preparing for campus placements.

Candidate resume:
{resume["extracted_text"]}

User question:
{question}

Answer only the user's question.
Keep the answer concise, practical, and career-focused.
Do not add extra sections unless the user asks for them.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return {
            "advice": response.text
        }