# 🏗️ Architecture

This directory contains the technical architecture, methodological framework, and analytical foundations of the **Territorial Risk Intelligence** project.

The artifacts stored here document how household survey data was transformed into a territorial intelligence solution through data engineering, analytical modeling, geospatial analysis, and business intelligence.

---

# 🎯 Purpose

The architecture was designed to support the complete lifecycle of territorial risk assessment, including:

- Survey design
- Field data collection planning
- Data preparation
- Data normalization
- Relational data modeling
- Analytical scoring
- Geospatial intelligence
- Business intelligence reporting

---

# 📝 Methodological Framework

The project follows a structured workflow that combines social, environmental, and spatial dimensions.

```text
Survey Design
        ↓
Field Data Collection
        ↓
Raw Survey Data
        ↓
Data Preparation
        ↓
Data Normalization
        ↓
Relational Data Model
        ↓
Social Vulnerability Assessment
        ↓
Environmental Risk Assessment
        ↓
Socioenvironmental Prioritization
        ↓
Geospatial Analysis
        ↓
Power BI Dashboard
```

---

# 📌 Architecture Assets

## 🔄 data_flow.png

Illustrates the end-to-end analytical workflow implemented in the project.

Main stages:

```text
Survey Design
      ↓
Field Data Collection
      ↓
Raw Survey Dataset
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Data Normalization
      ↓
Analytical Models
      ↓
Power BI Dashboard
```

Purpose:

- Document data lineage
- Demonstrate workflow reproducibility
- Support technical documentation

---

## 🗃️ data_model.png

Presents the relational data model used throughout the project.

Core entities:

```text
Households
    │
    ├── Social Programs
    │
    ├── Housing Conditions
    │
    ├── Environmental Risks
    │
    └── Locations
```

The model supports:

- Data normalization
- Household-level analysis
- Risk assessment
- Dashboard development

---

## 🧭 methodology.png

Documents the methodological approach used to structure and analyze territorial data.

Project phases:

1. Survey Design
2. Data Collection Planning
3. Data Preparation
4. Data Validation
5. Feature Engineering
6. Data Normalization
7. Risk Assessment
8. Geospatial Analysis
9. Dashboard Development

Purpose:

- Ensure methodological transparency
- Support reproducibility
- Document analytical assumptions

---

## 🌍 geospatial_analysis.png

Illustrates how spatial information is integrated with social and environmental indicators to support territorial intelligence.

Components:

- Household locations
- Watershed segmentation
- Environmental risk indicators
- Housing conditions
- Social vulnerability indicators
- Socioenvironmental prioritization

Conceptual framework:

```text
Locations
      +
Environmental Risks
      +
Housing Conditions
      +
Social Vulnerability
      ↓
Spatial Analysis
      ↓
Territorial Intelligence
      ↓
Priority Areas
```

Geospatial capabilities:

- Household-level mapping
- Risk hotspot identification
- Watershed analysis
- Territorial prioritization
- Spatial decision support

---

# 🧠 Analytical Architecture

The project integrates three analytical layers.

## 📈 Social Vulnerability Assessment

Evaluates vulnerability based on:

- Age group
- Family income
- Dependency ratio
- Housing tenure
- Social program participation

Output:

```text
Vulnerability Index
```

---

## 🌧️ Environmental Risk Assessment

Evaluates environmental exposure based on:

- Housing material
- Geological risks
- Observed risk indicators
- Registration status

Output:

```text
Environmental Risk Index
```

---

## 🌱 Integrated Socioenvironmental Assessment

Combines both analytical dimensions.

```text
Social Vulnerability
            +
Environmental Risk
            ↓
Socioenvironmental Index
```

Outputs:

- Socioenvironmental Index
- Priority Classification
- Household Ranking

Priority Levels:

```text
Low
Medium
High
Critical
```

---

# 🗺️ Territorial Intelligence Framework

The project was built around the concept that territorial vulnerability cannot be explained by a single variable.

The analytical framework integrates:

```text
Demographic Indicators
            +
Socioeconomic Indicators
            +
Housing Conditions
            +
Environmental Risks
            +
Spatial Information
            ↓
Territorial Risk Intelligence
```

This approach enables the identification of priority households and supports evidence-based territorial planning.

---

# 🔐 Data Privacy and Ethics

The architecture was designed to support the publication of anonymized and synthetic datasets.

The public version of the project:

- Does not contain real household identifiers
- Does not contain real addresses
- Does not contain real geographic coordinates
- Does not contain personal or sensitive information

Geographic coordinates available in the repository were synthetically generated exclusively for demonstration purposes.

---

# 🚀 Key Capabilities Demonstrated

- Survey Design
- Questionnaire Structuring
- Data Collection Planning
- Data Engineering
- Data Cleaning
- Feature Engineering
- Data Normalization
- Relational Data Modeling
- Risk Scoring
- Geospatial Analysis
- Territorial Intelligence
- Business Intelligence
- Dashboard Development

---

# 📍 Architecture in Context

```text
architecture/
        ↓
Project Design

analytics/
        ↓
Risk Models

data/
        ↓
Anonymized Datasets

power_bi/
        ↓
Interactive Dashboard

docs/
        ↓
Visual Outputs
```

This directory provides the technical and methodological foundation supporting every stage of the Territorial Risk Intelligence project.
