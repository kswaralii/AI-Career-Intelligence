from pathlib import Path
import re

import pandas as pd


class SkillExtractor:

    @staticmethod
    def _contains(text: str, alias: str) -> bool:
        alias = alias.strip().lower()

        if not alias:
            return False

        pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"
        return re.search(pattern, text.lower()) is not None

    @classmethod
    def extract(cls, normalized_text) -> dict:

        # Supports both a list of NLP tokens and a normal text string
        if isinstance(normalized_text, list):
            text = " ".join(str(token) for token in normalized_text)
        else:
            text = str(normalized_text)

        dataframe = pd.read_csv(Path("data/skills.csv"))
        dataframe.columns = dataframe.columns.str.strip()

        extracted = {}

        for _, row in dataframe.iterrows():

            skill = str(row["Skill"]).strip()
            category = str(row["Category"]).strip()

            # Uses aliases if present; otherwise uses the skill itself
            if "Aliases" in dataframe.columns:
                aliases = str(row["Aliases"]).split(",")
            else:
                aliases = [skill]

            if any(cls._contains(text, alias) for alias in aliases):
                extracted.setdefault(category, []).append(skill)

        return {
            category: sorted(set(skills))
            for category, skills in extracted.items()
        }