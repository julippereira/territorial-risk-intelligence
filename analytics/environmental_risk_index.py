# =============================================================================
# TERRITORIAL RISK INTELLIGENCE
# ENVIRONMENTAL RISK INDEX
# =============================================================================

import pandas as pd
import numpy as np


# =============================================================================
# ENVIRONMENTAL RISK MODEL
# =============================================================================

def calculate_environmental_risk(df):

    # =========================================================================
    # HOUSING MATERIAL
    # Less resistant materials = higher risk
    # =========================================================================

    material_map = {
        "Tent": 4,
        "Wood": 3,
        "Mixed": 2,
        "Masonry": 0
    }

    df["score_material"] = (
        df["housing_material"]
        .map(material_map)
        .fillna(1)
    )

    # =========================================================================
    # RISK COUNT
    # =========================================================================

    def count_items(text):

        if pd.isna(text):
            return 0

        text = str(text).strip()

        if text == "" or text.lower() == "none":
            return 0

        text = (
            text.replace(";", ",")
                .replace(" and ", ",")
        )

        return len(
            [
                item
                for item in text.split(",")
                if item.strip()
            ]
        )

    df["risk_count"] = (
        df["risk_types"]
        .apply(count_items)
    )

    df["score_risks"] = (
        df["risk_count"]
        .clip(upper=4)
    )

    # =========================================================================
    # OBSERVED SIGNS
    # =========================================================================

    df["sign_count"] = (
        df["observed_signs"]
        .apply(count_items)
    )

    df["score_signs"] = (
        df["sign_count"]
        .clip(upper=4)
    )

    # =========================================================================
    # REGISTRATION STATUS
    # =========================================================================

    def score_registration(value):

        value = str(value).upper().strip()

        if "NOT REGISTERED" in value:
            return 5

        if "INCOMPLETE" in value:
            return 4

        if "INACTIVE" in value:
            return 3

        if "ACTIVE" in value:
            return 2

        if "MORTGAGE" in value:
            return 1

        if "REMOVED" in value:
            return 0

        return 2

    df["score_registration"] = (
        df["registration_status"]
        .apply(score_registration)
    )

    # =========================================================================
    # ENVIRONMENTAL RISK INDEX
    # =========================================================================

    df["environmental_risk_index"] = (
        df["score_risks"] * 0.30 +
        df["score_signs"] * 0.30 +
        df["score_material"] * 0.20 +
        (df["score_registration"] / 1.25) * 0.20
    )

    # =========================================================================
    # RISK CLASSIFICATION
    # =========================================================================

    def classify_risk(score):

        if score >= 3.0:
            return "Very High"

        elif score >= 2.0:
            return "High"

        elif score >= 1.0:
            return "Medium"

        else:
            return "Low"

    df["environmental_risk_classification"] = (
        df["environmental_risk_index"]
        .apply(classify_risk)
    )

    return df


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    print("Loading environmental dataset...")

    df = pd.read_csv(
        "../data/processed/households_sample.csv"
    )

    print(f"Records loaded: {len(df)}")

    print("Calculating environmental risk index...")

    result = calculate_environmental_risk(df)

    output_file = (
        "../data/processed/"
        "households_environmental_risk_sample.csv"
    )

    result.to_csv(
        output_file,
        index=False
    )

    print("Environmental risk calculation completed.")

    print("\nTop 5 Highest Environmental Risk Households\n")

    print(
        result
        .sort_values(
            by="environmental_risk_index",
            ascending=False
        )
        [
            [
                "id_household",
                "environmental_risk_index",
                "environmental_risk_classification"
            ]
        ]
        .head()
    )
