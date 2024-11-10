### 📊 Dataset
The model uses a synthetic time series dataset generated specifically for anomaly detection. Key details include:

- **Structure**: The dataset consists of a single-variable time series with 1,000 timesteps.
- **Data Scaling**: The values are scaled between 0 and 1 using MinMaxScaler to standardize the data range, which helps the model learn more effectively.
- **Time Steps**: A window of 10 time steps is used to create sequences for training the LSTM model, making it capable of learning temporal dependencies.
- **Anomalies**: Certain points in the series represent anomalies, which the model is trained to identify.

This synthetic dataset enables the model to learn from a controlled data source with a known pattern of anomalies, making it suitable for evaluating the accuracy of different anomaly detection algorithms.
