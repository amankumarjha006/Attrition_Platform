"""
Model Loader Module

Loads all ML artifacts required for inference.
Artifacts are loaded once and cached in memory.
"""

import json
import logging
from pathlib import Path
import joblib

from .config import (
    MODEL_PATH,
    PREPROCESSOR_PATH,
    FEATURE_NAMES_PATH,
    METADATA_PATH,
    SHAP_EXPLAINER_PATH,
)
from .exceptions import ModelLoadError

logger = logging.getLogger(__name__)

# -------------------------------------------------------------------
# Helper to validate artifact existence
# -------------------------------------------------------------------
def _validate_artifact(path: Path, name: str) -> None:
    if not path.exists():
        raise ModelLoadError(f"{name} not found at {path}")
    if not path.is_file():
        raise ModelLoadError(f"{name} path is not a file: {path}")

# -------------------------------------------------------------------
# Load artifacts once
# -------------------------------------------------------------------
logger.info("Loading ML artifacts...")

_validate_artifact(MODEL_PATH, "Model")
_validate_artifact(PREPROCESSOR_PATH, "Preprocessor")
_validate_artifact(SHAP_EXPLAINER_PATH, "SHAP explainer")
_validate_artifact(FEATURE_NAMES_PATH, "Feature names")
_validate_artifact(METADATA_PATH, "Metadata")

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    explainer = joblib.load(SHAP_EXPLAINER_PATH)
except Exception as exc:
    raise ModelLoadError("Failed to load joblib artifacts") from exc

try:
    with open(FEATURE_NAMES_PATH, "r", encoding="utf-8") as f:
        feature_names = json.load(f)
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)
except Exception as exc:
    raise ModelLoadError("Failed to load JSON artifacts") from exc

logger.info("ML artifacts loaded successfully.")


# -------------------------------------------------------------------
# Getter Functions
# -------------------------------------------------------------------

def get_model():
    """Return trained model."""
    return model


def get_preprocessor():
    """Return fitted preprocessing pipeline."""
    return preprocessor


def get_explainer():
    """Return SHAP explainer."""
    return explainer


def get_feature_names():
    """Return transformed feature names."""
    return feature_names


def get_metadata():
    """Return model metadata."""
    return metadata