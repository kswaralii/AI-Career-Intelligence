from pathlib import Path

import pandas as pd


class RecommendationEngine:

    @staticmethod
    def recommend(missing_skills: list[str]):

        dataframe = pd.read_csv(
            Path("data/learning_resources.csv")
        )

        recommendations = []

        for skill in missing_skills:

            matches = dataframe[
                dataframe["Skill"].astype(str).str.strip().str.lower()
                == skill.strip().lower()
            ]

            for _, row in matches.iterrows():
                recommendations.append(
                    {
                        "skill": str(row["Skill"]),
                        "resource": str(row["Resource"]),
                        "platform": str(row["Platform"]),
                        "url": str(row["URL"]),
                    }
                )

        return recommendations