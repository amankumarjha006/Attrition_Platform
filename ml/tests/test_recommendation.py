from ml.src.recommendation import get_recommendations

# Mock explanation output similar to explain_employee
mock_explanation = {
    "base_log_odds": -2.5,
    "top_features": [
        {"feature": "bin__OverTime", "shap_value": 0.45, "feature_value": 1.0, "direction": "increase"},
        {"feature": "nom__JobRole_Sales Representative", "shap_value": -0.30, "feature_value": 0.0, "direction": "decrease"},
        {"feature": "num__TotalWorkingYears", "shap_value": 0.20, "feature_value": 5.0, "direction": "increase"},
        {"feature": "ord__EnvironmentSatisfaction", "shap_value": -0.15, "feature_value": 4.0, "direction": "decrease"},
    ]
}

recs = get_recommendations(mock_explanation)

print("=" * 50)
print("Recommendations")
print("=" * 50)
for r in recs:
    print("- ", r)

assert isinstance(recs, list)
assert len(recs) > 0
for r in recs:
    assert isinstance(r, str)
    assert len(r) > 0

print("\nAll assertions passed.")