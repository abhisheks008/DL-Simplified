# Model

## Overview

This notebook implements an Artificial Neural Network (ANN) to predict whether Spaceship Titanic passengers were transported, based on passenger and travel features.

---

## Workflow

- Import Libraries
- Load Dataset
- Data Cleaning
- Feature Engineering (split Cabin into deck, num, side)
- Missing Value Imputation (median for numeric, mode for categorical)
- Categorical Encoding (one-hot for HomePlanet, Destination, deck, side)
- Feature Scaling
- Stratified Train-Test Split
- ANN Model Development
- Model Training
- Performance Evaluation
- Prediction & Submission

---

## Data Preprocessing

- Dropped irrelevant columns (PassengerId, Name)
- Split Cabin into deck, num, and side
- Imputed missing numeric values with median (Age, RoomService, FoodCourt, ShoppingMall, Spa, VRDeck, num)
- Imputed missing categorical values with mode (CryoSleep, VIP)
- One-hot encoded categorical features (HomePlanet, Destination, deck, side)
- Applied MinMaxScaler to feature set
- Stratified train-test split to maintain class balance

---

## Neural Network Architecture

The model consists of:

- Input Layer (25 features)
- Dense Layer (20 neurons, ReLU)
- Dense Layer (15 neurons, ReLU)
- Dense Layer (10 neurons, ReLU)
- Output Layer (Sigmoid)

**Loss Function:** Binary Crossentropy
**Optimizer:** Adam
**Metric:** Accuracy

---

## Training

- Train-test split applied (80/20, stratified)
- Model trained using the Adam optimizer for 50 epochs with a batch size of 50

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

- Passenger Outcome Prediction
- Kaggle Competition Benchmarking
- Binary Classification Case Study

---

## Future Improvements

- Hyperparameter tuning (layers, units, learning rate)
- Dropout or regularization to reduce overfitting
- Additional feature engineering (total spending, family groups)
- Experiment with ensemble methods
- Class weighting or resampling if class imbalance affects performance

---

## Conclusion

This project demonstrates the application of an ANN for a binary passenger-outcome prediction task, emphasizing feature engineering, preprocessing, and model evaluation. Performance can be further improved through regularization and hyperparameter tuning.