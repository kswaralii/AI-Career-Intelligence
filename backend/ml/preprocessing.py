import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DataPreprocessor:

    @staticmethod
    def preprocess(df):

        # Remove unnecessary columns
        df = df.drop(
            columns=[
                "Unnamed: 0",
                "salary",
                "salary_currency"
            ]
        )

        # Separate target
        y = df["salary_in_usd"]

        X = df.drop(columns=["salary_in_usd"])

        encoders = {}

        categorical_columns = X.select_dtypes(
            include=["object", "string"]
        ).columns

        for column in categorical_columns:

            encoder = LabelEncoder()

            X[column] = encoder.fit_transform(X[column])

            encoders[column] = encoder

        return X, y, encoders