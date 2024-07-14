# **Apple Historic Stock Price Analysis**

### 🎯 Goal
To analyze and predict the future stock prices of Apple using various machine learning and deep learning models.

### Purpose
The purpose of this project is to develop and compare the performance of different models, including LSTM, LSTM+CONV1D, and the Prophet Model, in predicting the stock prices of Apple. This can help investors make informed decisions by providing insights into future stock price movements.

### 🧵 Dataset
The dataset used in this project is: https://www.kaggle.com/datasets/meetnagadia/apple-stock-price-from-19802021/data

### 🧾 Description
This is a Dataset for Stock Prediction on Apple Inc. This dataset start from 1980 to 2021. It was collected from Yahoo Finance. Here's a breakdown of the dataset columns:

- **Date:** The date of the stock price record, providing a chronological timeline for the dataset.
- **Open:** The opening price, representing the initial trading price of Apple Inc.'s stock on a given day.
- **High:** The highest stock price during a specific period, providing insights into peak price levels.
- **Low:** The lowest stock price observed during a defined period, indicating potential fluctuations in value.
- **Close:** The closing price, representing the last recorded price at the end of a regular trading session.
- **Adj Close (Adjusted Close):** Adjusts the closing price for corporate actions, offering a more accurate representation of the stock's true value.
- **Volume:** Measures the number of shares traded, providing insights into interest and activity in Apple Inc.'s stock.

### 🚀 Models Implemented
1. LSTM (Long Short-Term Memory)
2. LSTM+CONV1D (Combining LSTM and 1D Convolutional Layers)
3. Prophet Model (Developed by Facebook for time series forecasting)

### 📚 Libraries Needed
- TensorFlow: For building and training deep learning models.
- Keras: For simplifying the creation and training of neural networks.
- NumPy: For numerical computations and array operations.
- Pandas: For data manipulation and analysis.
- Matplotlib: For plotting and visualizing data.

### 📊 Data Visualization
![Close Price History Plot](https://github.com/user-attachments/assets/155d8d3a-f065-4f4b-b5b5-8b126694c22e)
![Scatter Plot](https://github.com/user-attachments/assets/562841ee-830a-4afa-ba55-074cebafae8c)
![Histogram](https://github.com/user-attachments/assets/cf71256a-3d2b-4293-98df-38cb90e97be7)
![Cross Price Seasonality](https://github.com/user-attachments/assets/a2532bcb-b137-41cb-98be-35704ddc1e86)
![Correlation Matrix](https://github.com/user-attachments/assets/d00419ed-4bc8-4f03-8e23-c8d52a503344)

## 📈 Performance of the Models based on the Accuracy Scores
| Model | Accuracy |
|-------|-------------|
| LSTM | 93.0% |
| LSTM+ Conv1D | 98.11% |
<img width="703" alt="Prophet Model" src="https://github.com/user-attachments/assets/1639d413-55a3-458f-b5f5-08e930d86385">

### 📢 Conclusion
Based on the evaluation metrics, the LSTM+CONV1D model outperforms the LSTM model in predicting Apple stock prices. The combination of LSTM and 1D convolutional layers allows the model to capture both long-term dependencies and local patterns in the time series data, leading to more accurate predictions.

### Best Fitted Model
The LSTM+CONV1D model is identified as the best-fitted model for predicting Apple stock prices due to its higher accuracy compared to the LSTM model.

## ✒️ Contributor
- Name: Khushi Kalra
- Github: https://www.github.com/abckhush
