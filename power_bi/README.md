# 📊 Power BI Dashboard

This directory contains the Power BI dashboard developed for the **Territorial Risk Intelligence** project.

The dashboard integrates demographic, socioeconomic, housing, environmental, and geospatial indicators to support household-level risk assessment and territorial prioritization.

---

## File

```text
territorial_risk_intelligence.pbix
```

---

## Dashboard Structure

### 1. Demographics

Provides an overview of the surveyed population and household composition.

Key indicators:

- Total Households
- Total Residents
- Female-Headed Households
- Households with Dependents
- Age Distribution
- Education Level
- Occupation Profile

---

### 2. Socioeconomics

Presents socioeconomic characteristics and vulnerability-related indicators.

Key indicators:

- Average Family Income
- Average Per Capita Income
- Income Distribution
- Beneficiary Households
- Social Program Coverage
- Social Program Participation

---

### 3. Housing

Assesses housing conditions and infrastructure adequacy.

Key indicators:

- Households in Critical Areas
- Households Exposed to Geological Risks
- Households Without Sewer Access
- Wood/Mixed Housing Units
- Housing Condition Score
- Environmental and Sanitary Conditions

---

### 4. Geospatial Distribution

Combines analytical indicators with geographic information to support territorial intelligence.

Key indicators:

- Average Socioenvironmental Index
- Average Vulnerability Index
- Average Environmental Risk Index
- High-Priority Households

Visualizations:

- Socioenvironmental Priority Map
- Priority Households by Income Range
- Socioenvironmental Priority Distribution
- Interactive Household-Level Tooltips

---

## Analytical Framework

The dashboard consolidates the outputs produced by the analytical models contained in the `analytics/` directory.

```text
Household Survey Data
            ↓
Data Preparation
            ↓
Data Normalization
            ↓
Social Vulnerability Index
            ↓
Environmental Risk Index
            ↓
Socioenvironmental Matrix
            ↓
Power BI Dashboard
```

---

## Geospatial Analysis

The dashboard includes interactive geospatial visualizations based on anonymized coordinates.

Capabilities include:

- Household-level risk mapping
- Watershed-based analysis
- Priority area identification
- Spatial risk distribution
- Interactive filtering and exploration

> Geographic coordinates included in this project are synthetic and were generated exclusively for demonstration purposes.

---

## Dashboard Screenshots

Available in the `/docs` directory:

```text
dashboard_demographics.png
dashboard_socioeconomics.png
dashboard_housing.png
dashboard_geospatial.png
dashboard_geospatial_detail.png
```

---

## Main Indicators

### Social Vulnerability

- Vulnerability Index
- Income Profile
- Dependents
- Social Programs
- Household Composition

### Environmental Risk

- Environmental Risk Index
- Geological Risks
- Housing Material
- Registration Status
- Risk Indicators

### Territorial Prioritization

- Socioenvironmental Index
- Risk Classification
- Priority Households
- Geospatial Distribution

---

## Purpose

The dashboard was designed to transform household survey data into actionable territorial intelligence products, supporting risk assessment, prioritization, and evidence-based decision-making through an integrated socioenvironmental perspective.
