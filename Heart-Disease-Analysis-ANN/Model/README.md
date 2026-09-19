# Model

## Overview

This notebook implements an Artificial Neural Network (ANN) to predict the probability of heart disease based on patient health indicators. The model performs binary classification and was developed for a Kaggle competition.

---

## Workflow

- Import Libraries
- Load Dataset
- Data Cleaning
- Categorical Value Mapping (Presence/Absence → 1/0)
- Train-Test Split
- ANN Model Development
- Model Training
- Performance Evaluation
- Prediction & Submission

---

## Data Preprocessing

- Dropped irrelevant columns (e.g., id)
- Mapped target labels (Presence/Absence) to binary values (1/0)
- Boolean columns converted to 0/1
- Target variable separated before training

---

## Neural Network Architecture

The model consists of:

- Input Layer (matching number of features)
- Dense Layer (128 neurons, ReLU)
- Dropout (0.3)
- Dense Layer (64 neurons, ReLU)
- Dropout (0.3)
- Dense Layer (32 neurons, ReLU)
- Output Layer (Sigmoid)

**Loss Function:** Binary Crossentropy
**Optimizer:** Adam
**Metric:** Accuracy

---

## Training

- Train-test split applied (80/20)
- Model trained using the Adam optimizer over multiple epochs with a large batch size
- Dropout layers used for regularization

---

## Evaluation

- Accuracy score
- Precision, Recall, and F1-score
- Confusion Matrix visualization

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

## Applications

- Heart Disease Risk Screening
- Preventive Healthcare Analytics
- Patient Risk Stratification
- Clinical Decision Support

---

## Future Improvements

- Apply feature scaling (e.g., MinMax or Standard scaling)
- One-hot encode categorical features instead of using raw values
- Hyperparameter tuning
- Deeper architectures
- Additional regularization techniques

---

## Conclusion

This project demonstrates the application of an ANN for medical risk prediction, emphasizing proper preprocessing, model design, and evaluation. Performance can be further improved through hyperparameter tuning, feature scaling, and regularization techniques.