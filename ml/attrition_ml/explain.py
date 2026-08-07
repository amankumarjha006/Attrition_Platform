"""
Explainability module: provides local SHAP explanations for a single employee.
"""

import pandas as pd
from attrition_ml.model_loader import get_explainer, get_preprocessor, get_feature_names
from attrition_ml.preprocessing import prepare_employee_df
from attrition_ml.schemas import ExplanationResult


def explain_employee(raw_employee_dict: dict, top_n: int = 6) -> ExplanationResult:
    """
    Compute SHAP feature contributions for a single employee.

    Returns a JSON-friendly dict with top features.
    """
    preprocessor = get_preprocessor()
    explainer = get_explainer()
    feature_names = get_feature_names()

    # Prepare data
    sample_df = prepare_employee_df(raw_employee_dict)
    X_trans = preprocessor.transform(sample_df)
    X_trans_df = pd.DataFrame(X_trans, columns=feature_names)

    # SHAP values for single sample
    single_shap = explainer(X_trans_df)[0]

    shap_values = single_shap.values
    base_value = float(single_shap.base_values)

    contributions = []
    for feat_name, shap_val, feat_val in zip(feature_names, shap_values, X_trans_df.iloc[0]):
        contributions.append({
            "feature": feat_name,
            "shap_value": float(round(shap_val, 4)),
            "feature_value": float(round(feat_val, 4)),
            "direction": "increase" if shap_val > 0 else "decrease"
        })

    # Sort by absolute impact
    contributions.sort(key=lambda x: abs(x["shap_value"]), reverse=True)

    top_features = contributions[:top_n]

    return {
        "base_log_odds": round(base_value, 4),
        "top_features": top_features
    }