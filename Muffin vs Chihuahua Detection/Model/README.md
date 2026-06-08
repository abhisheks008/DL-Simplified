# Muffin vs Chihuahua Detection using Deep Learning

## Project Overview

This project focuses on classifying images into two categories:

* Chihuahua
* Muffin

Although visually different to humans in many cases, several muffin images resemble chihuahuas and vice versa, making this an interesting computer vision classification problem.

The objective of this project is to compare multiple deep learning architectures and determine the best-performing model for the task.

---

# Objectives

* Perform Exploratory Data Analysis (EDA)
* Apply Image Preprocessing and Augmentation
* Train Multiple Deep Learning Models
* Evaluate Model Performance
* Compare Results Across Architectures
* Identify the Best Performing Model

---

# Exploratory Data Analysis (EDA)

EDA was performed before model development.

The following analyses were conducted:

* Class Distribution Analysis
* Sample Image Visualization
* Dataset Statistics
* Image Inspection

Generated Visualizations:

* sample_images.png
* class_distribution.png

---

# Data Preprocessing

The following preprocessing techniques were applied:

* Image Resizing (224 × 224)
* Pixel Value Normalization
* Data Augmentation

  * Rotation
  * Width Shift
  * Height Shift
  * Zoom
  * Horizontal Flip

---

# Models Implemented

## 1. Custom CNN

Architecture:

* Conv2D
* MaxPooling2D
* Conv2D
* MaxPooling2D
* Conv2D
* MaxPooling2D
* Flatten
* Dense Layer
* Dropout
* Output Layer

### Results

* Test Accuracy: 86.82%
* Test Loss: 0.2967

---

## 2. MobileNetV2 (Transfer Learning)

Transfer Learning was applied using the pretrained MobileNetV2 model.

### Results

* Test Accuracy: 99.32%
* Test Loss: 0.0197

---

## 3. ResNet50 (Transfer Learning)

Transfer Learning was applied using the pretrained ResNet50 model.

### Results

* Test Accuracy: 79.05%
* Test Loss: 0.4630

---

## 4. EfficientNetB0 (Transfer Learning)

Transfer Learning was applied using the pretrained EfficientNetB0 model.

### Results

* Test Accuracy: 45.95%
* Test Loss: 0.7061

---

# Model Evaluation

Evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Confusion Matrix Visualizations:

* cnn_confusion_matrix.png
* mobilenet_confusion_matrix.png
* resnet50_confusion_matrix.png
* efficientnet_confusion_matrix.png

---

# Model Comparison

| Model          | Test Accuracy | Test Loss |
| -------------- | ------------- | --------- |
| Custom CNN     | 86.82%        | 0.2967    |
| MobileNetV2    | 99.32%        | 0.0197    |
| ResNet50       | 79.05%        | 0.4630    |
| EfficientNetB0 | 45.95%        | 0.7061    |

Visualization:

* model_comparison.png

---

# Best Performing Model

🏆 MobileNetV2 achieved the highest performance.

### MobileNetV2 Results

* Accuracy: 99.32%
* Precision: 99%
* Recall: 99%
* F1 Score: 99%

This demonstrates the effectiveness of transfer learning for image classification tasks.

---

# Folder Structure

```text
Muffin vs Chihuahua Detection
│
├── Dataset
│   └── README.md
│
├── Images
│   ├── sample_images.png
│   ├── class_distribution.png
│   ├── cnn_confusion_matrix.png
│   ├── mobilenet_confusion_matrix.png
│   ├── resnet50_confusion_matrix.png
│   ├── efficientnet_confusion_matrix.png
│   └── model_comparison.png
│
├── Model
│   ├── muffin_vs_chihuahua.ipynb
│   └── README.md
│
└── requirements.txt
```

---

# How to Run

1. Clone the repository.
2. Install required dependencies.
3. Download the dataset from Kaggle.
4. Update dataset paths if necessary.
5. Run the notebook sequentially.
6. Train and evaluate the models.

---

# Conclusion

Four deep learning models were trained and evaluated for Muffin vs Chihuahua classification.

Among all tested architectures, MobileNetV2 produced the highest accuracy and the best overall classification performance. The results show that transfer learning significantly improves performance compared to a custom CNN for this dataset.

This project demonstrates the practical application of deep learning and transfer learning techniques in image classification tasks.
