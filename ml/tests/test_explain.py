from ml.src.explain import explain_employee

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

explanation = explain_employee(sample, top_n=5)

print("=" * 50)
print("Explanation Result")
print("=" * 50)
import json
print(json.dumps(explanation, indent=2))

assert "base_log_odds" in explanation
assert isinstance(explanation["base_log_odds"], float)
assert "top_features" in explanation
assert isinstance(explanation["top_features"], list)
assert len(explanation["top_features"]) <= 5
for feat in explanation["top_features"]:
    assert "feature" in feat
    assert "shap_value" in feat
    assert "feature_value" in feat
    assert "direction" in feat
    assert feat["direction"] in ("increase", "decrease")

print("\nAll assertions passed.")