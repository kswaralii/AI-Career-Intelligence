from predictor import Predictor

predictor = Predictor()

sample = {
    "work_year": 2024,
    "experience_level": "SE",
    "employment_type": "FT",
    "job_title": "Data Scientist",
    "employee_residence": "US",
    "remote_ratio": 100,
    "company_location": "US",
    "company_size": "M"
}

salary = predictor.predict(sample)

print(f"Predicted Salary: ${salary:,.2f}")