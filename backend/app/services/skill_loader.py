from pathlib import Path

import pandas as pd


class SkillLoader:

    @staticmethod
    def load_skills():

        file_path = Path("data/skills.csv")

        dataframe = pd.read_csv(file_path)

        return dataframe