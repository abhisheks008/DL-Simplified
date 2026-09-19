# Model

## Overview

This notebook implements an Artificial Neural Network (ANN) to classify stellar objects into categories based on astronomical and spectral features.

---

## Workflow

- Import Libraries
- Load Dataset
- Explore Class Distributions
- Categorical Feature Encoding (LabelEncoder)
- Feature Scaling
- ANN Model Development
- Model Training
- Prediction & Submission

---

## Data Preprocessing

- Encoded categorical features (spectral_type, galaxy_population) and the target (class) using LabelEncoder
- Dropped the id column before training
- Standardized input features using StandardScaler

---

## Neural Network Architecture

The model consists of:

- Input Layer (matching number of features)
- Dense Layer (128 neurons, ReLU)
- Dense Layer (64 neurons, ReLU)
- Dense Layer (32 neurons, ReLU)
- Output Layer (3 neurons, Softmax)

**Loss Function:** Sparse Categorical Crossentropy
**Optimizer:** Adam
**Metric:** Accuracy

---

## Training

- Trained on the full training set (no held-out validation split)
- Training conducted across multiple fit calls (30 epochs, followed by two additional runs of 10 epochs each)

---

## Prediction

- Predicted class probabilities converted to class labels using argmax
- Predicted labels mapped back to original class names using the fitted LabelEncoder
- Final predictions exported to a submission file

---

## Required Libraries

- numpy
- pandas
- scikit-learn
- tensorflow
- keras
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

- Stellar Object Classification
- Astronomical Data Analysis
- Kaggle Competition Benchmarking

---

## Future Improvements

- Add a proper train-validation split for evaluation
- Hyperparameter tuning
- Cross-validation
- Dropout regularization
- Batch normalization
- Learning rate optimization
- Comparison with traditional machine learning models

---

## Conclusion

This project demonstrates the application of an ANN for multi-class stellar object classification, emphasizing feature encoding, scaling, and model design. Performance can be further improved through proper validation, regularization, and hyperparameter tuning.