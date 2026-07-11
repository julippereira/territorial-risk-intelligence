# =============================================================================
# TERRITORIAL RISK INTELLIGENCE
# INTEGRATED SOCIOENVIRONMENTAL MATRIX
# =============================================================================

import pandas as pd


# =============================================================================
# LOAD PROCESSED ANALYTICAL DATASETS
# =============================================================================

social_df = pd.read_csv(
    "../data/processed/households_vulnerability_sample.csv"
)

environmental_df = pd.read_csv(
    "../data/processed/households_environmental_risk_sample.csv"
)

# =============================================================================
# SELECT RELEVANT FIELDS
# =============================================================================

social_subset = social_df[
    [
        "id_household",
        "vulnerability_index",
        "risk_classification",
        "family_income_range",
        "dependents_count",
        "age_group"
    ]
]

environmental_subset = environmental_df[
    [
        "id_household",
        "environmental_risk_index",
        "environmental_risk_classification",
        "housing_material",
        "risk_types",
        "observed_signs"
    ]
]

# =============================================================================
# MERGE DATASETS
# =============================================================================

integrated_df = pd.merge(
    social_subset,
    environmental_subset,
    on="id_household",
    how="inner"
)

# =============================================================================
# INTEGRATED SOCIOENVIRONMENTAL INDEX
# Equal weight for both dimensions
# =============================================================================

integrated_df["socioenvironmental_index"] = (
    integrated_df["vulnerability_index"]
    +
    integrated_df["environmental_risk_index"]
) / 2

# =============================================================================
# PRIORITY CLASSIFICATION
# =============================================================================

def classify_priority(score):

    if score >= 2.5:
        return "Critical"

    elif score >= 1.8:
        return "High"

    elif score >= 1.2:
        return "Medium"

    else:
        return "Low"


integrated_df["socioenvironmental_priority"] = (
    integrated_df["socioenvironmental_index"]
    .apply(classify_priority)
)

# =============================================================================
# EXPORT
# =============================================================================

output_file = (
    "../data/processed/"
    "socioenvironmental_matrix_sample.csv"
)

integrated_df.to_csv(
    output_file,
    index=False
)

# =============================================================================
# SUMMARY
# =============================================================================

print(
    f"Integrated dataset created successfully: "
    f"{len(integrated_df)} records."
)

print("\nTop 5 Socioenvironmental Priorities\n")

print(
    integrated_df
    .sort_values(
        by="socioenvironmental_index",
        ascending=False
    )
    [
        [
            "id_household",
            "socioenvironmental_index",
            "socioenvironmental_priority"
        ]
    ]
    .head()
)
