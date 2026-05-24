# 📈 Anomaly Detection in Time Series 

### 🔴 Goal
The objective of this project is to develop an effective model to detect anomalies in time series data using LSTM networks and other algorithms, aiming to achieve high accuracy and reliability.

### 📊 Dataset
The model uses a synthetic time series dataset generated for anomaly detection.

---

## 📝 Description
This project focuses on implementing a robust anomaly detection system using multiple algorithms on time series data, primarily leveraging LSTM (Long Short-Term Memory) networks. Additionally, models such as Facebook Prophet and Isolation Forest are applied to compare effectiveness in detecting anomalies. The process includes:

1. **Data Preprocessing**: Cleaning and preparing time series data for modeling.
2. **Exploratory Data Analysis (EDA)**: Analyzing data distribution, trends, and seasonality.
3. **Model Implementation**: Applying LSTM and other models to identify patterns and detect outliers.
4. **Performance Evaluation**: Assessing model accuracy to determine the best approach.

---

## 💻 Models Implemented
- **LSTM (Long Short-Term Memory) Network**
- **Facebook Prophet**
- **Isolation Forest**
- **Other Anomaly Detection Algorithms**

## 🛠️ Libraries Needed
To run this project, ensure you have the following libraries installed:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `tensorflow` (for LSTM models)
- `scikit-learn`
- `fbprophet`

Install the libraries using:
```bash
pip install numpy pandas matplotlib seaborn tensorflow scikit-learn fbprophet
```
## 📊 Exploratory Data Analysis (EDA) Results
In the EDA section, the following analyses were conducted:

- **Trend Analysis**: Understanding the overall trend in the data.
- **Seasonality Check**: Identifying any seasonal patterns.
- **Data Distribution**: Visualizing the spread and outliers in the data.

EDA findings helped in selecting and tuning models to better capture the characteristics of anomalies in time series data.

---

## 📈 Performance of the Models Based on Accuracy Scores
| Model                  | Accuracy Score |
|------------------------|----------------|
| **LSTM Network**       | 79%           |
| **Facebook Prophet**   | 86%           |
| **Isolation Forest**   | 88%           |

The table above compares model accuracy to highlight the most effective approach for detecting anomalies in this synthetic time series dataset.

---

## ✅ Conclusion
This project demonstrates that while LSTM networks provide a reliable approach to anomaly detection in time series data, models like Facebook Prophet and Isolation Forest achieved higher accuracy in this synthetic dataset, with Isolation Forest reaching the top performance at 88%. Each model's classification metrics indicate that they performed well in identifying non-anomalous points but faced challenges with anomaly recall due to the limited representation of anomalies in the dataset. The accuracy comparison suggests that Isolation Forest may be more effective for detecting anomalies in this context, making it the preferred choice over LSTM and Facebook Prophet.
