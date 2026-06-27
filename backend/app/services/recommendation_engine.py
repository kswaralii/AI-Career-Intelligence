from pathlib import Path

import pandas as pd


class RecommendationEngine:
    """
    Returns learning resources for the missing skills
    from learning_resources.csv.
    """

    @staticmethod
    def recommend(missing_skills: list[str]):

        file_path = Path("data/learning_resources.csv")

        dataframe = pd.read_csv(file_path)

        recommendations = []

        for skill in missing_skills:

            result = dataframe[
                dataframe["Skill"].str.lower() == skill.lower()
            ]

            if not result.empty:

                for _, row in result.iterrows():

                    recommendations.append(
                        {
                            "skill": row["Skill"],
                            "resource": row["Resource"],
                            "platform": row["Platform"],
                            "url": row["URL"]
                        }
                    )

        return recommendations