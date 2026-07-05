# Notebooks

This directory contains the analytical workflow used to transform raw household survey data into a structured territorial intelligence dataset.

The notebooks represent the main stages of the data preparation and analysis process.

---

## 01_data_cleaning.ipynb

Transforms raw survey records into a standardized dataset suitable for analysis.

### Main Activities

- Load raw survey data
- Assess data quality
- Handle missing values
- Standardize column names
- Normalize categorical values
- Remove duplicate records
- Generate unique household identifiers
- Export cleaned datasets

### Outputs

- Clean household records
- Standardized demographic attributes
- Validated socioeconomic information
- Consistent categorical fields

---

## 02_feature_engineering.ipynb

Creates analytical features derived from the original survey data.

### Main Activities

- Calculate household size indicators
- Calculate income per capita
- Create age group classifications
- Generate binary program participation indicators
- Generate housing condition indicators
- Generate environmental risk indicators

### Outputs

- Analytical features
- Risk indicators
- Social vulnerability attributes
- Household-level metrics

---

## 03_data_quality_checks.ipynb

Validates the consistency and integrity of the processed datasets.

### Main Activities

- Null value analysis
- Referential integrity checks
- Duplicate detection
- Range validation
- Category validation
- Quality reporting

### Outputs

- Data quality report
- Validation metrics
- Data consistency checks

---

## 04_exploratory_analysis.ipynb

Performs exploratory analysis to identify patterns and trends.

### Main Activities

- Demographic analysis
- Income distribution analysis
- Social program coverage analysis
- Housing condition assessment
- Environmental risk assessment
- Geographic distribution analysis

### Outputs

- Descriptive statistics
- Visualizations
- Vulnerability insights
- Territorial risk indicators

---

## Workflow

```text
Raw Survey Data
        │
        ▼
01_data_cleaning
        │
        ▼
02_feature_engineering
        │
        ▼
03_data_quality_checks
        │
        ▼
04_exploratory_analysis
        │
        ▼
Territorial Risk Intelligence Dataset
```

The notebooks illustrate the complete analytical workflow, from raw field survey records to a structured dataset suitable for business intelligence, geospatial analysis, and territorial risk assessment.
