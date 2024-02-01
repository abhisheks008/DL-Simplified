# Project Summary

**PROJECT TITLE:** Facial Emotion Detection

**GOAL:** Multiclass classification of facial emotions from grayscale images.

**DATASET:** [FER-DS - Kaggle](https://www.kaggle.com/datasets/mhantor/facial-expression)

**DESCRIPTION:**  
We have 19950 images covering 4 facial emotions (angry, happy, neutral, surprised).  
The images are in grayscale and have a low resolution (48x48).  
Our aim is to use these images to train a deep learning model which can classify them accurately.

**TASKS PERFORMED:**

1. Data exploration and creation of custom validation and test sets using images sampled from the original dataset.  
These will be fixed to ensure valid comparison of different models.  
Final distribution of images: Train - 16159, Validation - 1796, Test - 1995 (Total: 19950)
2. Trained CNN model from scratch as a baseline, trying different configurations for number of layers and hidden units.  
3. Added 3 configurations for data-augmentation to the data pipeline, and evaluated their effectiveness using the same CNN architecture from the previous step.
4. Applied transfer-learning techniques: feature-extraction and fine-tuning, using 2 backbone architectures: MobileNetV2 and EfficientNetV2S.

**MODELS USED:**

1. Convolutional Neural Network
2. MobileNetV2
3. EfficientNetV2S

(Data-augmentation utilized with each of these)

**LIBRARIES USED:**

1. Tensorflow
2. Keras
3. Keras_CV
4. Numpy
5. Matplotlib
6. Scikit-learn

**VISUALIZATION:**

1. [Baseline CNN](Images/00_baseline_cnn) ([Notebook 00](Model/00_baseline_cnn.ipynb))
2. [CNN + Data augmentation](Images/01_data_augmentation_cnn) ([Notebook 01](Model/01_data_augmentation_cnn.ipynb))
3. [Transfer-learning: MobileNetV2](Images/02_transfer_learning_mobilenetv2) ([Notebook 02](Model/02_transfer_learning_mobilenetv2.ipynb))
4. [Transfer-learning: EfficientNetV2S](Images/03_transfer_learning_efficientnetv2) ([Notebook 03](Model/03_transfer_learning_efficientnetv2.ipynb))

**ACCURACIES:**

| Model configuration | Val accuracy (%) | Test accuracy (%) |
|:-----:|:-----:|:-----:|
| Baseline CNN | 71.05 | 71.23 |
| CNN + Simple data-augment | 75.45 | 74.99 |
| CNN + Complex data-augment | 67.82 | 67.92 |
| CNN + Keras-CV RandAugment | 60.47 | 60.15 |
| MobileNetV2 | 80.01 | 79.30 |
| MobileNetV2 + Simple data-augment | 82.41 | 81.35 |
| EfficientNetV2S | 83.24 | 82.31 |
| EfficientNetV2S + Simple data-augment | **84.24** | **82.86** |

**CONCLUSION:**  
We used low-resolution, grayscale images to train a deep learning model to detect four facial emotions.  
Starting with a solid baseline using a CNN, we setup a framework for comparison of different model configurations.  
Combining data-augmentation with transfer-learning techniques improved performance significantly.  
Our final model consists of:  
Preprocessing - Lanczos5 interpolation for resizing  
Data augmentation - Rotation + Horizontal flipping  
Model (transfer-learning) - EfficientNetV2S backbone for feature-extraction and fine-tuning.

**AUTHOR**:
Siddhant Tiwari  
([Github](https://www.github.com/siddhant4ds) - [Kaggle](https://www.kaggle.com/sid4ds) - [LinkedIn](https://www.linkedin.com/in/siddhant4ds/))
