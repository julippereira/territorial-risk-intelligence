# 🌎 Territorial Risk Intelligence

An end-to-end data analytics project designed to transform household survey data into actionable territorial intelligence products.

This project demonstrates the complete lifecycle of a territorial risk assessment initiative, from survey design and data preparation to analytical modeling, geospatial analysis, and interactive business intelligence dashboards.

---

# 🎯 Project Overview

Territorial vulnerabilities are influenced by a combination of social, environmental, housing, and geographic factors.

This project integrates these dimensions into a unified analytical framework capable of:

- Identifying vulnerable households
- Assessing environmental risks
- Prioritizing intervention areas
- Supporting territorial planning
- Enabling evidence-based decision-making

The solution combines Data Engineering, Analytics, Geospatial Intelligence, and Business Intelligence techniques to provide a holistic view of socioenvironmental risk.

---

# 📝 Survey Design

A key component of this project was the design and structuring of the household survey instrument used to collect territorial data.

The survey was planned to capture demographic, socioeconomic, housing, environmental, and geospatial information at the household level.

### Survey Dimensions

- Demographics
- Education
- Occupation
- Household composition
- Income profile
- Social program participation
- Housing conditions
- Environmental risks
- Territorial location
- Geospatial references

### Survey Design Activities

- Questionnaire structure definition
- Variable standardization
- Response categorization
- Data collection planning
- Geospatial requirements definition
- Analytical indicator requirements

The resulting dataset was specifically designed to support risk assessment, household prioritization, and geospatial analysis.

---

# 🏗️ Project Architecture

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
Integrated Socioenvironmental Matrix
        ↓
Geospatial Analysis
        ↓
Power BI Dashboard
        ↓
Territorial Risk Intelligence
```

---

# 📂 Repository Structure

```text
territorial-risk-intelligence/
│
├── architecture/
├── analytics/
├── data/
├── docs/
├── notebooks/
├── power_bi/
│
├── README.md
└── requirements.txt
```

---

# 🗃️ Data Model

The project is based on a normalized household survey model.

### Core Entities

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

### Analytical Outputs

```text
Households Vulnerability
Households Environmental Risk
Socioenvironmental Matrix
```

---

# 🧹 Data Engineering Workflow

The data engineering layer includes:

- Survey data ingestion
- Data cleaning
- Header standardization
- Feature engineering
- Household ID generation
- Income classification
- Geospatial preparation
- Data normalization
- Relational modeling

Implemented through Jupyter notebooks available in:

```text
notebooks/
```

---

# 📒 Notebooks

### 01_data_preparation.ipynb

Responsible for:

- Raw data ingestion
- Data cleaning
- Standardization
- Feature engineering

### 02_social_programs_normalization.ipynb

Responsible for:

- Social program normalization
- Indicator structuring
- Data modeling

### 03_housing_conditions_normalization.ipynb

Responsible for:

- Housing condition normalization
- Infrastructure indicators
- Housing quality assessment

### 04_environmental_risks_normalization.ipynb

Responsible for:

- Environmental risk normalization
- Risk classification
- Analytical preparation

---

# 🧠 Analytics Layer

Located in:

```text
analytics/
```

The analytics layer transforms processed datasets into risk intelligence products.

---

## 📈 Social Vulnerability Assessment

```text
vulnerability_index.py
```

Calculates household vulnerability based on:

- Age group
- Family income
- Dependents
- Housing tenure
- Social program participation

Output:

```text
households_vulnerability_sample.csv
```

---

## 🌧️ Environmental Risk Assessment

```text
environmental_risk_index.py
```

Calculates environmental risk based on:

- Housing material
- Environmental hazards
- Risk indicators
- Registration status

Output:

```text
households_environmental_risk_sample.csv
```

---

## 🌱 Integrated Socioenvironmental Matrix

```text
socioenvironmental_matrix.py
```

Integrates:

- Social Vulnerability Index
- Environmental Risk Index

Outputs:

- Socioenvironmental Index
- Priority Classification
- Household Ranking

Output:

```text
socioenvironmental_matrix_sample.csv
```

Priority Levels:

```text
Low
Medium
High
Critical
```

---

# 🌍 Geospatial Intelligence

Geospatial analysis is a core component of the project.

The solution combines:

- Household locations
- Watershed segmentation
- Housing conditions
- Environmental risk indicators
- Social vulnerability indicators

to support territorial prioritization.

### Capabilities

- Household-level mapping
- Risk hotspot detection
- Watershed analysis
- Spatial prioritization
- Territorial decision support

> Geographic coordinates available in this repository are synthetic values generated exclusively for demonstration purposes.

---

# 📊 Power BI Dashboard

The Power BI solution consolidates demographic, socioeconomic, environmental, housing, and geospatial indicators into an interactive territorial intelligence platform.

---

## 👥 Demographics

Provides an overview of the surveyed population.

Key indicators:

- Total Households
- Total Residents
- Female-Headed Households
- Households with Dependents
- Age Distribution
- Education Level
- Occupation Profile

---

## 💰 Socioeconomics

Presents socioeconomic characteristics and vulnerability-related indicators.

Key indicators:

- Average Family Income
- Average Per Capita Income
- Income Distribution
- Social Program Participation
- Beneficiary Households

---

## 🏠 Housing

Assesses housing quality and infrastructure adequacy.

Key indicators:

- Households in Critical Areas
- Households Exposed to Geological Risks
- Households Without Sewer Access
- Wood/Mixed Housing Units
- Housing Condition Score
- Environmental & Sanitary Conditions

---

## 🌎 Geospatial Distribution

Combines analytical indicators with spatial information to support territorial decision-making.

Key indicators:

- Average Socioenvironmental Index
- Average Vulnerability Index
- Average Environmental Risk Index
- High-Priority Households

Visualizations:

- Socioenvironmental Priority Map
- Interactive Household-Level Tooltips
- Priority Distribution
- Priority Households by Income Range

---

# 📸 Dashboard Preview

### 👥 Demographics

docs/dashboard_demographics.png

---

### 💰 Socioeconomics

docs/dashboard_socioeconomics.png

---

### 🏠 Housing

docs/dashboard_housing.png

---

### 🌍 Geospatial Distribution

docs/dashboard_geospatial.png

---

### 🔎 Household-Level Geospatial Detail

docs/dashboard_geospatial_detail.png

---

# 🏗️ Technical Documentation

The complete project architecture is documented in:

```text
architecture/
```

Contents include:

- Data Flow
- Relational Data Model
- Project Methodology
- Geospatial Architecture

---

# 🛠️ Technologies

### Data Engineering

- Python
- Pandas
- Jupyter Notebook

### Analytics

- Python
- Risk Scoring Models
- Feature Engineering

### Business Intelligence

- Power BI
- DAX
- Power Query

### Geospatial Analysis

- Azure Maps
- Spatial Visualization
- Territorial Intelligence

---

# 🔐 Data Privacy

All datasets included in this repository are anonymized and synthetic.

The repository does not contain:

- Real household information
- Real addresses
- Real geographic coordinates
- Personally identifiable information

The published datasets were designed exclusively for demonstration, educational, and portfolio purposes.

---

# 🚀 Key Skills Demonstrated

- Survey Design
- Questionnaire Development
- Data Collection Planning
- Data Engineering
- Data Cleaning
- Feature Engineering
- Data Normalization
- Relational Modeling
- Analytics Engineering
- Risk Assessment
- Geospatial Analysis
- Territorial Intelligence
- Business Intelligence
- Dashboard Development
- Power BI

---

# 📬 Contact

If you would like to discuss the project, exchange ideas, or collaborate, feel free to connect through GitHub or LinkedIn.

---

⭐ If you enjoyed this project, consider giving the repository a star.
