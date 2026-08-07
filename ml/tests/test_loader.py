"""
Test for model_loader module.
"""

from ml.src.model_loader import (
    get_model,
    get_preprocessor,
    get_explainer,
    get_feature_names,
    get_metadata,
)


def test_model_loader():
    model = get_model()
    preprocessor = get_preprocessor()
    explainer = get_explainer()
    feature_names = get_feature_names()
    metadata = get_metadata()

    assert model is not None
    assert preprocessor is not None
    assert explainer is not None
    assert isinstance(feature_names, list) and len(feature_names) > 0
    assert isinstance(metadata, dict) and "optimal_threshold" in metadata

    print("All model_loader assertions passed.")


if __name__ == "__main__":
    test_model_loader()