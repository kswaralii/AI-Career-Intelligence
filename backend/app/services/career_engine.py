from pathlib import Path
import re

import pandas as pd


class CareerEngine:

    @staticmethod
    def recommend(resume_skills: dict):

        dataframe = pd.read_csv(Path("data/job_roles.csv"))
        dataframe.columns = dataframe.columns.str.strip()

        if "Role" not in dataframe.columns:
            return {
                "recommended_roles": [],
                "message": "Career data is missing the Role column."
            }

        if "Required Skills" in dataframe.columns:
            skills_column = "Required Skills"
        elif "Skills" in dataframe.columns:
            skills_column = "Skills"
        else:
            return {
                "recommended_roles": [],
                "message": "Career data is missing the skills column."
            }

        resume_skill_set = {
            skill.strip().lower()
            for skills in resume_skills.values()
            for skill in skills
        }

        recommendations = []

        for _, row in dataframe.iterrows():

            role = str(row["Role"]).strip()

            raw_skills = str(row[skills_column])

            role_skills = {
                skill.strip().lower()
                for skill in re.split(r"[;,]", raw_skills)
                if skill.strip()
            }

            if not role_skills:
                continue

            matched_skills = resume_skill_set.intersection(role_skills)

            match_percentage = round(
                (len(matched_skills) / len(role_skills)) * 100
            )

            recommendations.append(
                {
                    "role": role,
                    "match_percentage": match_percentage
                }
            )

        recommendations.sort(
            key=lambda item: item["match_percentage"],
            reverse=True
        )

        return {
            "recommended_roles": recommendations[:5]
        }