"""
Recommendation module: translates SHAP explanations into actionable HR recommendations.
"""

from typing import List
from ml.src.schemas import RecommendationResult

# Mapping from feature keywords to recommendation strings
RECOMMENDATION_RULES = {
    "OverTime": "Reduce overtime workload.",
    "JobRole": "Discuss career progression and role fit.",
    "BusinessTravel": "Review travel requirements and flexibility.",
    "TotalWorkingYears": "Consider tenure-based retention incentives.",
    "Age": "Evaluate age-related engagement strategies.",
    "EnvironmentSatisfaction": "Improve workplace environment satisfaction.",
    "JobSatisfaction": "Address job satisfaction drivers.",
    "WorkLifeBalance": "Promote better work-life balance.",
    "MonthlyIncome": "Review compensation competitiveness.",
    "YearsAtCompany": "Recognize long-term commitment.",
    "DistanceFromHome": "Explore remote or flexible location options.",
    "PerformanceRating": "Align performance expectations and rewards.",
    "TrainingTimesLastYear": "Increase development and training opportunities.",
    "RelationshipSatisfaction": "Foster positive workplace relationships.",
    "StockOptionLevel": "Review equity and long-term incentive plans.",
}


def get_recommendations(explanation: dict) -> RecommendationResult:
    """
    Generate a list of HR recommendations based on the top SHAP features.

    Parameters
    ----------
    explanation : dict
        Output from explain_employee containing 'top_features'.

    Returns
    -------
    RecommendationResult
        List of actionable recommendation strings.
    """
    recommendations: List[str] = []
    seen = set()

    for feat in explanation.get("top_features", []):
        feature_name = feat.get("feature", "")
        direction = feat.get("direction", "")

        # Find matching rule (simple substring match on key)
        for key, rec in RECOMMENDATION_RULES.items():
            if key.lower() in feature_name.lower() and rec not in seen:
                # Optionally tailor based on direction
                if direction == "increase":
                    recommendations.append(rec)
                else:
                    # If feature decreases risk, maybe reinforce positive factor
                    recommendations.append(f"Maintain {rec.lower()}")
                seen.add(rec)

    # Fallback generic recommendations if none matched
    if not recommendations:
        recommendations = [
            "Review overall employee engagement.",
            "Conduct stay interview to understand concerns.",
            "Monitor attrition risk indicators regularly."
        ]

    return recommendations