# Bank Churn Prediction using Deep Learning

## Overview

This project focuses on predicting customer churn in the banking sector using deep learning techniques. Customer churn prediction helps financial institutions identify customers who are likely to leave the bank, enabling proactive retention strategies.

The project implements and compares multiple deep learning architectures designed for tabular data classification tasks.

---

## Dataset

The dataset contains customer information such as:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card Status
* Active Membership Status
* Estimated Salary

**Target Variable:**

* `Exited`

  * 0 → Customer stays
  * 1 → Customer leaves

---

## Project Workflow

1. Data Loading and Exploration
2. Data Cleaning and Preprocessing
3. Feature Engineering
4. Handling Class Imbalance
5. Model Training
6. Model Evaluation
7. Performance Comparison

---

## Models Implemented

### 1. Artificial Neural Network (ANN)

A baseline feed-forward neural network used for binary classification.

### 2. TabNet

A deep learning architecture specifically designed for tabular datasets using sequential attention mechanisms.

### 3. FT-Transformer

A transformer-based architecture adapted for structured/tabular data.

### 4. Autoencoder + Classifier

An autoencoder is first trained to learn compact feature representations, followed by a classifier trained on the encoded features.

---

## Data Preprocessing

The following preprocessing steps were applied:

* Missing value checking
* Label encoding
* One-hot encoding of categorical features
* Feature scaling
* Train-test split
* Class imbalance handling using SMOTE

---

## Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

---

## Results

The project compares multiple deep learning approaches and highlights their effectiveness in predicting customer churn.

Performance comparison is carried out using standard classification metrics and ROC curves.

---

## Libraries Used

```python
numpy
pandas
matplotlib
seaborn
scikit-learn
tensorflow
torch
pytorch-tabnet
imbalanced-learn
```

---


## Future Improvements

* Hyperparameter tuning
* Ensemble learning approaches
* Explainable AI techniques (SHAP/LIME)
* Deployment using Flask/FastAPI
* Real-time churn prediction pipeline

---

## Author

Raaghav Kapoor

Developed as part of an open-source contribution to DL-Simplified.
