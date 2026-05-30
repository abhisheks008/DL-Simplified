# Real Estate Price Prediction — Model Documentation

## Objective
Predict real estate prices in Bengaluru using ML and Deep Learning models on the Bengaluru House Price dataset.

---

## Approach

### 1. Data Preprocessing
- Handle missing values in `bath`, `balcony`, `society`
- Parse `size`: extract numeric BHK (e.g., "2 BHK" → 2)
- Handle `total_sqft` ranges (e.g., "2000–2500" → 2250)
- Engineer `price_per_sqft` feature
- Remove outliers using mean ± std deviation per location group
- Group rare locations (< 10 listings) as "other"
- One-Hot Encode `location` and `area_type`

### 2. Exploratory Data Analysis (EDA)
- Price distribution across top locations (bar/violin plots)
- Correlation heatmap of numerical features
- Scatter: `total_sqft` vs `price`
- Box plots for outlier visualization

### 3. Models Implemented

#### Machine Learning Baseline
| Model | Notes |
|-------|-------|
| Linear Regression | Baseline |
| Lasso Regression | L1 regularization; feature selection |
| Random Forest | Ensemble; handles non-linearity |
| XGBoost | Gradient boosting; top ML performer |

Tuning: GridSearchCV with 5-Fold Cross Validation

#### Deep Learning Models
| Model | Notes |
|-------|-------|
| MLP (Feedforward NN) | ReLU + Dropout + BatchNorm layers |
| Wide & Deep Network | Linear memorization + deep generalization (Google) |
| TabNet | Attention-based; interpretable; great for tabular data |
| Embedding-based DNN | Learned entity embeddings for `location` + DNN |

Stack: TensorFlow/Keras or PyTorch

### 4. Evaluation Metrics
| Metric | Description |
|--------|-------------|
| R² Score | Proportion of variance explained |
| MAE | Mean Absolute Error (Lakhs INR) |
| RMSE | Root Mean Squared Error (Lakhs INR) |
| Cross-val Score | 5-fold CV for reliability |

---

## Results

> *(Update after running the notebook)*

| Model | R² | MAE | RMSE |
|-------|----|-----|------|
| Linear Regression | — | — | — |
| Lasso Regression | — | — | — |
| Random Forest | — | — | — |
| XGBoost | — | — | — |
| MLP | — | — | — |
| Wide & Deep | — | — | — |
| TabNet | — | — | — |
| Embedding DNN | — | — | — |

---

## Visualizations

> *(Add saved plots from the Images/ folder)*

- `price_distribution.png` — Price spread across locations
- `correlation_heatmap.png` — Feature correlation matrix
- `sqft_vs_price.png` — Scatter plot
- `model_comparison.png` — R² / RMSE comparison bar chart

---

## Conclusions

> *(Fill in after training)*

---

## Saved Artifacts
- `real_estate_best_model.pkl` — Best ML model (joblib)
- `real_estate_dl_model.h5` — Best DL model (Keras) or `.pt` (PyTorch)
