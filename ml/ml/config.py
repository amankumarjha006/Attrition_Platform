from pathlib import Path

# Project root (ml/)
ML_ROOT = Path(__file__).resolve().parent.parent

# Artifact directory
ARTIFACTS_DIR = ML_ROOT / "artifacts"

# Artifact files
MODEL_PATH = ARTIFACTS_DIR / "model.joblib"
PREPROCESSOR_PATH = ARTIFACTS_DIR / "preprocessor.joblib"
FEATURE_NAMES_PATH = ARTIFACTS_DIR / "feature_names.json"
METADATA_PATH = ARTIFACTS_DIR / "metadata.json"
SHAP_EXPLAINER_PATH = ARTIFACTS_DIR / "shap_explainer.joblib"