from pathlib import Path

import pandas as pd


class SkillExtractor:
    """
    Extract technical skills from normalized NLP text
    using the skills knowledge base.
    """

    @staticmethod
    def extract(normalized_text: str) -> dict:

        # Load skills knowledge base
        file_path = Path("data/skills.csv")
        dataframe = pd.read_csv(file_path)

        extracted = {}

        normalized_text = normalized_text.lower()

        for _, row in dataframe.iterrows():

            skill = str(row["Skill"]).strip()
            category = str(row["Category"]).strip()

            if skill.lower() in normalized_text:
                extracted.setdefault(category, []).append(skill)

        return extracted