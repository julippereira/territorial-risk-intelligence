# 📓 Notebooks

This directory contains the data preparation workflow used in the Territorial Risk Intelligence project.

## Workflow

### 01_data_preparation.ipynb
- Raw data ingestion
- Header standardization
- String cleaning
- Household ID creation
- Age group creation
- Family income classification
- Per capita income calculation

### 02_social_programs_normalization.ipynb
- Social program normalization
- Pivot transformation
- Binary indicators generation

### 03_housing_conditions_normalization.ipynb
- Housing condition normalization
- Pivot transformation
- Binary indicators generation

### 04_environmental_risks_normalization.ipynb
- Environmental risk normalization
- Pivot transformation
- Binary indicators generation

## Output

The notebooks generate the relational datasets used throughout the project:

- households_sample.csv
- social_programs_sample.csv
- housing_conditions_sample.csv
- environmental_risks_sample.csv
- locations_sample.csv
