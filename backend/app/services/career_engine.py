from pathlib import Path

import pandas as pd


class CareerEngine:
    """
    Recommends careers based on resume skills.
    """

    @staticmethod
    def recommend(resume_skills: dict):

        file_path = Path("data/job_roles.csv")
        dataframe = pd.read_csv(file_path)

        recommendations = []

        # Convert resume skills into a set
        resume_set = set()

        for skills in resume_skills.values():
            resume_set.update(skill.lower() for skill in skills)

        # Compare against every role
        for _, row in dataframe.iterrows():

            role = row["Role"]

            required_skills = [
                skill.strip().lower()
                for skill in row["Required Skills"].split(";")
            ]

            matched = len(
                resume_set.intersection(required_skills)
            )

            score = round(
                (matched / len(required_skills)) * 100
            )

            recommendations.append(
                {
                    "role": role,
                    "match_percentage": score
                }
            )

        # Highest score first
        recommendations.sort(
            key=lambda x: x["match_percentage"],
            reverse=True
        )

        return recommendations[:5]