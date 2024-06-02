
# Turbofan Engine Prognostics Using NASA C-MAPSS Dataset
This repository contains the implementation of various deep learning models for predicting the Remaining Useful Life (RUL) of turbofan engines using the NASA C-MAPSS dataset. The models include Convolutional Neural Networks (CNN), Long Short-Term Memory networks (LSTM), and Gated Recurrent Units (GRU).

### Dataset
The NASA C-MAPSS dataset (Commercial Modular Aero-Propulsion System Simulation) provides realistic time-series data for large commercial turbofan engines. It includes multiple operational settings and fault conditions for four different engine models.

### Models
We have implemented the following models for RUL prediction:

- Convolutional Neural Network (CNN) <br>
CNNs are effective in capturing spatial hierarchies in data. In this project, CNNs are used to automatically learn and extract meaningful features from the time-series sensor data, which are then used to predict the RUL of the engines.

- Long Short-Term Memory Network (LSTM) <br>
LSTMs are a type of recurrent neural network (RNN) that are well-suited for learning from sequential data due to their ability to maintain long-term dependencies. LSTMs are used to capture the temporal dependencies in the time-series data, providing robust predictions for the RUL of the engines.

- Gated Recurrent Unit (GRU) <br>
GRUs are a variant of RNNs similar to LSTMs but with a simplified architecture. GRUs effectively capture temporal dependencies with fewer parameters, making them computationally efficient. GRUs are employed to process the sequence of sensor readings and predict the RUL.

### Libraries Used
- TensorFlow - For building and training the neural networks.
- Keras - High-level API for TensorFlow for easy and fast prototyping.
- NumPy - For numerical computations.
- Pandas - For data manipulation and analysis.
- Matplotlib - For plotting and visualizing results.
- Scikit-learn - For data preprocessing and evaluation metrics.
