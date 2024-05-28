# HEART DISEASE DETECTION USING DEEP NEURAL NETWORK

## Goal
This project aims to compare the performance of a convolutional neural network (CNN) implemented using TensorFlow/Keras with that of a Random Forest classifier for binary classification tasks.

## Dataset
The dataset is collected from the following link : https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data

## Setup and Installation

1. **Python Environment**: Make sure you have Python installed on your system. This project is developed using Python 3.x.
2. **Libraries**: Install the necessary libraries using pip:

    ```bash
    pip install tensorflow scikit-learn matplotlib
    ```
   
### Libraries used
1. `Numpy`
2. `Pandas`
3. `sklearn`
4. `Keras`
5. `Tensorflow`
6. `matplotlib`


## Model Implementation

## Model - 1

**Architecture Description:**
- **Input Layer**: Receives sequences of length 12 with one feature dimension.
- **Convolutional Blocks**: Four blocks, each with two convolutional layers followed by element-wise addition (residual connection). Filters increase progressively (32, 64, 128, 256), ReLU activation.
- **Global Average Pooling Layer**: GlobalAveragePooling1D layer computes average of each feature map across all spatial locations.
- **Dense Layers**: Four Dense layers (128, 90, 64, 32 neurons) with ReLU activation.
- **Output Layer**: Single neuron with sigmoid activation for binary classification.

**Training Description:**
- **Optimizer**: Stochastic Gradient Descent (SGD) with learning rate 0.001 and momentum 0.9.
- **Loss Function**: Binary Crossentropy.
- **Regularization**: No explicit regularization mentioned.
- **Normalization**: No explicit normalization mentioned.

<img width="451" alt="model1_acc" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/e4810d15-8a3e-47d0-ba9a-3072e1fb8d06">
<img width="436" alt="model1_loss" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/c249356d-78f2-4ac5-bcec-50694c86929e">


## Model - 2

**Architecture Description:**
- **Input Layer**: Receives sequences of length 12.
- **Convolutional Layers**: Multiple convolutional layers with filter sizes of 32, 64, 128, and 256 respectively, each followed by Batch Normalization and ReLU activation.
- **Global Average Pooling**: Applied after the convolutional layers to reduce spatial dimensions.
- **Dense Layers**: Several Dense layers with decreasing neuron counts (128, 90, 64, 32), each followed by ReLU activation and Dropout regularization.
- **Output Layer**: Single neuron with sigmoid activation for binary classification.

**Training Description:**
- **Optimizer**: Stochastic Gradient Descent (SGD) with learning rate of 0.001 and momentum of 0.9.
- **Loss Function**: Binary Crossentropy.
- **Regularization**: Dropout regularization is used to prevent overfitting.
- **Normalization**: Batch Normalization is applied to stabilize and accelerate training.

<img width="536" alt="model2_acc" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/2fb0c4f2-a5c7-4526-9b34-33c219d7d83b">
<img width="555" alt="model2_loss" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/6972a33a-eb0e-414e-be34-fe25340a0cee">


## Model - 3

**Architecture Description:**
- **Input Layer**: Receives sequences of length 12 with one feature dimension.
- **Convolutional Blocks**: Four blocks, each with two convolutional layers followed by element-wise addition (residual connection). Filters increase progressively (32, 64, 128, 256), ReLU activation.
- **Max Pooling Layer**: After final convolutional block, MaxPooling1D layer with pool size 2 and stride 1 reduces spatial dimensions.
- **Flatten Layer**: Reshapes output of last convolutional layer into 1D vector.
- **Global Average Pooling Layer**: GlobalAveragePooling1D layer computes average of each feature map across all spatial locations.
- **Dense Layers**: Four Dense layers (128, 90, 64, 32 neurons) with ReLU activation.
- **Output Layer**: Single neuron with sigmoid activation for binary classification.

**Training Description:**
- **Optimizer**: Stochastic Gradient Descent (SGD) with learning rate 0.001 and momentum 0.9.
- **Loss Function**: Binary Crossentropy.
- **Regularization**: Dropout used to prevent overfitting.
- **Normalization**: Batch Normalization stabilizes and accelerates training.


**Random Forest Classifier**:
    - **Description**: A Random Forest classifier with 100 estimators was trained for comparison purposes.
 
<img width="551" alt="model3_acc" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/48df4f82-8674-4c31-af22-5f0da3518ba9">
<img width="543" alt="model3_loss" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/86826676-4db3-4f1b-91d6-2f0ab1b0b7bf">


## Training and Evaluation
- **Data Splitting**: The dataset was split into training and testing sets using a 80:20 ratio.
- **Training**: The CNN model was trained for 150 epochs with a batch size of 4.
- **Evaluation Metrics**: Accuracy was used as the evaluation metric for both models.

## Results

To provide a conclusion based on the three models provided:

1. **Model 1**: This model consists of four convolutional blocks with residual connections, followed by global average pooling and dense layers. It employs convolutional layers to capture local patterns in the input sequences, while residual connections facilitate gradient flow and help in mitigating the vanishing gradient problem. The model architecture seems suitable for sequential data processing tasks, especially with its residual connections and global pooling layer.

2. **Model 2**: This model also utilizes convolutional layers but without residual connections. It follows a similar architecture to Model 1 but lacks the residual connections. This may result in slower convergence during training and may require more careful initialization or regularization to prevent vanishing gradients.

3. **Model 3**: Unlike the first two models, Model 3 employs a simpler architecture with convolutional layers followed by pooling and dense layers. It lacks residual connections and global pooling, which may limit its ability to capture long-range dependencies in sequential data. However, it may still perform adequately for simpler tasks or datasets with less complex patterns.

<img width="680" alt="Result" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/5d2b08d7-1be7-4b87-b597-0c4b44aed4c3">


**Conclusion**:
- Model 1 appears to be the most comprehensive and robust among the three, thanks to its use of residual connections and global pooling.
- Model 2 may suffer from vanishing gradients during training due to the absence of residual connections but could still perform reasonably well with proper tuning.
- Model 3, while simpler, may struggle with capturing complex patterns in sequential data compared to the other two models.

**The choice of the best model depends on factors such as the complexity of the dataset, computational resources, and the specific requirements of the task at hand.**
