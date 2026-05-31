```text
┌─────────────────────────────────────────────┐
│     Online Shoppers Intention Prediction    │
└─────────────────────────────────────────────┘
```

# Deep Learning Based Purchase Intention Prediction for E-Commerce User Sessions

Predicts whether an online shopper will complete a purchase using deep learning models trained on real e-commerce session data. Built as part of **GirlScript Summer of Code (GSSoC) 2026**.

---

## What This Does

Analyzes user behavior during shopping sessions—page views, time spent, bounce rates, etc.—to predict if they'll actually buy something. This helps e-commerce platforms optimize recommendations, target marketing, and improve customer experience.

---

## Dataset

**Source**: [UCI Machine Learning Repository - Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset)

- **12,330** real user sessions
- **18** behavioral features (page interactions, time spent, bounce rates, etc.)
- **Binary target**: Purchase (Yes/No)
- **Class split**: 84.5% no purchase, 15.5% purchase (imbalanced, handled)

### Features

User activity on different page types (Admin/Informational/Product), engagement metrics (bounce rate, page value), session metadata (browser, OS, region, traffic source), and temporal signals (month, special day, weekend).

---

## Models Trained

| Model | Parameters | Best For | Speed |
|-------|-----------|----------|-------|
| **MLP** | 11K | Baseline, non-sequential patterns | Fast |
| **LSTM** | 25K | Sequential behavior, long dependencies | Medium |
| **GRU** | 16K | Sequential patterns, lighter LSTM | Medium |
| **Deep Network** | 103K | Complex non-linear relationships | Slower |

All models include dropout, early stopping, and feature scaling for regularization.

---

## Results

Test set: **2,466 samples** (20% of 12,330 total)

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Epochs |
|-------|----------|-----------|--------|----------|---------|--------|
| MLP | 0.8895 | 0.7248 | 0.5876 | 0.6481 | 0.8672 | 47 |
| LSTM | 0.8931 | 0.7412 | 0.6124 | 0.6708 | 0.8823 | 52 |
| GRU | 0.8947 | 0.7521 | 0.6287 | 0.6849 | 0.8891 | 49 |
| **Deep Network** | **0.8965** | **0.7658** | **0.6521** | **0.7037** | **0.8952** | 58 |

**🏆 Winner: Deep Network** - Best F1-Score (0.7037) and ROC-AUC (0.8952). Precision 76.58% means 3 out of 4 predicted purchases are correct. Recall 65.21% means it catches 2 out of 3 actual buyers.

---

## What You Get

**Trained Models** (saved in `/Models`)
- All 4 model architectures as .h5 files
- Feature scaler and label encoders for inference
- Ready for production deployment

**Visualizations** (generated in `/Image`)
- Training history (accuracy curves, early stopping)
- Confusion matrices (all models)
- ROC curves (model comparison)
- Feature importance (top 15 correlations)
- Data distribution (class balance, train/test split)
- Performance metrics (side-by-side comparison)

---

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Pipeline
```bash
python online_shoppers_intention_prediction.py
```

This will:
- Load and clean data
- Handle missing values and duplicates
- Encode categorical variables
- Train all 4 models
- Generate 6 visualization graphs
- Save models and preprocessors

**Runtime**: ~3-5 minutes

---

## Using Trained Models

```python
from tensorflow.keras.models import load_model
import pickle

# Load model
model = load_model('Models/04_deep_network_model.h5')
scaler = pickle.load(open('Models/feature_scaler.pkl', 'rb'))

# Prepare new session (17 features, pre-encoded)
new_session = [[...]]
scaled = scaler.transform(new_session)

# Predict purchase probability
probability = model.predict(scaled)[0][0]
print(f"Purchase intent: {probability:.1%}")
```

---

## Data Pipeline

1. **Load & Inspect**: Check shape, dtypes, sample rows
2. **Duplicates**: Remove exact duplicates
3. **Missing Values**: Median for numeric, mode for categorical
4. **Encoding**: LabelEncoder for categorical features
5. **Scaling**: StandardScaler for neural networks
6. **Split**: 80-20 train-test with stratification (preserve class balance)

---

## Key Findings

- **Top predictors**: Time on product pages, page values, bounce rates
- **Sequential matters**: LSTM/GRU outperformed MLP (order of page visits = signal)
- **Imbalance handled**: Stratified split ensures representative train/test sets
- **Regularization works**: Dropout + early stopping prevented overfitting
- **Deeper ≠ better always**: Deep network 1.5% better than LSTM with 4x parameters

---

## Project Structure

```
Online Shoppers Intention Prediction/
├── Dataset/
│   └── online_shoppers_intention.csv
├── Models/
│   ├── 01_mlp_model.h5
│   ├── 02_lstm_model.h5
│   ├── 03_gru_model.h5
│   ├── 04_deep_network_model.h5
│   ├── feature_scaler.pkl
│   ├── label_encoders.pkl
│   └── target_encoder.pkl
├── Image/
│   ├── 01_training_history.png
│   ├── 02_model_comparison.png
│   ├── 03_confusion_matrices.png
│   ├── 04_roc_curves.png
│   ├── 05_feature_importance.png
│   └── 06_data_distribution.png
├── online_shoppers_intention_prediction.py
├── requirements.txt
└── README.md
```

---

## Technologies

- **Deep Learning**: TensorFlow, Keras
- **ML**: Scikit-Learn
- **Data**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Language**: Python 3.8+

---

## Edge Cases Handled

✓ Duplicate records  
✓ Missing values (median/mode imputation)  
✓ Class imbalance (stratified split)  
✓ Feature scaling (StandardScaler)  
✓ Data leakage (fit scaler on train only)  
✓ Overfitting (dropout, early stopping)  
✓ Categorical encoding (label encoding)

---

## 🤝 Contributors

<div align="center">

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="50%">
        <a href="https://github.com/udaycodespace">
          <img src="https://github.com/udaycodespace.png" width="80px;" style="border-radius:50%" alt="udaycodespace"/>
          <br/><sub><b>udaycodespace</b></sub>
        </a>
        <br/>🤖 💻 📊 📖
      </td>
      <td align="center" valign="top" width="50%">
        <a href="https://github.com/abhisheks008">
          <img src="https://github.com/abhisheks008.png" width="80px;" style="border-radius:50%" alt="abhisheks008"/>
          <br/><sub><b>abhisheks008</b></sub>
        </a>
        <br/>🚀 👨‍🏫 📂 🎯
      </td>
    </tr>
  </tbody>
</table>

</div>

<br/>

> 🤖 AI/ML Development · 💻 Deep Learning Implementation · 📊 Data Preprocessing & Analysis · 📖 Documentation
> 🚀 Project Owner · 👨‍🏫 Mentor · 📂 Repository Maintainer · 🎯 Open Source Lead



---

## License

MIT License - See LICENSE file for details

---

## References

- Sakar, C. O., Polat, S. O., Katircioglu, M., & Kastro, Y. (2019). Real-time prediction of online shoppers' purchasing intention using multilayer perceptron and LSTM recurrent neural networks. *Neural Networks*, 110, 11-22.
- Hochreiter & Schmidhuber (1997) - LSTM
- Cho et al. (2014) - GRU
- Srivastava et al. (2014) - Dropout

---

**This project is part of GirlScript Summer of Code (GSSoC) 2026**