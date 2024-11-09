import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_layer_size, hidden_layer_size, output_layer_size, X):
        self.input_layer_size = input_layer_size
        self.hidden_layer_size = hidden_layer_size
        self.output_layer_size = output_layer_size

        # Initialize the weights with random values
        self.W1 = np.random.randn(input_layer_size, hidden_layer_size)
        self.W2 = np.random.randn(hidden_layer_size, output_layer_size)

        # Initialize the biases with zeros
        self.b1 = np.zeros((1, hidden_layer_size))
        self.b2 = np.zeros((1, output_layer_size))

    def sigmoid(self, x):
        x = np.array(x, dtype=float)
        return 1 / (1 + np.exp(-x))

    def forward_propagation(self, X):
        # Calculate the hidden layer activations
        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = self.sigmoid(self.Z1)

        # Calculate the output layer activations
        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        self.A2 = self.sigmoid(self.Z2)

        return self.A2

    def backward_propagation(self, X, Y, output, learning_rate):
        # Reshape Y to match the shape of output
        Y = Y.values.reshape(-1, 1)

        # Calculate the error in the output layer
        dZ2 = output - Y
        dW2 = np.dot(self.A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)

        # Calculate the error in the hidden layer
        dZ1 = np.dot(dZ2, self.W2.T) * (self.A1 * (1 - self.A1))
        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)
        self.W1 = self.W1.astype('float64')
        dW1 = dW1.astype('float64')
        # Update the weights and biases
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2

    def loss(self, y_pred, y_true):
        y_true = y_true.values.reshape(-1, 1)
        y_pred_binary = (y_pred >= 0.5).astype(int)
        y_true_binary = (y_true >= 0.5).astype(int)
        mse = np.mean((y_pred - y_true_binary)**2)
        return mse

    def accuracy(self, y_pred, y_true):
        y_true = y_true.values.reshape(-1, 1)
        y_pred_binary = (y_pred >= 0.5).astype(int)
        y_true_binary = (y_true >= 0.5).astype(int)
        return (y_pred_binary == y_true_binary).mean() * 100

    def rmsee(self, y_pred, y_train):
        mse = mean_squared_error(y_train, y_pred)
        rmse = mean_squared_error(y_train, y_pred, squared=False)
        return rmse

    def train(self, X, Y, epoch=10, alpha=0.01):
        acc = []
        losss = []
        rm = []
        for j in range(epoch):
            out = self.forward_propagation(X)
            self.backward_propagation(X, Y, out, alpha)
            acc.append(self.accuracy(out, Y))
            losss.append(self.loss(out, Y))
            rm.append(self.rmsee(out, Y))

        return acc, losss, rm

    def predict(self, X):
        # Forward propagation to get the output
        output = self.forward_propagation(X)

        # Apply the threshold to classify the output
        predictions = (output >= 0.5).astype(int)

        return predictions

# Streamlit app
st.title("Groundwater Quality Prediction")

uploaded_file = st.file_uploader("../Ground Water.csv", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Data preprocessing
    numeric_columns = data.select_dtypes(include='number').columns
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

    # Select only numeric columns for quantile calculations
    numeric_data = data.select_dtypes(include=[np.number])
    data[numeric_data.columns] = numeric_data.clip(lower=numeric_data.quantile(0.01), upper=numeric_data.quantile(0.99), axis=1)

    # Encode categorical variables
    data = pd.get_dummies(data)

    # Scale numerical variables
    scaler = StandardScaler()
    data[data.select_dtypes(include=['float64']).columns] = scaler.fit_transform(data.select_dtypes(include=['float64']))

    data = data.drop(data.columns[[1, 2]], axis=1)
    X = data.iloc[:, :-3]
    y = data.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    # Define your ANN architecture
    input_layer_size = X_train.shape[1]
    hidden_layer_size = 10
    output_layer_size = 1

    # Initialize and train the neural network
    nn = NeuralNetwork(input_layer_size, hidden_layer_size, output_layer_size, X_train)
    acc, losss, rm = nn.train(X_train, y_train, epoch=10, alpha=0.01)

    # Make predictions
    predictions = nn.predict(X_test)

    # Display results
    st.write("Predictions:", predictions)
    accuracy = nn.accuracy(predictions, y_test)
    st.write("Test Accuracy:", accuracy)

    # Print messages for groundwater quality
    for i, prediction in enumerate(predictions):
        if prediction == 1:
            st.write(f"Sample {i+1}: Groundwater is harmful.")
        else:
            st.write(f"Sample {i+1}: Groundwater is not harmful.")

    # Plotting accuracy
    st.subheader("Accuracy over Time")
    fig, ax = plt.subplots()
    ax.plot(acc)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Accuracy")
    st.pyplot(fig)

    # Plotting Loss
    st.subheader("Loss over Time")
    fig, ax = plt.subplots()
    ax.plot(losss)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    st.pyplot(fig)

    # Plotting RMSE
    st.subheader("RMSE over Time")
    fig, ax = plt.subplots()
    ax.plot(rm)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("RMSE value")
    st.pyplot(fig)
