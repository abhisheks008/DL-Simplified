# Dataset

## Description

This project uses the **Telco Customer Churn** dataset, which contains customer-level data for a telecom company, including demographics, account information, subscribed services, billing details, and whether the customer churned.

---

## Dataset Information

- One row per customer
- Mix of categorical and numerical features (e.g., gender, contract type, tenure, monthly charges)
- Target column: `Churn` (Yes/No)
- Suitable for binary classification

---

## Key Columns

- `customerID` — unique customer identifier (dropped during preprocessing)
- `gender`, `SeniorCitizen`, `Partner`, `Dependents` — demographic info
- `tenure` — number of months the customer has stayed
- `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `TechSupport`, etc. — subscribed services
- `Contract`, `PaperlessBilling`, `PaymentMethod` — account/billing details
- `MonthlyCharges`, `TotalCharges` — billing amounts
- `Churn` — target variable (Yes/No)

---

## Dataset Source

The dataset is publicly available on Kaggle.

**Dataset Link:**
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

## Dataset File

WA_Fn-UseC_-Telco-Customer-Churn.csv


---

## Preprocessing Notes

- Rows with blank/invalid `TotalCharges` values are removed.
- `customerID` is dropped (not predictive).
- Categorical Yes/No fields are converted to 0/1.
- `InternetService`, `Contract`, and `PaymentMethod` are one-hot encoded.
- `tenure`, `MonthlyCharges`, and `TotalCharges` are scaled using MinMaxScaler.

---

## Applications

- Customer Churn Analysis
- Retention Modeling
- Subscription Business Analytics

---

## Acknowledgement

Special thanks to the dataset creator and the Kaggle community for making this dataset publicly available for educational and research purposes.