### Hair Type Classification Model using Deep Learning ###


## Goal
The main objective of this project is to develop a deep learning-based hair type classification system that can accurately classify hair into five categories: Kinky, Dreadlocks, Straight, Curly, and Wavy. This project aims to enhance automated hair classification accuracy using an ensemble of three powerful deep learning models.

## Overview
Hair type classification is a crucial aspect in various domains, including cosmetics, fashion, and dermatology. The goal of this project is to build an **AI-powered hair type classification system** that can categorize hair into five types:  
- **Kinky**
- **Dreadlocks**
- **Straight**
- **Curly**
- **Wavy**  
## Objectives
- Develop a **deep learning-based model** for hair type classification.  
- Train and evaluate multiple models, then combine them using an **ensemble approach**.  
- Achieve **higher accuracy** through a hybrid model combining **ResNet50, VGG16, and ConvNeXt-Tiny**.  

## Dataset
Here is the dataset link : [Link to the dataset](https://www.kaggle.com/datasets/kavyasreeb/hair-type-dataset)
## Data Distrubution
| Hair Type  | Training Images | Testing Images |
|------------|----------------|---------------|
| Kinky      | 173            | 44            |
| Dreadlocks | 354            | 89            |
| Straight   | 390            | 98            |
| Curly      | 411            | 103           |
| Wavy       | 264            | 66            |

---
## Methodology
- **Image Resizing**: All images resized to **224x224** for model compatibility.  
- **Normalization**: Applied using **ImageNet statistics**.  
- **Data Augmentation**: Used **Albumentations** for better generalization.  

## Model Selection & Training
I implemented and trained following three models:
1. **ResNet50** – A deep residual network for effective feature extraction.  
2. **VGG16** – A deep CNN with uniform kernel sizes.  
3. **ConvNeXt-Tiny** – A modern CNN inspired by Vision Transformers. 
### Ensemble Learning Approach  
The **final model** is an **ensemble of all three models**, using a **weighted averaging technique** to achieve **higher accuracy**.  
## Results
### Classification Report for **Hair-ResNet50**:

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Straight    | 0.92      | 0.92   | 0.92     | 195     |
| Wavy        | 0.82      | 0.81   | 0.82     | 126     |
| Curly       | 0.86      | 0.92   | 0.89     | 186     |
| Dreadlocks  | 0.97      | 0.99   | 0.98     | 193     |
| Kinky       | 0.91      | 0.77   | 0.83     | 95      |

- **Accuracy**: 0.90 (795 samples)
- **Macro Average**: Precision 0.90, Recall 0.88, F1-Score 0.89
- **Weighted Average**: Precision 0.90, Recall 0.90, F1-Score 0.90
### Classification Report for Hair-VGG16:

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Straight    | 0.88      | 0.94   | 0.91     | 195     |
| Wavy        | 0.89      | 0.83   | 0.86     | 126     |
| Curly       | 0.91      | 0.92   | 0.91     | 186     |
| Dreadlocks  | 0.98      | 0.97   | 0.98     | 193     |
| Kinky       | 0.90      | 0.85   | 0.88     | 95      |

- **Accuracy**: 0.92 (795 samples)
- **Macro Average**: Precision 0.91, Recall 0.90, F1-Score 0.91
- **Weighted Average**: Precision 0.92, Recall 0.92, F1-Score 0.92
### Classification Report for hair-convnext-tiny:

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Straight    | 0.92      | 0.96   | 0.94     | 195     |
| Wavy        | 0.87      | 0.82   | 0.84     | 126     |
| Curly       | 0.89      | 0.95   | 0.92     | 186     |
| Dreadlocks  | 0.98      | 0.98   | 0.98     | 193     |
| Kinky       | 0.94      | 0.80   | 0.86     | 95      |

- **Accuracy**: 0.92 (795 samples)
- **Macro Average**: Precision 0.92, Recall 0.90, F1-Score 0.91
- **Weighted Average**: Precision 0.92, Recall 0.92, F1-Score 0.92
### Ensemble Model Classification Report:

| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Straight    | 0.92      | 0.94   | 0.93     | 195     |
| Wavy        | 0.88      | 0.85   | 0.86     | 126     |
| Curly       | 0.91      | 0.93   | 0.92     | 186     |
| Dreadlocks  | 1.00      | 1.00   | 1.00     | 193     |
| Kinky       | 0.90      | 0.86   | 0.88     | 95      |

- **Accuracy**: 0.93 (795 samples)
- **Macro Average**: Precision 0.92, Recall 0.92, F1-Score 0.92
- **Weighted Average**: Precision 0.93, Recall 0.93, F1-Score 0.93
## Key Observations  
- **Ensemble Model** provided the best results (**93.7% accuracy**).  
- **ConvNeXt-Tiny** performed better than ResNet50 and VGG16.  
- **Data Augmentation** significantly improved model robustness. 
## Required Libraries
- fastai  
- fastai.vision.all  
- fastai.callback.tracker  
- albumentations -- version 1.3.0 
- sklearn.metrics  
- cv2 (OpenCV)  
- pathlib 




