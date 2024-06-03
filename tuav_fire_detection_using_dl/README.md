# TUAV Fire Detection


## AIM OF PROJECT 
This project aims to detect fires using images captured by Thermal Unmanned Aerial Vehicles (TUAV). It leverages a dataset from Kaggle and employs a pre-trained VGG16 model to extract features for image classification.

## Table of Contents
- [Installation](#installation)
- [Dataset](#dataset)
- [Data Preparation](#data-preparation)
- [Feature Extraction](#feature-extraction)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, you'll need to install the necessary Python packages:

```bash
pip install opendatasets
```

## Dataset
The dataset used for this project is sourced from Kaggle. Ensure you have your Kaggle API credentials ready to download the dataset.

Download the dataset using the `opendatasets` library:

## Data Preparation
After downloading the dataset, organize and split it into training and testing sets. Here's a high-level overview of the steps involved:

## Directory Setup:
Create separate directories for training and testing data.
Define a split ratio (e.g., 80% training and 20% testing).

## Data Splitting:
Loop through each member folder in the dataset.
Shuffle the images randomly and split them based on the defined ratio.
Move the split images into their respective train and test directories.

## Feature Extraction
Use the pre-trained VGG16 model to extract features from the images:

## Load VGG16 Model:

Use the pre-trained VGG16 model with weights='imagenet' and include_top=False.

## Define Feature Extraction Function:

Create a function to load an image, preprocess it, and extract features using the VGG16 model.

## Extract Features:
Loop through the images in the training and testing directories.
Use the feature extraction function to extract features and store them in arrays.

## Model Training
Initialize Lists:
Prepare lists to store features and labels for both training and testing data.

## Extract Features and Labels:
Extract features and corresponding labels from both training and testing images.

## Prepare Data:
Convert the lists of features and labels into NumPy arrays.

## Evaluation

Use evaluation metrics such as accuracy, precision, recall, and F1-score to assess the performance of your model.

Following is the attached image
![Alt Text](https://github.com/jahnvisahni31/DL-Simplified/raw/main/tuav_fire_detection_using_dl/images/model_Accuracy.png)
