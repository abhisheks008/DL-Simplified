## **Framing the Future**

### 🎯 **Goal**
The main objective of this project is to predict future frames in a sequence of Moving MNIST dataset using various deep learning models, including Artificial Neural Networks (ANN), Convolutional Neural Networks (CNN), and Convolutional LSTM (ConvLSTM). Each model's architecture and performance are analyzed to determine the most suitable approach for this task.

### 🧵 **Dataset**
The dataset used in this project is the Moving MNIST dataset, which consists of sequences of handwritten digits moving within a frame. Each sequence contains multiple frames, and the goal is to predict the subsequent frames based on the previous ones.

Dataset:

![sample](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/datset.jpeg)

### 🧾 **Description**

This project involves building multiple deep learning models to predict future frames in Moving MNIST sequences. It includes data preprocessing, model creation, training, evaluation, and prediction on unseen examples.

### 🧮 **What I had done!**

1. **Data Preprocessing**:
   - Imported necessary libraries for data manipulation, visualization, and model training.
   - Loaded the Moving MNIST dataset and performed basic exploratory data analysis.

2. **Data Visualization**:
   - Visualized the first few sequences in the dataset to understand the nature of the data.

3. **Dataset Splitting**:
   - Split the dataset into training and validation sets for model training and evaluation.

4. **Data Normalization**:
   - Normalized the pixel values of the dataset to the range [0, 1].

5. **Model Creation**:
   - Designed various deep learning model architectures, including ANN, CNN, and ConvLSTM.
   - Compiled each model with appropriate loss function and optimizer.

6. **Model Training**:
   - Trained each model using the training dataset.
   - Implemented early stopping and learning rate reduction callbacks during training.

7. **Model Evaluation**:
   - Evaluated the trained models' performance using the validation dataset.
   - Plotted training and validation loss curves to monitor the models' learning progress.

8. **Prediction**:
   - Made predictions on a few examples from the validation dataset to visualize the models' performance in predicting future frames.

### 🚀 **Models Implemented**

#### Artificial Neural Network (ANN):
- Designed an ANN model architecture with multiple dense layers.
- Compiled the model with binary cross-entropy loss and Adam optimizer.
- Trained the model on the Moving MNIST training dataset.

#### Convolutional Neural Network (CNN):
- Designed a CNN model architecture with multiple convolutional and pooling layers.
- Compiled the model with binary cross-entropy loss and Adam optimizer.
- Trained the model on the Moving MNIST training dataset.

#### Convolutional LSTM (ConvLSTM):
- Designed a ConvLSTM model architecture with multiple ConvLSTM2D layers followed by batch normalization.
- Compiled the model with binary cross-entropy loss and Adam optimizer.
- Trained the model on the Moving MNIST training dataset.

### 📚 **Libraries Needed**

- TensorFlow and Keras: For building and training deep learning models.
- NumPy and Matplotlib: For numerical operations and data visualization.
- scikit-learn: For dataset manipulation and evaluation.

### 📊 **Exploratory Data Analysis Results**

## Dataset

![Dataset](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/datset.jpeg)

This image represents the dataset used in the project.


## Average Intensity Over Time

![Average Intensity Over Time](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/avg_intensity_over_time.png)

This plot illustrates the average pixel intensity over time.


## Frame Intensity Distributions

![Frame Intensity Distributions](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/frame_intensity_distributions.png)

This plot displays the intensity distributions across frames.

## Intensity Histogram

![Intensity Histogram](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/intensity_histogram.png)

This histogram illustrates the distribution of pixel intensities in the dataset.


## Mean and Standard Deviation Frames

![Mean and Standard Deviation Frames](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/mean_std_frames.png)

This image shows the mean and standard deviation frames of the dataset.

### 📈 **Performance of the Models**

#### Artificial Neural Network (ANN):
- **ANN Loss**: Training loss decreased from 0.0021 to 0.0004 over 50 epochs.
- **ANN Accuracy**: Training accuracy stabilized around 0.0%, while validation accuracy also remained at 0.0%.

#### Convolutional Neural Network (CNN):
- **CNN Loss**: Training loss decreased from 0.0019 to 0.0002 over 50 epochs.
- **CNN Accuracy**: Training accuracy reached 92.60%, while validation accuracy stabilized around 92.48%.

#### Convolutional LSTM (ConvLSTM):
- **ConvLSTM Loss**: Training loss decreased from 0.0694 to 0.0237 over 41 epochs.
- **ConvLSTM Accuracy**: Training accuracy reached 92.11%, while validation accuracy stabilized around 93.2%.

### **Model Comparison**

Based on the performance metrics, the Convolutional LSTM (ConvLSTM) model outperforms the other models in terms of both training and validation accuracy.
## Plot Ann
![Plot](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/ANN_training_validation.png)

## Plot Ann
![Plot](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/CNN_training_validation.png)

## Accuracy Plot lstm

![Accuracy Plot](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/accuracy_plot.png)

This plot showcases the training and validation accuracy over epochs.

## Loss Plot lstm

![Loss Plot](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/loss_plot.png)

This plot showcases the training and validation loss over epochs.

## Comparison

![comp](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/accuracy_comparison_bar_with_values.png)

## Result

![Result](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/Result.jpeg)

This image shows the final result or output of the project.



### 📢 **Conclusion**

In conclusion, this project successfully implemented and trained multiple deep learning models for predicting future frames in Moving MNIST sequences. The Convolutional LSTM (ConvLSTM) model demonstrated superior performance in capturing spatiotemporal dependencies and accurately predicting the next frames in the sequences.

### ✒️ **Your Signature**

[Manish Kumar Gupta]
