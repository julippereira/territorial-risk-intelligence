# Analytics

This directory contains the analytical models used to transform processed household survey data into actionable territorial intelligence indicators.

## Models

### vulnerability_index.py

Calculates a social vulnerability score based on:

- Age group
- Family income
- Dependents
- Housing tenure
- Social program participation

### environmental_risk_index.py

Calculates an environmental risk score based on:

- Housing material
- Environmental hazards
- Risk warning signs
- Registration status

### socioenvironmental_matrix.py

Integrates social vulnerability and environmental risk indicators into a single prioritization framework.

Outputs:

- Socioenvironmental index
- Priority classification
- Household ranking

Priority Levels:

- Critical
- High
- Medium
- Low
