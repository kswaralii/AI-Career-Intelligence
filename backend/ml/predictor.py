from pathlib import Path

import joblib
import pandas as pd


class Predictor:
    """
    Loads the trained model and predicts salary.
    """

    def __init__(self):

        self.model = joblib.load(
            Path("ml/models/salary_model.pkl")
        )

        self.encoders = joblib.load(
            Path("ml/artifacts/encoders.pkl")
        )

    def predict(self, input_data: dict):

        df = pd.DataFrame([input_data])

        categorical_columns = [
            "experience_level",
            "employment_type",
            "job_title",
            "employee_residence",
            "company_location",
            "company_size"
        ]

        for column in categorical_columns:
            df[column] = self.encoders[column].transform(df[column])

        prediction = self.model.predict(df)

        return float(prediction[0])