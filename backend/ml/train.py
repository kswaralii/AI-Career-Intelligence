import pandas as pd

from preprocessing import DataPreprocessor
from model_saver import ModelSaver
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def load_dataset():
    """
    Load salary dataset.
    """
    df = pd.read_csv("data/salary_data.csv")
    return df


if __name__ == "__main__":

    # ===============================
    # Load Dataset
    # ===============================

    df = load_dataset()

    print("=" * 50)
    print("DATASET OVERVIEW")
    print("=" * 50)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    # ===============================
    # Target Variable
    # ===============================

    print("\n" + "=" * 50)
    print("TARGET VARIABLE")
    print("=" * 50)

    print(df["salary_in_usd"].describe())

    # ===============================
    # Categorical Columns
    # ===============================

    print("\n" + "=" * 50)
    print("CATEGORICAL COLUMNS")
    print("=" * 50)

    categorical_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    print(categorical_columns.tolist())

    print("\nUnique Values")

    for column in categorical_columns:
        print(f"\n{column}")
        print(df[column].nunique())

    # ===============================
    # Preprocessing
    # ===============================

    print("\n" + "=" * 50)
    print("PREPROCESSING")
    print("=" * 50)

    X, y, encoders = DataPreprocessor.preprocess(df)

    print("\nFeatures Shape")
    print(X.shape)

    print("\nTarget Shape")
    print(y.shape)

    print("\nEncoded Features")
    print(X.head())

    print("\nTarget")
    print(y.head())

    # ===============================
    # Train Test Split
    # ===============================

    print("\n" + "=" * 50)
    print("TRAIN TEST SPLIT")
    print("=" * 50)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training Samples :", X_train.shape[0])
    print("Testing Samples  :", X_test.shape[0])

    # ===============================
    # Linear Regression
    # ===============================

    print("\n" + "=" * 50)
    print("LINEAR REGRESSION")
    print("=" * 50)

    lr_model = LinearRegression()

    lr_model.fit(X_train, y_train)

    lr_predictions = lr_model.predict(X_test)

    lr_mae = mean_absolute_error(y_test, lr_predictions)
    lr_rmse = mean_squared_error(y_test, lr_predictions) ** 0.5
    lr_r2 = r2_score(y_test, lr_predictions)

    print(f"MAE  : {lr_mae:.2f}")
    print(f"RMSE : {lr_rmse:.2f}")
    print(f"R²   : {lr_r2:.4f}")

    # ===============================
    # Random Forest
    # ===============================

    print("\n" + "=" * 50)
    print("RANDOM FOREST REGRESSION")
    print("=" * 50)

    rf_model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    rf_model.fit(X_train, y_train)

    rf_predictions = rf_model.predict(X_test)

    rf_mae = mean_absolute_error(y_test, rf_predictions)
    rf_rmse = mean_squared_error(y_test, rf_predictions) ** 0.5
    rf_r2 = r2_score(y_test, rf_predictions)

    print(f"MAE  : {rf_mae:.2f}")
    print(f"RMSE : {rf_rmse:.2f}")
    print(f"R²   : {rf_r2:.4f}")

    # ===============================
    # Gradient Boosting
    # ===============================

    print("\n" + "=" * 50)
    print("GRADIENT BOOSTING REGRESSION")
    print("=" * 50)

    gb_model = GradientBoostingRegressor(
        random_state=42
    )

    gb_model.fit(X_train, y_train)

    gb_predictions = gb_model.predict(X_test)

    gb_mae = mean_absolute_error(y_test, gb_predictions)
    gb_rmse = mean_squared_error(y_test, gb_predictions) ** 0.5
    gb_r2 = r2_score(y_test, gb_predictions)

    print(f"MAE  : {gb_mae:.2f}")
    print(f"RMSE : {gb_rmse:.2f}")
    print(f"R²   : {gb_r2:.4f}")

    # ===============================
    # Model Comparison
    # ===============================

    print("\n" + "=" * 70)
    print("MODEL COMPARISON")
    print("=" * 70)

    print(f"{'Model':<25}{'MAE':<15}{'RMSE':<15}{'R²'}")
    print("-" * 70)

    print(f"{'Linear Regression':<25}{lr_mae:<15.2f}{lr_rmse:<15.2f}{lr_r2:.4f}")
    print(f"{'Random Forest':<25}{rf_mae:<15.2f}{rf_rmse:<15.2f}{rf_r2:.4f}")
    print(f"{'Gradient Boosting':<25}{gb_mae:<15.2f}{gb_rmse:<15.2f}{gb_r2:.4f}")

    print("\n" + "=" * 70)
    print("SAVING BEST MODEL")
    print("=" * 70)

    ModelSaver.save(
    rf_model,
    encoders
)