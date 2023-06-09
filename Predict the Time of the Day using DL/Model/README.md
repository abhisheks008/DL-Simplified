
# PROJECT TITLE

Predict the Time of the Day using DL

## GOAL

The main goal of this project is to classify images based on their time of day (morning, afternoon, evening, or night) using deep learning algorithms. The purpose of the project is to showcase the application of various deep learning techniques for image classification tasks.

## DATASET

The dataset used in this project can be found at (https://www.kaggle.com/datasets/aymenkhouja/timeofdaydataset). The dataset consists of a collection of images categorized into four classes representing different times of day.

## DESCRIPTION

This project utilizes deep learning algorithms to classify images based on the time of day. The dataset is preprocessed and then used to train different deep learning models. The trained models are evaluated based on their accuracies and compared to identify the most effective algorithm for the given task. The project also includes visualizations of the dataset and the learning curves of the best model.

## WHAT I HAD DONE

The project follows these steps:

1. Load and preprocess the image dataset.
2. Split the dataset into training and testing sets.
3. Encode the target labels for training and testing.
4. Create multiple deep learning models using different algorithms.
5. Train and evaluate the models using cross-validation.
6. Compare the accuracies of the models and identify the best performing one.
7. Plot learning curves for the best model.
8. Display a subset of predicted images by the best model.
9. Compute and display the confusion matrix for the best model.

## MODELS USED

The following deep learning models are used in this project:

  1. Convolutional Neural Network (CNN)
2. Long-short-term memory (LSTM)
3. Gated Recurrent Unit (GRU)

These models are chosen based on their effectiveness in image classification tasks and their availability in popular deep learning libraries.

## LIBRARIES NEEDED

The project requires the following libraries:

- numpy
- Pillow
- scikit-learn
- tensorflow
- matplotlib

## VISUALIZATION



































The visualization shows a subset of predicted images by the best model, along with their predicted and true labels.

## ACCURACIES

The accuracies achieved by the different models are as follows:

- CNN Accuracy: 0.8485981225967407
- LSTM Accuracy: 0.5757009387016296
- GRU Accuracy: 0.6336448788642883


## CONCLUSION

Based on the accuracy results, the Convolutional Neural Network (CNN) model achieved the highest accuracy of 0.85. It outperformed the other models, including LSTM and GRU, in classifying images based on the time of day. Therefore, the CNN model (adam_model) can be considered the best-fitted model for this project.

**Author:** 

Saket Gudimella

GitHub: https://github.com/SaketGudimella)

LinkedIn: www.linkedin.com/in/saket-gudimella-299611240
