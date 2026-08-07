"""
Inference Module

Provides prediction utilities for employee attrition.
"""

from ml.src.model_loader import get_model, get_preprocessor, get_metadata
from ml.src.preprocessing import prepare_employee_df
from ml.src.schemas import PredictionResult


# ------------------------------------------------------------------
# Load cached artifacts
# ------------------------------------------------------------------

model = get_model()
preprocessor = get_preprocessor()
metadata = get_metadata()


# ------------------------------------------------------------------
# Prediction
# ------------------------------------------------------------------

def predict_employee(employee: dict) -> PredictionResult:
    """
    Predict attrition probability for a single employee.

    Parameters
    ----------
    employee : dict
        Raw employee record.

    Returns
    -------
    PredictionResult
        Prediction payload with keys:
        - prediction (bool)
        - label (str)  "Attrition" or "No Attrition"
        - probability (float)
        - threshold (float)
        - risk_level (str)
    """
    sample_df = prepare_employee_df(employee)

    X = preprocessor.transform(sample_df)

    probability = float(model.predict_proba(X)[0][1])

    threshold = metadata.get("optimal_threshold", 0.5)

    prediction = probability >= threshold

    label = "Attrition" if prediction else "No Attrition"

    if probability < 0.25:
        risk_level = "Low Risk"
    elif probability < threshold:
        risk_level = "Medium Risk"
    elif probability < 0.65:
        risk_level = "High Risk"
    else:
        risk_level = "Critical Risk"

    return {
        "prediction": bool(prediction),
        "label": label,
        "probability": round(probability, 4),
        "threshold": round(threshold, 4),
        "risk_level": risk_level,
    }