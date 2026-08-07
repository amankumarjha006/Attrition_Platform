"""
Type schemas for ML package public APIs.
"""

from typing import List, TypedDict


class FeatureContribution(TypedDict):
    feature: str
    shap_value: float
    feature_value: float
    direction: str  # "increase" or "decrease"


class PredictionResult(TypedDict):
    prediction: bool
    label: str
    probability: float
    threshold: float
    risk_level: str


class ExplanationResult(TypedDict):
    base_log_odds: float
    top_features: List[FeatureContribution]


RecommendationResult = List[str]