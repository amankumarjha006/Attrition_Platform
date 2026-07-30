# Functional Requirements Specification (FRS)

**Project:** AI Workforce Analytics Platform

**Version:** 1.0

**Document Type:** Functional Requirements Specification (FRS)

**Status:** Planning Phase

---

# 1. Purpose

This document defines the functional requirements of the AI Workforce Analytics Platform. It specifies the features and capabilities the system must provide to meet business objectives and user needs.

The purpose of this document is to establish a clear understanding of system functionality before implementation begins.

---

# 2. Scope

This document covers all functional features included in Version 1 of the platform, including:

- User Authentication
- Role-Based Access Control
- Employee Management
- Single Employee Prediction
- Batch Prediction
- Explainable AI
- Recommendation Engine
- Dashboard & Analytics
- Prediction History
- Reporting
- User Administration

Future enhancements such as AI chat assistants, automated model retraining, and HR software integrations are outside the scope of this document.

---

# 3. User Roles

| Role               | Description                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| Administrator      | Manages users, departments, and platform settings.                      |
| HR Manager         | Accesses organization-wide analytics, predictions, and reports.         |
| Department Manager | Accesses only employees and analytics within their assigned department. |

---

# 4. Functional Requirements

---

# FR-01 User Authentication

## Description

The system shall authenticate registered users before granting access to protected resources.

## Inputs

- Email Address
- Password

## Process

- Validate credentials.
- Verify hashed password.
- Generate JWT access token.
- Retrieve user role.

## Outputs

- Access Token
- User Information
- Assigned Role

## Acceptance Criteria

- Registered users can log in successfully.
- Invalid credentials return an appropriate error message.
- Unauthenticated users cannot access protected routes.

---

# FR-02 Role-Based Access Control

## Description

The system shall restrict access to resources based on user roles.

## Permissions

### Administrator

- Manage users
- Manage departments
- View all employees
- View all analytics
- Configure platform settings

### HR Manager

- View organization-wide data
- Predict employee attrition
- Upload employee datasets
- Generate reports

### Department Manager

- View employees within assigned department
- Predict attrition
- View department analytics

## Acceptance Criteria

- Users can only access features permitted by their assigned role.
- Unauthorized requests return a "403 Forbidden" response.

---

# FR-03 Employee Management

## Description

The system shall maintain employee records for prediction and analytics.

## Capabilities

- Add employee
- Edit employee
- Delete employee
- Search employee
- Filter employee list
- View employee profile

## Acceptance Criteria

- Employee records are stored successfully.
- Duplicate employee IDs are not allowed.
- Deleted employees are removed from active records.

---

# FR-04 Single Employee Prediction

## Description

The system shall predict the likelihood of employee attrition for an individual employee.

## Inputs

Employee information including:

- Age
- Department
- Job Role
- Monthly Income
- Years at Company
- Job Satisfaction
- Overtime
- Work-Life Balance
- Education
- Other model features

## Process

- Validate input.
- Apply preprocessing pipeline.
- Run trained ML model.
- Calculate prediction probability.
- Determine risk category.
- Generate SHAP explanation.
- Generate recommendations.
- Store prediction.

## Outputs

- Attrition Probability
- Risk Category
- Confidence Score
- SHAP Explanation
- Retention Recommendations

## Acceptance Criteria

- Prediction completes successfully.
- Prediction is stored in the database.
- SHAP explanation is generated.
- Recommendations are displayed.

---

# FR-05 Batch Prediction

## Description

The system shall predict attrition for multiple employees uploaded via CSV.

## Inputs

CSV File

## Process

- Validate file structure.
- Parse employee records.
- Run predictions.
- Generate recommendations.
- Store prediction history.

## Outputs

- Prediction Results
- Downloadable CSV
- Summary Statistics

## Acceptance Criteria

- Invalid CSV files are rejected.
- Valid files are processed successfully.
- Prediction results can be downloaded.

---

# FR-06 Explainable AI

## Description

The system shall explain each prediction using SHAP.

## Information Displayed

- Feature Importance
- Positive Risk Factors
- Negative Risk Factors
- SHAP Visualization
- Plain-English Explanation

Example

> High attrition risk due to frequent overtime, low job satisfaction, and limited career progression.

## Acceptance Criteria

- Every prediction includes an explanation.
- Feature contributions are visible.
- Explanations are understandable by non-technical users.

---

# FR-07 Recommendation Engine

## Description

The system shall generate personalized retention recommendations based on SHAP feature contributions.

## Example Rules

| Model Insight             | Recommendation                           |
| ------------------------- | ---------------------------------------- |
| High Overtime             | Reduce workload or redistribute tasks    |
| Low Job Satisfaction      | Schedule employee engagement initiatives |
| Low Work-Life Balance     | Encourage flexible work arrangements     |
| Long Time Since Promotion | Review promotion eligibility             |

## Acceptance Criteria

- Every prediction includes recommendations.
- Recommendations correspond to the employee's risk factors.

---

# FR-08 Dashboard

## Description

The dashboard shall provide an overview of workforce analytics.

## Dashboard Components

- Total Employees
- Attrition Rate
- High-Risk Employees
- Low-Risk Employees
- Department Distribution
- Recent Predictions
- Monthly Trends

## Acceptance Criteria

- Dashboard loads successfully.
- Statistics reflect current database values.
- Charts update automatically.

---

# FR-09 Analytics

## Description

The system shall provide interactive workforce analytics.

## Analytics

- Department-wise Attrition
- Salary Distribution
- Age Distribution
- Overtime Analysis
- Job Satisfaction Analysis
- Attrition by Business Travel
- Attrition by Education
- Attrition Trends

## Acceptance Criteria

- Charts display correct data.
- Filters update visualizations dynamically.

---

# FR-10 Prediction History

## Description

The system shall maintain a history of previous predictions.

## Features

- View history
- Search
- Sort
- Filter
- Delete history
- View prediction details

## Acceptance Criteria

- All predictions are stored.
- History is searchable.
- History can be filtered.

---

# FR-11 Reporting

## Description

The system shall generate downloadable reports.

## Supported Formats

- CSV
- PDF (Future Enhancement)
- Excel (Future Enhancement)

## Report Contents

- Employee Summary
- Prediction Results
- Department Statistics
- Recommendations

## Acceptance Criteria

- Reports download successfully.
- Reports reflect selected filters.

---

# FR-12 User Management

## Description

Administrators shall manage user accounts.

## Features

- Create User
- Update User
- Delete User
- Reset Password
- Assign Roles

## Acceptance Criteria

- Only administrators can manage users.
- Role updates take effect immediately.

---

# FR-13 API Services

The backend shall expose RESTful API endpoints.

| Method | Endpoint        | Description         |
| ------ | --------------- | ------------------- |
| POST   | /auth/login     | Authenticate user   |
| POST   | /auth/register  | Register user       |
| GET    | /employees      | Retrieve employees  |
| POST   | /employees      | Add employee        |
| PUT    | /employees/{id} | Update employee     |
| DELETE | /employees/{id} | Delete employee     |
| POST   | /predict        | Single prediction   |
| POST   | /predict/batch  | Batch prediction    |
| GET    | /analytics      | Dashboard analytics |
| GET    | /history        | Prediction history  |

---

# 5. Functional Dependencies

| Requirement           | Depends On         |
| --------------------- | ------------------ |
| Prediction            | Authentication     |
| Batch Prediction      | Authentication     |
| Recommendation Engine | Prediction         |
| SHAP Explanation      | Prediction         |
| Dashboard             | Database           |
| Analytics             | Database           |
| Reports               | Prediction History |

---

# 6. Assumptions

- Users possess valid login credentials.
- Employee data is available for prediction.
- The trained ML model has been deployed.
- The preprocessing pipeline matches the training pipeline.

---

# 7. Constraints

- Version 1 supports structured employee datasets only.
- Predictions are generated using a pre-trained model.
- Recommendations are rule-based.
- Internet connectivity is required to access the platform.

---

# 8. Traceability

| Business Goal               | Functional Requirement |
| --------------------------- | ---------------------- |
| Predict employee attrition  | FR-04                  |
| Explain predictions         | FR-06                  |
| Improve employee retention  | FR-07                  |
| Analyze workforce trends    | FR-08, FR-09           |
| Secure access               | FR-01, FR-02           |
| Maintain prediction history | FR-10                  |

---

# 9. Approval

This document serves as the baseline functional specification for Version 1. Any additional functionality proposed after approval shall be evaluated as a future enhancement or a new project version.