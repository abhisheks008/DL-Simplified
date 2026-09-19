# Model

## Overview

This notebook demonstrates the complete workflow for predicting diabetes using an Artificial Neural Network (ANN).

The workflow includes preprocessing, feature encoding, model development, training, evaluation, and prediction.

---

## Workflow

- Import Libraries
- Load Dataset
- Data Cleaning
- Categorical Encoding (one-hot)
- Feature Alignment between train and test sets
- Feature Scaling
- Stratified Train-Test Split
- ANN Model Development
- Model Training
- Threshold Tuning
- Performance Evaluation
- Prediction

---

## Data Preprocessing

- Removed irrelevant columns (e.g., id)
- Handled categorical features using one-hot encoding
- Ensured consistent feature alignment between training and test data
- Applied feature scaling using MinMaxScaler
- Used stratified train-test split to maintain class balance

---

## Neural Network Architecture

The model consists of:

- Input Layer (matching number of features)
- Dense Layer (256 neurons, ReLU)
- Batch Normalization
- Dropout (0.3)
- Dense Layer (128 neurons, ReLU)
- Dropout (0.2)
- Dense Layer (64 neurons, ReLU)
- Output Layer (Sigmoid)

**Loss Function:** Binary Crossentropy
**Optimizer:** Adam

---

## Training Strategy

- Trained for a fixed number of epochs with a large batch size
- Used Batch Normalization and Dropout for regularization
- Tuned the decision threshold using Precision-Recall analysis (rather than default 0.5)
- Evaluated model using:
  - Accuracy
  - Precision
  - Recall
  - F1-score

---

## Required Libraries

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- tensorflow
- jupyter

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Running the Notebook

Start Jupyter Notebook and run all cells sequentially.

```bash
jupyter notebook
```

---

## Results

- Achieved balanced performance across both classes
- Improved recall for the positive class through threshold tuning
- Reduced overfitting using Batch Normalization and Dropout
- Current accuracy is moderate and stable

---

## Applications

- Diabetes Risk Screening
- Preventive Healthcare Analytics
- Patient Risk Stratification
- Clinical Decision Support

---

## Future Improvements

- Hyperparameter tuning
- Learning rate adjustments
- Architecture optimization
- Feature engineering
- Early stopping to further reduce overfitting
- Advanced regularization techniques

---

## Notes

This notebook demonstrates an end-to-end deep learning pipeline for binary diabetes classification using TensorFlow and Keras.