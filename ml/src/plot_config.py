"""
Global plotting configuration for the Employee Attrition Prediction project.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================================
# Theme
# ==========================================================

sns.set_theme(
    style="whitegrid",
    context="talk",
    palette="crest"
)

# ==========================================================
# Matplotlib Configuration
# ==========================================================

plt.rcParams.update({

    # Figure
    "figure.figsize": (8, 5),
    "figure.dpi": 120,
    "figure.facecolor": "white",

    # Axes
    "axes.titlesize": 18,
    "axes.titleweight": "bold",
    "axes.labelsize": 13,
    "axes.grid": True,

    # Grid
    "grid.alpha": 0.25,

    # Tick Labels
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,

    # Legend
    "legend.fontsize": 11,

    # Spines
    "axes.spines.top": False,
    "axes.spines.right": False,

    # Save Figures
    "savefig.bbox": "tight",
    "savefig.dpi": 300
})

# ==========================================================
# Project Color Palette
# ==========================================================

PRIMARY = "#4C78A8"
SECONDARY = "#72B7B2"
ACCENT = "#F58518"
SUCCESS = "#54A24B"
DANGER = "#E45756"
PURPLE = "#B279A2"

# Sequential palette
SEQUENTIAL = sns.color_palette("crest")

# Diverging palette
DIVERGING = sns.color_palette("coolwarm", as_cmap=True)