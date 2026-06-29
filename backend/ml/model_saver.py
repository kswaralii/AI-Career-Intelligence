from pathlib import Path
import joblib


class ModelSaver:
    """
    Saves trained ML model and encoders.
    """

    @staticmethod
    def save(model, encoders):

        model_dir = Path("ml/models")
        artifact_dir = Path("ml/artifacts")

        model_dir.mkdir(parents=True, exist_ok=True)
        artifact_dir.mkdir(parents=True, exist_ok=True)

        joblib.dump(
            model,
            model_dir / "salary_model.pkl"
        )

        joblib.dump(
            encoders,
            artifact_dir / "encoders.pkl"
        )

        print("\n✅ Model Saved Successfully")
        print(model_dir / "salary_model.pkl")

        print("\n✅ Encoders Saved Successfully")
        print(artifact_dir / "encoders.pkl")