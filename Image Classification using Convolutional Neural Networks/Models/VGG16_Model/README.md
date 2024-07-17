# 📷 ️ VGG-16 Model for Image Classification

## 📝 Overview
This project implements a VGG-16 Convolutional Neural Network (CNN) for image classification using the CIFAR-10 and MNIST datasets. The notebook `VGG16_model.ipynb` contains the entire workflow from data loading and preprocessing to model training, evaluation, and visualization.

## ⚙️ Installation
To run this project, you'll need to install the required libraries. You can do this by running:

```
pip install -r requirements.txt
```

## 🚀 Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks.git
    cd Image-Classification-using-Convolutional-Neural-Networks/Models/VGG16_Model/
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebook**:
    ```bash
    jupyter notebook VGG16_model.ipynb
    ```

## 📦 Dataset

### CIFAR-10
- **Description**: The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 different classes.
- **Classes**: 🛩️ Airplane, 🚗 Automobile, 🐦 Bird, 🐱 Cat, 🦌 Deer, 🐶 Dog, 🐸 Frog, 🐴 Horse, 🚢 Ship, 🚚 Truck.

### MNIST
- **Description**: The MNIST dataset consists of 70,000 28x28 grayscale images of handwritten digits.
- **Classes**: Digits 0 through 9.

## 🏗️ Model Architecture

The VGG-16 model for CIFAR-10 has the following architecture:
```
def create_vgg16_cifar10(input_shape, num_classes):
    model = Sequential([
        Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=input_shape),
        BatchNormalization(),
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2), strides=(2, 2)),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2), strides=(2, 2)),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2), strides=(2, 2)),
        Conv2D(512, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(512, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(512, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2), strides=(2, 2)),
        Conv2D(512, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(512, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(512, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2), strides=(2, 2)),
        Flatten(),
        Dense(4096, activation='relu'),
        Dropout(0.5),
        Dense(4096, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model
```

The VGG-16 model for MNIST has the following architecture:
```
def create_vgg16_mnist(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=input_shape),
        Conv2D(32, (3, 3), activation='relu', padding='same'),
        MaxPooling2D((2, 2), strides=(2, 2)),
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        MaxPooling2D((2, 2), strides=(2, 2)),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        MaxPooling2D((2, 2), strides=(2, 2)),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(512, activation='relu'),
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
- Train the VGG-16 model on both CIFAR-10 and MNIST datasets.
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
- **Accuracy**: Achieved accuracy on the CIFAR-10 test set - `0.7196000000`
- **Precision**: Achieved precision on the CIFAR-10 test set - `0.7470900339`
- **Classification Report**: Detailed classification report for CIFAR-10.

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Airplane    | 0.62      | 0.80   | 0.70     | 1000    |
| Automobile  | 0.64      | 0.96   | 0.77     | 1000    |
| Bird        | 0.64      | 0.65   | 0.64     | 1000    |
| Cat         | 0.52      | 0.66   | 0.58     | 1000    |
| Deer        | 0.86      | 0.62   | 0.72     | 1000    |
| Dog         | 0.87      | 0.43   | 0.58     | 1000    |
| Frog        | 0.79      | 0.85   | 0.82     | 1000    |
| Horse       | 0.87      | 0.70   | 0.77     | 1000    |
| Ship        | 0.82      | 0.85   | 0.83     | 1000    |
| Truck       | 0.83      | 0.68   | 0.74     | 1000    |
| **Accuracy**|           |        | 0.72     | 10000   |
| **Macro Avg** | 0.75    | 0.72   | 0.72     | 10000   |
| **Weighted Avg** | 0.75 | 0.72   | 0.72     | 10000   |

### MNIST
- **Accuracy**: Achieved accuracy on the MNIST test set - `0.9919000000`
- **Precision**: Achieved precision on the MNIST test set - `0.9919247329`
- **Classification Report**: Detailed classification report for MNIST.

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.99      | 1.00   | 0.99     | 980     |
| 1     | 0.99      | 0.99   | 0.99     | 1135    |
| 2     | 1.00      | 1.00   | 1.00     | 1032    |
| 3     | 0.99      | 1.00   | 0.99     | 1010    |
| 4     | 1.00      | 0.99   | 0.99     | 982     |
| 5     | 0.99      | 1.00   | 0.99     | 892     |
| 6     | 0.99      | 0.99   | 0.99     | 958     |
| 7     | 1.00      | 0.99   | 0.99     | 1028    |
| 8     | 0.99      | 0.99   | 0.99     | 974     |
| 9     | 0.99      | 0.98   | 0.99     | 1009    |
| **Accuracy** |   |        | 0.99     | 10000   |
| **Macro Avg** | 0.99 | 0.99   | 0.99     | 10000   |
| **Weighted Avg** | 0.99 | 0.99 | 0.99     | 10000   |

## 📈 Visualizations

### CIFAR-10
- **Training and Validation Accuracy**: Line plot of training and validation accuracy per epoch.
- **Training and Validation Loss**: Line plot of training and validation loss per epoch.
![image](https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks/assets/119779889/2ee3f078-71bb-45fd-af86-73e60820278f)

### MNIST
- **Training and Validation Accuracy**: Line plot of training and validation accuracy per epoch.
- **Training and Validation Loss**: Line plot of training and validation loss per epoch.
![image](https://github.com/UTSAVS26/Image-Classification-using-Convolutional-Neural-Networks/assets/119779889/eac4a5cf-afca-4e57-aa4f-fe9c8ff00bc5)

## 🎉 Conclusion
This notebook demonstrates the implementation of a VGG-16 model for image classification on the CIFAR-10 and MNIST datasets. The models achieve good accuracy and precision, showcasing the effectiveness of CNNs for image classification tasks.
