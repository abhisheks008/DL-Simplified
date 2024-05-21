## **Weather Prediction**

### 🎯 **Goal**
`The main goal of this project is to determine if a set of weather measurements results in suitable conditions for an outdoor BBQ in a specific European city.`

### 🧵 **Dataset**
The datasets used in this project are:

1. **Weather Prediction Dataset**: [weather_prediction_dataset.csv](https://content/weather_prediction_dataset.csv)
2. **BBQ Labels Dataset**: [weather_prediction_bbq_labels.csv](https://content/weather_prediction_bbq_labels.csv)

### 🧾 **Description**

`The project focuses on predicting whether weather conditions are suitable for an outdoor BBQ in various European cities. It involves analyzing historical weather data, including parameters such as wind speed, cloud cover, humidity, pressure, precipitation, sunshine, and temperatures. The goal is to build and compare machine learning models (ANN, CNN, and ConvLSTM) to accurately classify BBQ-friendly weather conditions. The project encompasses data preprocessing, exploratory data analysis, model development, training, evaluation, and visualization of results.`
### 🧮 **What I had done!**

1. **Data Collection**:
   - Import necessary libraries for data manipulation and visualization, such as NumPy, Pandas, Seaborn, and Matplotlib.
   - Load the weather dataset and BBQ labels dataset using Pandas `read_csv()` function.

2. **Data Exploration**:
   - Review the first few rows of both datasets to understand their structure and contents.
   - Check the column names and sizes of the datasets to ensure proper loading.

3. **City Selection**:
   - Prompt the user to input the name of the city they are interested in for BBQ weather prediction.
   - Generate column names dynamically based on the user input to extract relevant weather data for the chosen city.
   - Handle cases where no data is available for the specified city.

4. **Data Visualization**:
   - Visualize the relationship between different weather variables and BBQ suitability using various plots:
     - Pairplot to visualize pairwise relationships between variables.
     - Correlation heatmap to show the correlation between variables.
     - KDE plots to visualize the distribution of weather variables for BBQ and non-BBQ conditions.
     - Countplot to display the occurrence count of BBQ weather conditions.

5. **Data Preparation**:
   - Map the boolean BBQ labels (True/False) to binary values (1/0) for model training.

6. **Model Building**:
   - Utilize three different machine learning models:
     - Artificial Neural Network (ANN).
     - Convolutional Neural Network (CNN).
     - Convolutional Long Short-Term Memory (ConvLSTM).
   - Each model is set up with appropriate layers, activations, and regularization techniques (dropout).
   - Compile the models with appropriate loss functions, optimizers, and evaluation metrics.

7. **Model Training**:
   - Split the data into training and testing sets using `train_test_split()` from scikit-learn.
   - Train each model using the training data.
   - Implement early stopping during training to prevent overfitting and restore the best weights.

8. **Model Evaluation**:
   - Evaluate the trained models using the testing data to calculate accuracy and other relevant metrics.
   - Generate classification reports and confusion matrices to assess model performance.

9. **Model Comparison**:
   - Compare the performance of the ANN, CNN, and ConvLSTM models based on accuracy.
   - Visualize the comparison using a bar plot to showcase the accuracy of each method.

10. **Save Models**:
    - Save the trained models for future use or deployment.

By following these steps, the project efficiently predicts BBQ-friendly weather conditions using deep learning models and provides insights into the performance of different approaches.

![work_flow](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/workflow_graph.png)

### 🚀 **Models Implemented**

## Artificial Neural Network (ANN):
1. **Model Setup**:
   - The ANN consists of an input layer, two hidden layers, and an output layer.
   - The input layer has neurons equal to the number of features in the dataset.
   - Two hidden layers with ReLU activation functions are included to introduce non-linearity.
   - Dropout layers with a dropout rate of 0.2 are added after each hidden layer to prevent overfitting.
   - The output layer has a single neuron with a sigmoid activation function for binary classification.

2. **Compilation**:
   - The model is compiled with binary cross-entropy loss function, Adam optimizer, and accuracy metric.

3. **Training**:
   - The model is trained over 100 epochs with early stopping implemented to prevent overfitting.
   - Early stopping monitors the validation loss and stops training if it does not improve for 5 consecutive epochs, restoring the best weights.

4. **Evaluation**:
   - After training, the model is evaluated using the test data to calculate the test loss and accuracy.

 `ANN is suitable for this project because it can handle complex relationships between weather variables and BBQ suitability. It's capable of learning from large datasets and can capture non-linear patterns effectively.`

## Convolutional Neural Network (CNN):
1. **Model Setup**:
   - The CNN includes a reshaping layer, a 1D convolutional layer with 10 filters and a kernel size of 2, followed by a flattening layer.
   - A dropout layer with a dropout rate of 0.2 is added after flattening to prevent overfitting.
   - Finally, an output dense layer with a sigmoid activation function is included for binary classification.

2. **Compilation**:
   - Similar to ANN, the CNN is compiled with binary cross-entropy loss function, Adam optimizer, and accuracy metric.

3. **Training**:
   - The model is trained over a specified number of epochs with the given training data.

4. **Evaluation**:
   - After training, the model's performance is evaluated using test data to calculate the test loss and accuracy.

`CNN is suitable for this project because it can extract spatial and temporal patterns from weather data, similar to how it extracts features from images. By leveraging 1D convolutional layers, CNNs can capture sequential dependencies in time-series data, making them suitable for weather prediction tasks.`
## Convolutional Long Short-Term Memory (ConvLSTM):
1. **Model Setup**:
   - The model includes a ConvLSTM2D layer with 64 filters, a kernel size of (1, 1), and ReLU activation function.
   - A flattening layer is added after ConvLSTM for reshaping the output.
   - Dropout layer with a dropout rate of 0.5 is included to prevent overfitting.
   - An output dense layer with a sigmoid activation function is added for binary classification.

2. **Compilation**:
   - Similar to ANN and CNN, the model is compiled with binary cross-entropy loss function, Adam optimizer, and accuracy metric.

3. **Training**:
   - The model is trained with early stopping callback to prevent overfitting.

4. **Evaluation**:
   - After training, the model's performance is evaluated using test data, and the accuracy is calculated.

`ConvLSTM is suitable for this project because it combines the strengths of CNNs and LSTMs. It can effectively capture spatial patterns in weather data while retaining the ability to model long-term dependencies over time. This makes it well-suited for predicting BBQ weather conditions based on sequential weather measurements.`

### 📚 **Libraries Needed**

- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation and analysis.
- **Seaborn**: For statistical data visualization.
- **Matplotlib**: For creating plots and visualizations.
- **TensorFlow**: For building and training neural network models.
- **Scikit-learn**: For machine learning tasks such as splitting data, evaluating models, and generating classification reports.
- **Keras**: A high-level neural networks API, running on top of TensorFlow, used for building and training deep learning models.


### 📊 **Exploratory Data Analysis Results**

![Distribution plot](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_distribution_plot.jpeg)

![BBQ count](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_bbq_count.jpeg)

![HeatMap](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_heatmap.jpeg)

![PairPlot](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_pairplot.jpeg)

![Pie Chart](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_piechart.jpeg)

![subplot](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_sybplot.jpeg)


### 📈 **Performance of the Models based on the Accuracy Scores**

![Train_val accuracy ann](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/train_val_accuracy_ann.jpeg)

![Train_val loss ann](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/train_val_loss_ann.jpeg)

![conf matrix ann](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_ann_conf.jpeg)

![Train_val accuracy cnn](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/train_val_accuracy_cnn.jpeg)

![Train_val loss cnn](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/train_val_loss_cnn.jpeg)

![conf matrix cnn](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_cnn_conf.jpeg)

![Train_val accuracy lstm](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/train_val_accuracy_lstm.jpeg)

![Train_val loss lstm](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/train_val_loss_lstm.jpeg)

![conf matrix lstm](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_lstm_conf.jpeg)



### 📢 **Conclusion**

The conclusion of this project is that we've successfully built and evaluated three different models for predicting BBQ weather conditions based on various weather variables.

`Additionally, the accuracy of the model varies depending on the city selected. While this notebook uses Heathrow as an example, users can input different cities, leading to potentially different accuracy results.`

- We utilized an Artificial Neural Network (ANN), a Convolutional Neural Network (CNN), and a Convolutional LSTM model to predict whether weather conditions are suitable for outdoor BBQ activities.
- Each model was trained and evaluated using appropriate techniques such as dropout regularization and early stopping to prevent overfitting.
- The models were compared based on their accuracy scores to determine the best-fitted model for the specific project.

Here are the accuracy scores obtained for each model:
- ANN Accuracy: [93%]
- CNN Accuracy: [94%]
- ConvLSTM Accuracy: [96%]

Based on these accuracy scores, we can determine the best-fitted model among all the developed models for this particular project. We'll choose the model with the highest accuracy score as it indicates better performance in predicting BBQ weather conditions.
![accuracy](https://github.com/manishh12/DL-Simplified/blob/main/Weather_prediction/Images/Heathrow_accuracy_comp.jpeg)

### ✒️ **Your Signature**

`Manish Kumar Gupta`
