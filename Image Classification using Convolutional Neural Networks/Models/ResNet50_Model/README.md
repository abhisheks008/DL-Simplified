# 🔍 ResNet50 Model for Image Classification

## 📝 Overview
This project implements a ResNet50 Convolutional Neural Network (CNN) for image classification using the CIFAR-10 and MNIST datasets. The notebook `ResNet50_model.ipynb` contains the entire workflow from data loading and preprocessing to model training, evaluation, and visualization.

## ⚙️ Installation
To run this project, you'll need to install the required libraries. You can do this by running:

```
pip install -r requirements.txt
```

## 🚀 Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks.git
    cd Image-Classification-using-Convolutional-Neural-Networks/Models/ResNet50_Model/
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebook**:
    ```bash
    jupyter notebook ResNet50_model.ipynb
    ```

## 📦 Dataset

### CIFAR-10
- **Description**: The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 different classes.
- **Classes**: 🛩️ Airplane, 🚗 Automobile, 🐦 Bird, 🐱 Cat, 🦌 Deer, 🐶 Dog, 🐸 Frog, 🐴 Horse, 🚢 Ship, 🚚 Truck.

### MNIST
- **Description**: The MNIST dataset consists of 70,000 28x28 grayscale images of handwritten digits.
- **Classes**: Digits 0 through 9.

## 🏗️ Model Architecture

The ResNet50 model for CIFAR-10 has the following architecture:
```
def create_resnet50_cifar10(input_shape, num_classes):
    base_model = tf.keras.applications.ResNet50(weights=None, include_top=False, input_shape=input_shape)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
```

The ResNet50 model for MNIST has the following architecture:
```
def create_resnet50_mnist(input_shape, num_classes):
    base_model = tf.keras.applications.ResNet50(weights=None, include_top=False, input_shape=input_shape)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
```

## 📝 Steps

### 1. Data Loading and Preprocessing
- Load the CIFAR-10 and MNIST datasets.
- Normalize the pixel values to the range [0, 1].
- Convert class labels to categorical format.

### 2. Model Training
- Train the ResNet50 model on both CIFAR-10 and MNIST datasets.
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
- **Accuracy**: Achieved accuracy on the CIFAR-10 test set - `0.3908000000`
- **Precision**: Achieved precision on the CIFAR-10 test set - `0.4610951396`
- **Classification Report**: Detailed classification report for CIFAR-10.

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Airplane    | 0.55      | 0.49   | 0.52     | 1000    |
| Automobile  | 0.52      | 0.70   | 0.59     | 1000    |
| Bird        | 0.32      | 0.23   | 0.26     | 1000    |
| Cat         | 0.27      | 0.10   | 0.14     | 1000    |
| Deer        | 0.30      | 0.27   | 0.28     | 1000    |
| Dog         | 0.37      | 0.20   | 0.26     | 1000    |
| Frog        | 0.24      | 0.92   | 0.39     | 1000    |
| Horse       | 0.73      | 0.23   | 0.35     | 1000    |
| Ship        | 0.68      | 0.50   | 0.58     | 1000    |
| Truck       | 0.64      | 0.29   | 0.40     | 1000    |
| **Accuracy**|           |        | 0.39     | 10000   |
| **Macro Avg** | 0.46    | 0.39   | 0.38     | 10000   |
| **Weighted Avg** | 0.46 | 0.39 | 0.38     | 10000   |

### MNIST
- **Accuracy**: Achieved accuracy on the MNIST test set - `0.9789000000`
- **Precision**: Achieved precision on the MNIST test set - `0.9792632805`
- **Classification Report**: Detailed classification report for MNIST.

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.98      | 0.99   | 0.99     | 980     |
| 1     | 0.99      | 0.99   | 0.99     | 1135    |
| 2     | 0.97      | 0.99   | 0.98     | 1032    |
| 3     | 0.95      | 1.00   | 0.97     | 1010    |
| 4     | 0.98      | 0.98   | 0.98     | 982     |
| 5     | 0.99      | 0.96   | 0.98     | 892     |
| 6     | 1.00      | 0.93   | 0.97     | 958     |
| 7     | 0.97      | 1.00   | 0.98     | 1028    |
| 8     | 0.97      | 0.98   | 0.98     | 974     |
| 9     | 0.98      | 0.96   | 0.97     | 1009    |
| **Accuracy** |       |        | 0.98     | 10000   |
| **Macro Avg** | 0.98 | 0.98   | 0.98     | 10000   |
| **Weighted Avg** | 0.98 | 0.98 | 0.98     | 10000   |

## 📈 Visualizations

### CIFAR-10
- **Training and Validation Accuracy**: Line plot of training and validation accuracy per epoch.
- **Training and Validation Loss**: Line plot of training and validation loss per epoch.

### MNIST
- **Training and Validation Accuracy**: Line plot of training and validation accuracy per epoch.
- **Training and Validation Loss**: Line plot of training and validation loss per epoch.

## 🎉 Conclusion
This notebook demonstrates the implementation of a ResNet50 model for image classification on the CIFAR-10 and MNIST datasets. The models achieve good accuracy and precision, showcasing the effectiveness of deep learning architectures like ResNet50 for image classification tasks.