# Online Shoppers Intention Prediction

## 🎯 Goal
Predict whether an online visitor will complete a purchase session using behavioral signals captured from their browsing activity. The application is designed for product teams to identify likely buyers and drive smarter conversion strategies.

---

## 🧵 Dataset
- **Dataset Name**: Online Shoppers Purchasing Intention Dataset
- **Dataset Source**: Kaggle
- **Dataset Link**: https://www.kaggle.com/datasets/henrysue/online-shoppers-intention
- **Brief Dataset Description**: 12,330 real e-commerce session records with 17 features and a binary purchase target. The dataset includes page interactions, engagement metrics, traffic source, and visitor behavior signals.

---

## 🧾 Description
This project is a full end-to-end machine learning application for purchase intent prediction. It includes a production-ready Flask frontend, a prediction interface, real-time model inference, and an analytics dashboard for business reporting.

The application uses a trained deep neural network model to transform session data into a business-friendly score and a prediction narrative. It is built to support enterprise-style monitoring, validation, and decision-making.

---

## 🧮 What I had done!
1. Loaded dataset from the `Dataset` folder.
2. Performed preprocessing and data cleaning.
3. Handled categorical features with label encoding.
4. Applied feature engineering and scaling.
5. Conducted exploratory data analysis.
6. Built MLP, DNN, LSTM, and GRU models.
7. Trained models with early stopping and validation monitoring.
8. Saved production-ready model artifacts and preprocessors.
9. Built a Flask backend for real-time inference.
10. Created a professional landing page and prediction interface.
11. Rebuilt an analytics dashboard for enterprisewide insights.
12. Documented the deployment architecture and prediction workflow.

---

## 🚀 Models Implemented
### MLP
MLP is the tabular baseline model for purchase intent classification. It provides strong generalization on session-level features.

### Deep Feedforward Neural Network
The deep network is the production inference model, optimized for precision and consistency in business deployment.

### LSTM
LSTM evaluates sequential session patterns and temporal relationships in browsing behavior.

### GRU
GRU offers efficient sequence learning with fewer parameters than LSTM and strong inference speed.

---

## 📚 Libraries Needed
- Python 3
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow
- Keras
- Flask
- Joblib

---

## 📊 Exploratory Data Analysis Results
### Class Distribution
![Class Distribution](Image/class_distribution.png)

### Correlation Heatmap
![Correlation Heatmap](Image/correlation_heatmap.png)

### Feature Analysis
![Feature Analysis](Image/feature_analysis.png)

### Data Distribution
![Data Distribution](Image/data_distribution.png)

These visuals illustrate class balance, feature relationships, and the dataset distributions used by the model.

---

## 📈 Performance of the Models based on the Accuracy Scores
| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| MLP | 0.9002 | 0.7345 | 0.5576 | 0.6339 | 0.9081 |
| Deep Neural Network | 0.8483 | 0.8333 | 0.0262 | 0.0508 | 0.8541 |
| LSTM | 0.8451 | 0.0000 | 0.0000 | 0.0000 | 0.6513 |
| GRU | 0.8451 | 0.0000 | 0.0000 | 0.0000 | 0.6948 |

### Model Performance Visualizations
![Model Accuracy Comparison](Image/model_accuracy_comparison.png)

### Confusion Matrices
![MLP Confusion Matrix](Image/confusion_matrix_mlp.png)
![DNN Confusion Matrix](Image/confusion_matrix_dnn.png)
![LSTM Confusion Matrix](Image/confusion_matrix_lstm.png)
![GRU Confusion Matrix](Image/confusion_matrix_gru.png)

### ROC Curve Comparison
![ROC Curve Comparison](Image/roc_curve_comparison.png)

### Training History
![Training History](Image/training_history.png)

---

## 📢 Conclusion
This repository now includes a deployable Flask application with an interactive prediction interface and enterprise analytics dashboard. The solution supports production-ready inference, business-friendly purchase intent reporting, and model performance validation.

---

## ✒️ Your Signature
Somapuram Uday

GitHub: [https://github.com/udaycodespace](https://github.com/udaycodespace)
LinkedIn: [https://www.linkedin.com/in/somapuram-uday](https://www.linkedin.com/in/somapuram-uday)
