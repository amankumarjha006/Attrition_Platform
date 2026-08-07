"""
Custom exceptions for the ML package.
"""

class ModelLoadError(Exception):
    """Raised when an ML artifact fails to load or is missing."""
    pass

class PredictionError(Exception):
    """Raised when prediction fails due to invalid input or model error."""
    pass

class InvalidEmployeeDataError(Exception):
    """Raised when employee data is missing required fields or malformed."""
    pass

class ExplanationError(Exception):
    """Raised when SHAP explanation cannot be computed."""
    pass

class RecommendationError(Exception):
    """Raised when recommendation generation fails."""
    pass