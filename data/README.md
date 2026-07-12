# 🗃️ Data

This directory contains anonymized and synthetic datasets used to demonstrate the data engineering and analytics workflow developed for the Territorial Risk Intelligence project.

The original project was based on household survey data collected in the field, including demographic, socioeconomic, housing, environmental risk, and geospatial information.

To preserve confidentiality, all datasets published in this repository were anonymized or synthetically generated while maintaining the original structure, relationships, and analytical logic of the project.

> **Note**
>
> All sample files available in this repository are intended exclusively for demonstration and portfolio purposes.
>
> The datasets do not contain real personal information, geographic references, or sensitive records.
>
> Sample datasets were created to reproduce the data model, transformation processes, and analytical outputs used in the original project while ensuring privacy protection.

---

## Directory Structure

```text
data/
│
├── raw/
│   └── sample_survey_raw.xlsx
│
├── processed/
│   ├── households_sample.csv
│   ├── social_programs_sample.csv
│   ├── housing_conditions_sample.csv
│   ├── environmental_risks_sample.csv
│   ├── locations_sample.csv
│
└── dictionary/
    └── data_dictionary.xlsx
```

---

## Raw Data

### sample_survey_raw.xlsx

An anonymized representation of the original household survey structure.

Contains sample fields related to:

- Demographics
- Income
- Housing characteristics
- Social programs
- Environmental risks
- Geospatial information

---

## Processed Data

### households_sample.csv

Main household table containing demographic and socioeconomic attributes.

### social_programs_sample.csv

Normalized table containing social program participation indicators.

### housing_conditions_sample.csv

Normalized table containing housing infrastructure indicators.

### environmental_risks_sample.csv

Normalized table containing environmental risk indicators.

### locations_sample.csv

Geospatial reference table containing anonymized location attributes.

---

## Data Model

```text
households
      │
      ├── social_programs
      │
      ├── housing_conditions
      │
      ├── environmental_risks
      │
      └── locations
```

---

## Reproducibility

The datasets contained in this folder support the notebooks and analytical models located in:

```text
notebooks/
analytics/
```

and are intended to demonstrate:

- Data cleaning
- Data normalization
- Relational modeling
- Geospatial enrichment
- Vulnerability assessment
- Environmental risk analysis
- Socioenvironmental prioritization
