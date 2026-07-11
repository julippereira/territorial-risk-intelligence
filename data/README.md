# 📝 Data

This directory contains anonymized sample datasets used to demonstrate the data engineering and analytics workflow developed for the Territorial Risk Intelligence project.

The original dataset was collected through structured household surveys and included demographic, socioeconomic, housing, environmental risk, and geospatial information.

To support analytical use cases, the raw survey data was cleaned, normalized, and transformed into a relational data model composed of multiple linked tables.

All datasets available in this repository contain synthetic and fully anonymized records designed to preserve the original structure while protecting sensitive information.

## Structure

data/
```
├── raw/
│   └── sample_survey_raw.xlsx
│
├── processed/
│   ├── households_sample.csv
│   ├── social_programs_sample.csv
│   ├── environmental_risks_sample.csv
│   ├── housing_conditions_sample.csv
│   └── locations_sample.csv
│
└── dictionary/
    └── data_dictionary.xlsx
```
