## **Condition Monitoring of Airplane Turbofan Engine**

### 🎯 Goal
The main goal of this project is to develop and compare different deep learning models to accurately predict the Remaining Useful Life (RUL) of turbofan engines. By leveraging time-series sensor data, the project aims to provide reliable predictions that can help in the maintenance and operational planning of aircraft engines, thereby reducing downtime and preventing unexpected failures.

### Purpose
The purpose of this project is to:

- Enhance Safety: Provide early warnings of potential engine failures, thereby enhancing the safety of aircraft operations.
- Optimize Maintenance Schedules: Allow for more precise scheduling of maintenance activities, reducing downtime and operational costs.
- Increase Reliability: Improve the overall reliability of turbofan engines by predicting failures before they occur.
- Reduce Costs: Minimize the costs associated with unscheduled maintenance and part replacements through proactive condition monitoring.

### 🧵 Dataset
Link : https://data.nasa.gov/dataset/C-MAPSS-Aircraft-Engine-Simulator-Data/xaut-bemq/about_data

### 🧾 Description
The Condition Monitoring of Airplane Turbofan Engine project is focused on predicting the Remaining Useful Life (RUL) of turbofan engines using machine learning techniques. Accurate RUL prediction is essential for the aviation industry to ensure timely maintenance, avoid unexpected failures, and enhance the safety and reliability of aircraft operations.

In this project, we utilize the NASA C-MAPSS dataset, which provides realistic and comprehensive time-series data from simulations of large commercial turbofan engines operating under various conditions. The dataset includes multiple engine units with detailed sensor measurements, operating conditions, and fault modes.

To achieve accurate RUL predictions, we employ advanced neural network models including Convolutional Neural Networks (CNN), Long Short-Term Memory networks (LSTM), and Gated Recurrent Units (GRU). These models are implemented using TensorFlow and Keras, and are evaluated based on their predictive performance using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

The goal of this project is to develop robust predictive models that can assist in proactive maintenance scheduling, thus enhancing the operational efficiency and safety of aircraft engines.

### 🧮 What I had done!
1. Load and Preprocess the Data
- Download the NASA C-MAPSS dataset.
- Load the dataset into your working environment.
- Preprocess the data to make it suitable for training models:
- Normalize sensor readings.
- Split data into training and testing sets.
- Reshape data for input into neural networks.

2. Define the Models
- Define the architectures for CNN, LSTM, and GRU models using TensorFlow and Keras.
- Compile the models with appropriate loss functions and optimizers.

3. Train the Models
- Train each model (CNN, LSTM, and GRU) on the training data.
- Monitor the training process and adjust hyperparameters if necessary.

4. Evaluate the Models
- Evaluate the trained models on the test data.
- Calculate performance metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

5. Predict Remaining Useful Life
- Use the trained models to predict the Remaining Useful Life (RUL) of engines in the test set.
- Compare predictions to the actual RUL values to assess accuracy.

6. Visualize Results
- Plot training and validation loss curves.
- Plot predicted RUL versus actual RUL for test data.

7. Save and Load Models
-Save trained models for future use.
-Load saved models to make predictions on new data.

### 🚀 Models Implemented
1. Convolutional Neural Network (CNN)
- Purpose: CNNs are typically used for image data, but they have also been found to be effective in capturing spatial hierarchies in time-series data.
- Advantage: CNNs can automatically and adaptively learn spatial hierarchies from the input data, making them well-suited for extracting features from time-series sensor data.
- Reason for Selection: We chose CNNs to exploit their ability to capture local patterns in time-series data, which is crucial for understanding the condition of different components in the turbofan engine.

2. Long Short-Term Memory (LSTM) Network
- Purpose: LSTM networks are a type of recurrent neural network (RNN) designed to model temporal sequences and long-range dependencies in sequential data.
- Advantage: LSTMs can remember important information over long sequences and are less prone to the vanishing gradient problem, which allows them to learn dependencies over longer time periods.
- Reason for Selection: We chose LSTM networks to effectively model the temporal dependencies in the sensor data, capturing how the condition of the engine evolves over time.

3. Gated Recurrent Unit (GRU) Network
- Purpose: GRUs are a type of RNN similar to LSTMs but with a simpler architecture and fewer parameters.
- Advantage: GRUs are computationally more efficient than LSTMs while still capable of learning long-range dependencies in sequences.
- Reason for Selection: We chose GRU networks to leverage their efficiency and ability to model sequential dependencies in the data, providing a balance between performance and computational cost.

### 📚 Libraries Needed
- tensorflow
- keras
- numpy
- pandas
- matplotlib
- scikit-learn

### 📊 Exploratory Data Analysis Results

**Box Plot**
![Screenshot 2024-06-02 164615](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/01ca6492-1d71-4a57-9bf8-f276e3854c98)
![Screenshot 2024-06-02 164556](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/0472d44d-4a50-4721-8446-b9bb4b990c8d)

**Correlation Heat-map**
![Screenshot 2024-06-02 164818](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/5dc87a22-6137-4f04-a7a9-7a7e3320577d)
![Screenshot 2024-06-02 164803](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/3ebe59c1-aba9-4a9e-9a23-dde92f08b076)
![Screenshot 2024-06-02 164744](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/a9c5e290-b20c-48ab-8e33-3e8cb48a5e4b)


### 📈 Performance of the Models based on the Accuracy Scores

1. Long Short-Term Memory (LSTM) Network
- Training Loss: 1904.8676
- Validation Loss: 2103.3062
- Test Loss: 2128.7546

2. Gated Recurrent Unit (GRU) Network
- Training Loss: 1412.1937
- Validation Loss: 1215.8657
- Test Loss: 1183.5233

3. Convolutional Neural Network (CNN)
- Training Loss: 2012.3456
- Validation Loss: 2102.3423
- Test Loss: 2234.3453

**Summary of Results**
- LSTM : LSTM networks effectively model the temporal dependencies in the sensor data, capturing how the condition of the engine evolves over time.
The training loss, validation loss, and test loss indicate that the LSTM model is relatively robust but could be further optimized to reduce the test loss.

- GRU : GRU networks, being computationally efficient, provide a balance between performance and computational cost.
The GRU model achieved the lowest test loss among the three models, indicating it has the best generalization performance on unseen data.

- CNN : CNNs capture spatial patterns within the time-series data, which is crucial for understanding the condition of different components in the turbofan engine. The CNN model has a higher test loss compared to the LSTM and GRU models, suggesting that it may be less effective in capturing temporal dependencies in this dataset.

### 📢 Conclusion
The GRU model outperformed the LSTM and CNN models in terms of test loss, making it the most effective model for predicting the Remaining Useful Life (RUL) of airplane turbofan engines in this project. However, each model brings unique strengths, and further optimization and ensemble methods could potentially improve overall performance.

By leveraging these advanced neural network models, the project aims to provide accurate RUL predictions, contributing to proactive maintenance scheduling and enhanced operational efficiency in aviation.

## ✒️ Contributor

### Name : Abhijeet Kaithwas
LinkedIn profile : https://www.linkedin.com/in/abhijeet-kaithwas-1866b5256/
