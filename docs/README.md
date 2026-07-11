# 📁 Documentation

This directory contains visual and technical documentation supporting the Territorial Risk Intelligence project.

The assets in this folder are intended to document the end-to-end data lifecycle, from survey design and field data collection to data engineering, analytical modeling, geospatial analysis, and business intelligence reporting.

---

## Contents

### data_flow.png

Illustrates the complete data journey:

```text
Survey Design
    ↓
Field Data Collection
    ↓
Raw Data Sources
    ↓
Data Cleaning & Standardization
    ↓
Feature Engineering
    ↓
Relational Data Modeling
    ↓
Territorial Risk Analysis
    ↓
Business Intelligence
```

---

### data_model.png

Presents the relational data model used throughout the project.

Main entities include:

- Households
- Social Programs
- Housing Conditions
- Environmental Risks
- Locations

The model was designed to support analytical workloads and dashboard development.

---

### geospatial_analysis.png

Illustrates how geospatial information is combined with socioeconomic and environmental indicators to support territorial risk assessment.

Layers represented include:

- Household locations
- Watershed boundaries
- Risk exposure zones
- Housing conditions
- Social vulnerability indicators
- Environmental risk indicators

The geospatial framework enables:

- Spatial distribution analysis
- Risk hotspot identification
- Vulnerability mapping
- Priority area detection
- Territorial intervention planning

Example workflow:

```text
Household Survey Data
          +
Geographic Coordinates
          +
Environmental Risks
          +
Social Vulnerability Indicators
          ↓
Territorial Risk Assessment
          ↓
Priority Mapping
```

---

### methodology.png

Summarizes the project methodology and major 
