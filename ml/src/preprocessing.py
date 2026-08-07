"""
Preprocessing utilities for employee data.
"""

import pandas as pd


UNWANTED_COLS = [
    "EmployeeCount",
    "StandardHours",
    "Over18",
    "EmployeeNumber",
    "Attrition",
]


def prepare_employee_df(raw_employee_dict: dict) -> pd.DataFrame:
    """
    Convert raw employee dictionary to a DataFrame ready for the preprocessor.

    Drops constant / non-predictive columns if present.
    """
    df = pd.DataFrame([raw_employee_dict])
    df = df.drop(columns=UNWANTED_COLS, errors="ignore")
    return df