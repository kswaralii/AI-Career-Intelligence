from ml.predictor import Predictor


class SalaryPredictionService:

    @staticmethod
    def predict(data: dict):

        predictor = Predictor()

        predicted_salary = predictor.predict(data)

        return {
            "predicted_salary_usd": round(predicted_salary, 2)
        }