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
- **Convolutional Neural Network (CNN)**:
    - **Architecture**: The CNN model consists of several convolutional layers followed by global average pooling and dense layers.
    - **Training**: The model was trained using stochastic gradient descent (SGD) optimizer with a learning rate of 0.001 and momentum of 0.9.
      <img width="492" alt="summary_model" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/4b0efeff-f4ff-4ca9-8cd8-e70dca1dc15d">


- **Random Forest Classifier**:
    - **Description**: A Random Forest classifier with 100 estimators was trained for comparison purposes.

## Training and Evaluation
- **Data Splitting**: The dataset was split into training and testing sets using a 80:20 ratio.
- **Training**: The CNN model was trained for 150 epochs with a batch size of 4.
- **Evaluation Metrics**: Accuracy was used as the evaluation metric for both models.

## Results
- **Performance Comparison**: The performance of the CNN model and Random Forest classifier was compared using accuracy.
- **Visualization**: Training and validation accuracy and loss curves for the CNN model were plotted.
<img width="451" alt="plotting_Accuracy" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/25e6523f-10c6-4946-88e1-ac8371994d81">
<img width="436" alt="plotting_loss" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/523d9882-42c2-4336-8962-4ef1fb9b2cfa">


## Conclusion
- **Summary**: The CNN model outperformed the Random Forest classifier in terms of accuracy.
- **Future Work**: Further analysis could include experimenting with different architectures and hyperparameters for both models.

<img width="358" alt="metrics" src="https://github.com/KamakshiOjha/DL-Simplified/assets/114620432/905c1c54-86d0-4225-a9ce-346ca278f20f">

