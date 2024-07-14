# **Tesla Historic Stock Price Analysis**

### 🎯 Goal
To predict the future stock prices of Tesla using deep learning models such as GRU and BiGRU.

### Purpose
The purpose of this project is to develop and compare the performance of two advanced recurrent neural network architectures, GRU and BiGRU, in predicting the stock prices of Tesla. This can help investors make informed decisions by providing insights into future stock price movements.

### 🧵 Dataset
The dataset used in this project is: https://www.kaggle.com/datasets/muhammadibrahimqasmi/tesla-stock-insights-and-predictions/data

### 🧾 Description
The dataset contains historical stock price data for Tesla. It includes features like Open, High, Low, and Close prices, and Volume. This data is used to train and evaluate the performance of the prediction models.

### 🚀 Models Implemented
1. GRU (Gated Recurrent Unit)
2. BiGRU (Bidirectional Gated Recurrent Unit)

### 📚 Libraries Needed
- TensorFlow: For building and training deep learning models.
- Keras: For simplifying the creation and training of neural networks.
- NumPy: For numerical computations and array operations.
- Pandas: For data manipulation and analysis.
- Matplotlib: For plotting and visualizing data.

### 📊 Exploratory Data Analysis Results
1. Data Visualization: Plotting the historical stock prices to understand the trends and patterns. Plots are in the `Images` folder.
2. Statistical Summary: Providing a summary of the data to get insights into the mean, median, standard deviation, etc.
3. Correlation Analysis: Analyzing the correlation between different features to understand their relationships.

### 📈 Performance of the Models based on the Accuracy Scores
The performance of the models is evaluated using the following metrics:

- R2 Score: Measures the proportion of the variance in the dependent variable that is predictable from the independent variables.
- RMSE (Root Mean Squared Error): Measures the average magnitude of the errors between predicted and actual values.

1. GRU Model
    - R2 Score: 0.929
    - RMSE:  0.0004
2. BiGRU Model
    - R2 Score: 0.971
    - RMSE: 0.0005


### 📢 Conclusion
Based on the evaluation metrics, the BiGRU model outperforms the GRU model in predicting Tesla stock prices. The bidirectional nature of the BiGRU allows it to capture the temporal dependencies in both forward and backward directions, leading to more accurate predictions.

### Best Fitted Model
The BiGRU model is identified as the best-fitted model for predicting Tesla stock prices due to its higher accuracy and lower RMSE compared to the GRU model.

## ✒️ Contributor
- Name: Khushi Kalra
- Github: https://www.github.com/abckhush
