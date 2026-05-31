# Dataset for Online Shoppers Intention Prediction

## Dataset Name
Online Shoppers Purchasing Intention Dataset

## Dataset Source Link
https://www.kaggle.com/datasets/henrysue/online-shoppers-intention

## Dataset Description
This dataset contains real e-commerce session data collected from an online retailer. Each row represents a single user browsing session and captures behavioral metrics such as page visits, duration, bounce rate, exit rate, page value, traffic source, and session metadata.

## Number of Records
12,330 total user sessions

## Number of Features
18 features including the target variable

## Target Variable Description
- **Revenue**: Binary label indicating whether the session resulted in a purchase.
  - `True` or `Yes` indicates a purchase was made.
  - `False` or `No` indicates the user left without buying.

## Dataset Usage in this Project
This dataset is used to build and compare multiple deep learning models for purchase intention prediction. The workflow includes data loading, cleaning, categorical encoding, feature scaling, model training, evaluation, and visualization.

## Data Preprocessing Considerations
- Duplicate sessions are removed to prevent bias.
- Missing values are handled by median imputation for numeric features and mode imputation for categorical features.
- Categorical variables are encoded using label encoders so neural networks can process them.
- Numerical features are scaled with StandardScaler to stabilize training and improve convergence.
- Train/test split is stratified to preserve the target class distribution.

## Why this Dataset is Suitable for Purchase Intention Prediction
The dataset contains comprehensive session-level behavior signals, such as product page views, page duration, bounce rate, and session source, which are strong indicators of purchase intent. The binary target is directly aligned with the business goal of predicting whether a visitor will convert, making this dataset ideal for classification and deep learning research in e-commerce analytics.
