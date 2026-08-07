"""
Script to create and save SHAP explainer for model inference.
"""

import pandas as pd
import joblib
import shap
from pathlib import Path

from attrition_ml.config import (
    MODEL_PATH,
    PREPROCESSOR_PATH,
    SHAP_EXPLAINER_PATH,
    ARTIFACTS_DIR
)

def create_shap_explainer():
    """Create and save SHAP explainer."""
    # Load model and preprocessor
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    
    # Load training data for background reference
    processed_dir = Path(__file__).resolve().parent.parent / "data" / "processed"
    X_train = pd.read_pickle(processed_dir / "X_train.pkl")
    
    # Preprocess training data
    X_train_transformed = preprocessor.transform(X_train)
    
    # Load feature names
    feature_names_path = ARTIFACTS_DIR / "feature_names.json"
    import json
    with open(feature_names_path, "r") as f:
        feature_names = json.load(f)
    
    X_train_df = pd.DataFrame(X_train_transformed, columns=feature_names)
    
    # Create background sample
    background = shap.sample(X_train_df, 200, random_state=42)
    
    # Create explainer
    explainer = shap.Explainer(model, background)
    
    # Save explainer
    joblib.dump(explainer, SHAP_EXPLAINER_PATH)
    print(f"SHAP explainer saved to {SHAP_EXPLAINER_PATH}")

if __name__ == "__main__":
    create_shap_explainer()