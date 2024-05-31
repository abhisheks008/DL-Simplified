## **Framing the Future**

### 🎯 **Goal**
The main objective of this project is to predict future frames in a sequence of Moving MNIST dataset using Convolutional LSTM (ConvLSTM) model. The ConvLSTM architecture is capable of capturing both spatial and temporal dependencies in sequential data, making it suitable for this task.

### 🧵 **Dataset**
The dataset used in this project is the Moving MNIST dataset, which consists of sequences of handwritten digits moving within a frame. Each sequence contains multiple frames, and the goal is to predict the subsequent frames based on the previous ones.

Dataset:

![sample](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/datset.jpeg)

### 🧾 **Description**

This project involves building a ConvLSTM model to predict future frames in Moving MNIST sequences. It includes data preprocessing, model creation, training, evaluation, and prediction on unseen examples.

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
   - Designed a ConvLSTM model architecture to capture spatiotemporal dependencies in the Moving MNIST sequences.
   - Compiled the model with appropriate loss function and optimizer.

6. **Model Training**:
   - Trained the ConvLSTM model using the training dataset.
   - Implemented early stopping and learning rate reduction callbacks during training.

7. **Model Evaluation**:
   - Evaluated the trained model's performance using the validation dataset.
   - Plotted training and validation loss curves to monitor the model's learning progress.

8. **Prediction**:
   - Made predictions on a few examples from the validation dataset to visualize the model's performance in predicting future frames.

### 🚀 **Model Implemented**

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

### 📈 **Performance of the Model**

- **Convolutional LSTM (ConvLSTM) Loss**: Training loss decreased from 0.0694 to 0.0237 over 41 epochs.
- **Convolutional LSTM (ConvLSTM) Accuracy**: Training accuracy reached 92.11%, while validation accuracy stabilized around 93.2%.

## Accuracy Plot

![Accuracy Plot](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/accuracy_plot.png)

## Loss Plot

![Loss Plot](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/loss_plot.png)

This plot showcases the training and validation loss  and Accuracy over epochs.

  ## Result

![Result](https://github.com/manishh12/DL-Simplified/blob/main/Framing%20the%20Future/Images/Result.jpeg)

This image shows the final result or output of the project.



### 📢 **Conclusion**

In conclusion, this project successfully implemented and trained a Convolutional LSTM (ConvLSTM) model for predicting future frames in Moving MNIST sequences. The model demonstrated good performance in capturing spatiotemporal dependencies and accurately predicting the next frames in the sequences.

### ✒️ **Your Signature**

[Manish Kumar Gupta]
