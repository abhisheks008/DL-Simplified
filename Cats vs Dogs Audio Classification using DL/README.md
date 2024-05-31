# 🐱🐶 Cats vs Dogs Audio Classification using DL

## Introduction
This project focuses on classifying audio clips to determine whether the sound is from a cat 🐱 or a dog 🐶 using Deep Learning techniques. By leveraging advanced neural network architectures, we aim to achieve high accuracy in distinguishing between cat and dog sounds.

## Table of Contents
1. [🎯 Goal](#goal)
2. [📊 Dataset](#dataset)
3. [📜 Description](#description)
4. [🛠️ Project Workflow](#project-workflow)
5. [🧠 Models Used](#models-used)
6. [📦 Libraries Needed](#libraries-needed)
7. [📏 Evaluation Metrics](#evaluation-metrics)
8. [🏆 Results](#results)
9. [🔍 Conclusion](#conclusion)
10. [🔮 Future Work](#future-work)
11. [🙏 Acknowledgements](#acknowledgements)

## 🎯 Goal
The primary objective is to classify sounds as either a cat's meow 🐱 or a dog's bark 🐶 using deep learning models.

## 📊 Dataset
The dataset used for this project is available on Kaggle: [Audio Cats and Dogs Dataset](https://www.kaggle.com/datasets/mmoreaux/audio-cats-and-dogs).

## 📜 Description
This project identifies cat and dog sounds from audio files, training on a dataset containing sounds of both animals. We preprocess these audio files to generate spectrograms, which are then used for model training and evaluation.

## 🛠️ Project Workflow
1. **Data Collection**: Gathered audio data from the provided dataset link.
2. **Data Preprocessing**: Preprocessed audio files to generate spectrograms.
3. **Model Selection**: Utilized CNN, VGG16, ResNet50, and MobileNetV2 architectures.
4. **Comparative Analysis**: Compared the accuracy and loss of each model.

## 🧠 Models Used
1. **Convolutional Neural Network (CNN)** 
2. **VGG16** 
3. **ResNet50** 
4. **MobileNetV2** 

## 📦 Libraries Needed
To run this project, you will need the following libraries:

- `numpy==1.24.3` 🐍
- `pandas==1.5.0` 🐼
- `matplotlib==3.6.0` 📊
- `tensorflow==2.6.0` 🧠

## 📏 Evaluation Metrics
The models are assessed using the following metrics:
- **Accuracy** 📊
- **Loss** 📉

## 🏆 Results
Performance of models on the validation dataset:

| Model       | Accuracy | Loss   |
|-------------|----------|--------|
| **CNN**         | 0.94     | 0.203  |
| **VGG16**       | 0.866    | 0.424  |
| **ResNet50**    | 0.94     | 0.278  |
| **MobileNetV2** | 0.91     | 5.678  |

## 🔍 Conclusion
From the results, we can draw the following conclusions:
1. **CNN**: Achieved the highest accuracy (0.94) with a low loss (0.203), indicating strong performance in distinguishing between cat and dog sounds.
2. **VGG16**: Reached an accuracy of 0.866 with a higher loss (0.424). Although effective, it performed slightly worse than the CNN.
3. **ResNet50**: Also attained a high accuracy (0.94) but with a slightly higher loss (0.278) than the CNN, showing effective classification capabilities.
4. **MobileNetV2**: Achieved an accuracy of 0.91 but had a significantly higher loss (5.678), suggesting challenges in learning the audio patterns.

## 🔮 Future Work
- **Data Augmentation**: Implement data augmentation techniques to increase the diversity of the training set.
- **Hyperparameter Tuning**: Perform extensive hyperparameter tuning to improve model performance.
- **Additional Models**: Explore other deep learning architectures and ensemble methods to enhance accuracy and robustness.

## 🙏 Acknowledgements
- The dataset used in this project was provided by [Kaggle](https://www.kaggle.com).
- Special thanks to the developers of the deep learning frameworks and libraries utilized in this project.

Feel free to reach out with any questions or contributions! 😊
