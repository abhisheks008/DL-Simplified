# 🖼️ Simple CNN Model for Image Classification

## 📝 Overview
This project implements a simple Convolutional Neural Network (CNN) for image classification using the CIFAR-10 and MNIST datasets. The notebook `Simple_CNN_model.ipynb` contains the entire workflow from data loading and preprocessing to model training, evaluation, and visualization.

## ⚙️ Installation
To run this project, you'll need to install the required libraries. You can do this by running:

```
pip install -r requirements.txt
```

## 🚀 Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks.git
    cd Image-Classification-using-Convolutional-Neural-Networks/Models/Simple_CNN_Model/
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebook**:
    ```bash
    jupyter notebook Simple_CNN_model.ipynb
    ```

## 📦 Dataset

### CIFAR-10
- **Description**: The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 different classes.
- **Classes**: 🛩️ Airplane, 🚗 Automobile, 🐦 Bird, 🐱 Cat, 🦌 Deer, 🐶 Dog, 🐸 Frog, 🐴 Horse, 🚢 Ship, 🚚 Truck.

### MNIST
- **Description**: The MNIST dataset consists of 70,000 28x28 grayscale images of handwritten digits.
- **Classes**: Digits 0 through 9.

## 🏗️ Model Architecture

The simple CNN model implemented in the notebook has the following structure:

- **Conv2D**: 32 filters, (3,3) kernel size, ReLU activation
- **MaxPooling2D**: (2,2) pool size
- **Conv2D**: 64 filters, (3,3) kernel size, ReLU activation
- **MaxPooling2D**: (2,2) pool size
- **Flatten**
- **Dense**: 128 units, ReLU activation
- **Dropout**: 0.5 dropout rate
- **Dense**: 10 units, Softmax activation

## 📝 Steps

### 1. Data Loading and Preprocessing
- Load the CIFAR-10 and MNIST datasets.
- Normalize the pixel values to the range [0, 1].
- Convert class labels to categorical format.

### 2. Model Training
- Train the CNN model on both CIFAR-10 and MNIST datasets.
- Record the training and validation accuracy and loss over epochs.

### 3. Model Evaluation
- Evaluate the trained model on the test data.
- Calculate accuracy and precision.
- Generate a detailed classification report.

### 4. Visualization
- Plot training and validation accuracy and loss for each epoch.
- Display class distribution and exploratory data analysis (EDA) plots.

## 📊 Results

### CIFAR-10
- **Accuracy**: Achieved accuracy on the CIFAR-10 test set - `0.6947000000`
- **Precision**: Achieved precision on the CIFAR-10 test set - `0.6939820196`
- **Classification Report**: Detailed classification report for CIFAR-10 -

| Class      | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Airplane   | 0.71      | 0.74   | 0.73     | 1000    |
| Automobile | 0.75      | 0.88   | 0.81     | 1000    |
| Bird       | 0.58      | 0.61   | 0.59     | 1000    |
| Cat        | 0.58      | 0.41   | 0.48     | 1000    |
| Deer       | 0.66      | 0.61   | 0.63     | 1000    |
| Dog        | 0.68      | 0.55   | 0.61     | 1000    |
| Frog       | 0.64      | 0.87   | 0.74     | 1000    |
| Horse      | 0.74      | 0.77   | 0.75     | 1000    |
| Ship       | 0.77      | 0.83   | 0.80     | 1000    |
| Truck      | 0.84      | 0.69   | 0.76     | 1000    |
| Accuracy   |           |        | 0.69     | 10000   |
| Macro Avg  | 0.69      | 0.69   | 0.69     | 10000   |
| Weighted Avg | 0.69    | 0.69   | 0.69     | 10000   |

### MNIST
- **Accuracy**: Achieved accuracy on the MNIST test set - `0.9929000000`
- **Precision**: Achieved precision on the MNIST test set - `0.9929076933`
- **Classification Report**: Detailed classification report for MNIST.

| Class      | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| 0          | 1.00      | 0.99   | 1.00     | 980     |
| 1          | 1.00      | 1.00   | 1.00     | 1135    |
| 2          | 0.99      | 0.99   | 0.99     | 1032    |
| 3          | 0.99      | 1.00   | 0.99     | 1010    |
| 4          | 0.99      | 0.99   | 0.99     | 982     |
| 5          | 0.99      | 0.99   | 0.99     | 892     |
| 6          | 0.99      | 0.99   | 0.99     | 958     |
| 7          | 0.99      | 0.99   | 0.99     | 1028    |
| 8          | 0.99      | 0.99   | 0.99     | 974     |
| 9          | 0.99      | 0.99   | 0.99     | 1009    |
| Accuracy   |           |        | 0.99     | 10000   |
| Macro Avg  | 0.99      | 0.99   | 0.99     | 10000   |
| Weighted Avg | 0.99    | 0.99   | 0.99     | 10000   |

## 📈 Visualizations

### CIFAR-10
- **Training and Validation Accuracy**: Line plot of training and validation accuracy per epoch.
- **Training and Validation Loss**: Line plot of training and validation loss per epoch.
![image](https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks/assets/119779889/1ebccedd-5c50-4380-835b-1c67b4b48734)

### MNIST
- **Training and Validation Accuracy**: Line plot of training and validation accuracy per epoch.
- **Training and Validation Loss**: Line plot of training and validation loss per epoch.
![image](https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks/assets/119779889/d73edcf5-d190-4346-b120-437e5de90800)

## 🎉 Conclusion

This notebook demonstrates the implementation of a simple CNN model for image classification on the CIFAR-10 and MNIST datasets. The models achieve good accuracy and precision, showcasing the effectiveness of CNNs for image classification tasks.
