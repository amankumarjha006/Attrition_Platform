from attrition_ml.inference import predict_employee

sample = {
    "Age": 41,
    "BusinessTravel": "Travel_Rarely",
    "DailyRate": 1102,
    "Department": "Sales",
    "DistanceFromHome": 1,
    "Education": 2,
    "EducationField": "Life Sciences",
    "EnvironmentSatisfaction": 2,
    "Gender": "Female",
    "HourlyRate": 94,
    "JobInvolvement": 3,
    "JobLevel": 2,
    "JobRole": "Sales Executive",
    "JobSatisfaction": 4,
    "MaritalStatus": "Single",
    "MonthlyIncome": 5993,
    "MonthlyRate": 19479,
    "NumCompaniesWorked": 8,
    "OverTime": "Yes",
    "PercentSalaryHike": 11,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 1,
    "StockOptionLevel": 0,
    "TotalWorkingYears": 8,
    "TrainingTimesLastYear": 0,
    "WorkLifeBalance": 1,
    "YearsAtCompany": 6,
    "YearsInCurrentRole": 4,
    "YearsSinceLastPromotion": 0,
    "YearsWithCurrManager": 5
}

result = predict_employee(sample)

print("=" * 50)
print("Prediction Result")
print("=" * 50)

for key, value in result.items():
    print(f"{key}: {value}")

# Basic assertions
assert "prediction" in result
assert isinstance(result["prediction"], bool)
assert "label" in result
assert result["label"] in ("Attrition", "No Attrition")
assert "probability" in result
assert isinstance(result["probability"], float)
assert "threshold" in result
assert isinstance(result["threshold"], float)
assert "risk_level" in result
assert isinstance(result["risk_level"], str)

print("\nAll assertions passed.")