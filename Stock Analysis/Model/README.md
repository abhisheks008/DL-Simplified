# Stock Price Prediction Models

## Overview

This project applies four deep learning architectures to predict Tesla's stock prices. The models used are:
1. **Recurrent Neural Network (RNN)**
2. **Long Short-Term Memory (LSTM)**
3. **Gated Recurrent Unit (GRU)**
4. **Convolutional Neural Network (CNN)**

The goal of the project is to compare these models' performance in terms of accuracy and prediction capabilities using Tesla stock price data. We evaluate model performance using **Mean Squared Error (MSE)** and visualize the predictions vs actual stock prices.

## Models Implemented

### 1. **Recurrent Neural Network (RNN)**

RNNs are effective in handling time-series data as they have an internal state that helps them remember previous time steps.

- **Architecture**: 2 RNN layers with 50 units each.
- **Loss function**: Mean Squared Error (MSE).
- **Optimizer**: Adam.
- **Visualization**: Actual vs predicted stock prices are plotted and saved as `rnn_stock_prediction.png`.

### 2. **Long Short-Term Memory (LSTM)**

LSTMs are a type of RNN that can capture long-term dependencies in time-series data, making them more effective in stock price prediction.

- **Architecture**: 2 LSTM layers with 50 units each.
- **Loss function**: Mean Squared Error (MSE).
- **Optimizer**: Adam.
- **Visualization**: Actual vs predicted stock prices are plotted and saved as `lstm_stock_prediction.png`.

### 3. **Gated Recurrent Unit (GRU)**

GRUs are similar to LSTMs but have fewer gates, making them computationally more efficient while retaining the ability to capture long-term dependencies.

- **Architecture**: 2 GRU layers with 50 units each.
- **Loss function**: Mean Squared Error (MSE).
- **Optimizer**: Adam.
- **Visualization**: Actual vs predicted stock prices are plotted and saved as `gru_stock_prediction.png`.

### 4. **Convolutional Neural Network (CNN)**

CNNs, typically used for image data, can also be adapted for time-series data to capture patterns and trends over time.

- **Architecture**: 2 Conv1D layers with 32 and 64 filters, followed by MaxPooling and Dense layers.
- **Loss function**: Mean Squared Error (MSE).
- **Optimizer**: Adam.
- **Visualization**: Actual vs predicted stock prices are plotted and saved as `cnn_stock_prediction.png`.

## Data Preprocessing

The dataset used for training is Tesla's stock prices, which includes columns like **Date**, **Close Price**, **Volume**, **Open Price**, **High**, and **Low**. The dataset is located in the `Dataset` folder, and the actual data is too large to include directly. A link to the dataset can be found in the `Dataset/README.md` file.

- **Data Loading**: The data is loaded using `pandas` from the CSV file.
- **Data Scaling**: The stock prices are scaled using `MinMaxScaler` to normalize the values between 0 and 1.
- **Sequence Creation**: The data is split into sequences to train the RNN, LSTM, GRU, and CNN models. We use a 60-day window to predict the next day's price.

## Visualizations

For each model, the following visualizations are generated:
- **Actual vs Predicted Prices**: A plot showing the actual stock prices vs the predicted prices for the test data.
- **Mean Squared Error (MSE)**: The performance of each model is measured using MSE. The lower the MSE, the better the model's predictions.

### 1. **RNN Visualization**

- **File**: `rnn_stock_prediction.png`
- **Description**: This image shows the predicted stock prices from the RNN model compared to the actual prices over time.

### 2. **LSTM Visualization**

- **File**: `lstm_stock_prediction.png`
- **Description**: This image shows the predicted stock prices from the LSTM model compared to the actual prices over time.

### 3. **GRU Visualization**

- **File**: `gru_stock_prediction.png`
- **Description**: This image shows the predicted stock prices from the GRU model compared to the actual prices over time.

### 4. **CNN Visualization**

- **File**: `cnn_stock_prediction.png`
- **Description**: This image shows the predicted stock prices from the CNN model compared to the actual prices over time.

## Results and Conclusions

- **RNN Model**: While the RNN model performs adequately in capturing the sequential patterns in stock prices, it is limited in handling long-term dependencies, which leads to some inaccuracies in longer time frames.
  
- **LSTM Model**: The LSTM model outperforms the RNN model as it can capture long-term dependencies more effectively, leading to better predictions on unseen data.
  
- **GRU Model**: The GRU model performs similarly to the LSTM but is computationally more efficient with fewer parameters. It also performs well in predicting stock prices.

- **CNN Model**: The CNN model can capture short-term patterns in the stock prices effectively, but it may struggle with long-term trends compared to LSTM and GRU.

In conclusion, while all models can predict stock prices to some extent, the **LSTM** and **GRU** models provide the most accurate predictions due to their ability to capture long-term dependencies in the data.

## File Structure

- **Dataset**: Contains the Tesla stock price data (link provided in `Dataset/README.md`).
- **Images**: Stores all the visualizations (predicted vs actual prices).
- **Model**: Contains the Jupyter Notebooks (`.ipynb`) for each model and their respective visualizations.

## Requirements

To run the models, make sure you have the following Python libraries installed:
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `tensorflow`

These can be installed by running:
```bash
pip install -r requirements.txt
