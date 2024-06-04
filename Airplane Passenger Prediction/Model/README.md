## **Air Passenger Prediction**

### 🎯 **Goal**

The main goal of this project is to forecast future air passenger numbers using various time series forecasting techniques. The purpose is to compare the effectiveness of different models and determine the best one for accurate predictions.

### 🧵 **Dataset**

The dataset used is the [AirPassengers dataset](https://www.kaggle.com/datasets/flashgordon/air-passenger) which consists of monthly totals of US airline passengers from 1949 to 1960.

### 🧾 **Description**

This project involves time series analysis and forecasting on the AirPassengers dataset. We aim to explore the data, preprocess it for stationarity, apply various forecasting models, and compare their performance to determine the most accurate one.

### 🧮 **What I had done!**

1. **Load and Prepare Data**: Load the dataset, rename columns, convert the 'Month' column to datetime format, and set it as the index.
2. **Data Visualization**: Generate histograms and boxplots to understand data distribution and detect outliers.
3. **Seasonal Decomposition**: Analyze the seasonal patterns and trends.
4. **Stationarity Check**: Perform the Augmented Dickey-Fuller test and plot rolling statistics to check for stationarity.
5. **Deseasonality and Detrending**: Remove seasonality and trend components to make the data stationary.
6. **Model Implementation**: Implement and compare various forecasting models including Naïve Forecasting, ARIMA, SSA, Exponential Smoothing, FFT,LSTM,Prophet.
7. **Performance Evaluation**: Evaluate the models based on accuracy scores and visualize the results.

### 🚀 **Models Implemented**

- **Naïve Forecasting**: Simple method used as a benchmark.
- **ARIMA**: Used for its capability to handle different types of time series data.
- **SSA**: Chosen for its ability to decompose and reconstruct time series data.
- **Exponential Smoothing**: Selected for its effectiveness in capturing trends and seasonality.
- **FFT**: Used for its frequency domain analysis capability.
- **LSTM**: Chosen for its proficiency in handling sequential data and capturing long-term dependencies.
- **Prophet**: Model given by facebook for time series forecasting.

### 📚 **Libraries Needed**

- **NumPy**
- **Pandas**
- **Seaborn**
- **Matplotlib**
- **Statsmodels**
- **Scikit-learn**
- **TensorFlow**
- **Keras**


### 📊 **Exploratory Data Analysis Results**

#### Data
![Data](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/Data.png)

#### Autocorrelation
![Autocorrelation](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/Autocorrelation.png)

#### Boxplot
![Boxplot](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/boxplot.png)

#### Monthly Boxplot
![Monthly Boxplot](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/boxplot_monthly.png)

#### Decomposed Plot
![Decomposed Plot](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/decomposed_plot.png)

#### Histogram
![Histogram](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/histogram.png)


### 📈 **Performance of the Models**

- **ARIMA**: MAPE - 92.19
- **SSA**: MAPE - 100.00
- **Exponential Smoothing**: MAPE - 93.36
- **FFT**: MAPE - 96.46
- **LSTM**: MAPE - 86.57
- **Prophet**: MAPE - 93.39

  
#### Naive Forecast
![Naive Forecast](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/Naiveforec.png)


#### SSA Forecast
![SSA Forecast](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/SSA_forecast.png)

#### Exponential Smoothing
![Exponential Smoothing](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/expo.png)


#### LSTM Loss
![LSTM Loss](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/lstm_loss.png)


#### Prophet
![Prophet](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/prophet.png)

### 📢 **Conclusion**

The project successfully applied various time series forecasting models to the AirPassengers dataset and evaluated their performance based on Mean Absolute Percentage Error (MAPE). 


#### MAPE Comparison with Values
![MAPE Comparison with Values](https://github.com/manishh12/DL-Simplified/blob/main/Airplane%20Passenger%20Prediction/Images/mape_comparison_with_values.png)
### ✒️ **Your Signature**

[Manish Kumar Gupta]
