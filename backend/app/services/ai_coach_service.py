import google.generativeai as genai

from app.core.config import settings


genai.configure(api_key=settings.gemini_api_key)


class AICoachService:

    @staticmethod
    def get_career_advice(data: dict):

        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
You are an expert AI Career Coach.

Analyze the following candidate profile and provide personalized career advice.

Resume Skills:
{", ".join(data["resume_skills"])}

ATS Score:
{data["ats_score"]}

Recommended Role:
{data["recommended_role"]}

Missing Skills:
{", ".join(data["missing_skills"])}

Give:
1. Overall assessment
2. Strengths
3. Weaknesses
4. Skills to learn next
5. Suggested projects
6. A 30-day improvement roadmap

Keep the response professional and concise.
"""

        response = model.generate_content(prompt)

        return {
            "advice": response.text
        }