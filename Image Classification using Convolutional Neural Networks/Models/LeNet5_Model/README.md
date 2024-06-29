# 🖼️ LeNet-5 Model for Image Classification

## 📝 Overview
This project implements a LeNet-5 Convolutional Neural Network (CNN) for image classification using the CIFAR-10 and MNIST datasets. The notebook `LeNet5_model.ipynb` contains the entire workflow from data loading and preprocessing to model training, evaluation, and visualization.

## ⚙️ Installation
To run this project, you'll need to install the required libraries. You can do this by running:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks.git
    cd Image-Classification-using-Convolutional-Neural-Networks/Models/LeNet5_Model/
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebook**:
    ```bash
    jupyter notebook LeNet5_model.ipynb
    ```

## 📦 Dataset

### CIFAR-10
- **Description**: The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 different classes.
- **Classes**: 🛩️ Airplane, 🚗 Automobile, 🐦 Bird, 🐱 Cat, 🦌 Deer, 🐶 Dog, 🐸 Frog, 🐴 Horse, 🚢 Ship, 🚚 Truck.

### MNIST
- **Description**: The MNIST dataset consists of 70,000 28x28 grayscale images of handwritten digits.
- **Classes**: Digits 0 through 9.

## 🏗️ Model Architecture

The LeNet-5 model for CIFAR-10 and MNIST has the following architecture:

```python
def create_lenet5(input_shape, num_classes):
    model = tf.keras.Sequential([
        Conv2D(6, kernel_size=(5, 5), activation='relu', input_shape=input_shape),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(16, kernel_size=(5, 5), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(120, activation='relu'),
        Dense(84, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
```

## 📝 Steps

### 1. Data Loading and Preprocessing
- Load the CIFAR-10 and MNIST datasets.
- Normalize the pixel values to the range [0, 1].
- Convert class labels to categorical format.

### 2. Model Training
- Train the LeNet-5 model on both CIFAR-10 and MNIST datasets.
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
- **Accuracy**: Achieved accuracy on the CIFAR-10 test set - `0.5802000000`
- **Precision**: Achieved precision on the CIFAR-10 test set - `0.5827235484`
- **Classification Report**: Detailed classification report for CIFAR-10.

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Airplane    | 0.71      | 0.58   | 0.64     | 1000    |
| Automobile  | 0.57      | 0.83   | 0.68     | 1000    |
| Bird        | 0.51      | 0.41   | 0.45     | 1000    |
| Cat         | 0.49      | 0.25   | 0.34     | 1000    |
| Deer        | 0.65      | 0.37   | 0.48     | 1000    |
| Dog         | 0.50      | 0.51   | 0.51     | 1000    |
| Frog        | 0.55      | 0.76   | 0.64     | 1000    |
| Horse       | 0.57      | 0.73   | 0.64     | 1000    |
| Ship        | 0.72      | 0.70   | 0.71     | 1000    |
| Truck       | 0.55      | 0.65   | 0.60     | 1000    |
| **Accuracy**|           |        | 0.58     | 10000   |
| **Macro Avg** | 0.58    | 0.58   | 0.57     | 10000   |
| **Weighted Avg** | 0.58 | 0.58   | 0.57     | 10000   |

### MNIST
- **Accuracy**: Achieved accuracy on the MNIST test set - `0.9862000000`
- **Precision**: Achieved precision on the MNIST test set - `0.9862803962`
- **Classification Report**: Detailed classification report for MNIST.

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.99      | 0.99   | 0.99     | 980     |
| 1     | 0.99      | 1.00   | 0.99     | 1135    |
| 2     | 0.99      | 0.99   | 0.99     | 1032    |
| 3     | 0.97      | 0.99   | 0.98     | 1010    |
| 4     | 0.99      | 0.99   | 0.99     | 982     |
| 5     | 0.97      | 0.99   | 0.98     | 892     |
| 6     | 0.99      | 0.99   | 0.99     | 958     |
| 7     | 0.99      | 0.98   | 0.98     | 1028    |
| 8     | 1.00      | 0.97   | 0.98     | 974     |
| 9     | 0.99      | 0.97   | 0.98     | 1009    |
| **Accuracy** |       |        | 0.99     | 10000   |
| **Macro Avg** | 0.99    | 0.99   | 0.99     | 10000   |
| **Weighted Avg** | 0.99 | 0.99   | 0.99     | 10000   |

## 📈 Visualizations

### CIFAR-10
- **Training and Validation Accuracy**: Line plot of training and validation accuracy per epoch.
- **Training and Validation Loss**: Line plot of training and validation loss per epoch.
- ![image](https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks/assets/119779889/0850e3db-cfe2-43ea-9fa2-fbdee733e612)

### MNIST
- **Training and Validation Accuracy**: Line plot of training and validation accuracy per epoch.
- **Training and Validation Loss**: Line plot of training and validation loss per epoch.
![image](https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks/assets/119779889/cb3c8a92-f909-4cdc-8209-280dca76a7de)

## 🎉 Conclusion
This notebook demonstrates the implementation of a LeNet-5 model for image classification on the CIFAR-10 and MNIST datasets. The models achieve high accuracy and precision, indicating the effectiveness of LeNet-5 for image classification tasks.
