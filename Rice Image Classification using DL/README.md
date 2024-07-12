# Rice Image Classification using VGG, Xception, and ResNet

## Overview

This repository contains the code and resources for rice image classification using three popular convolutional neural network architectures: VGG, Xception, and ResNet. This project is part of the GirlScript Summer of Code initiative.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Models](#models)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Visualization](#visualization)
- [License](#license)

## Introduction

The goal of this project is to classify images of rice into different categories using deep learning models. We utilize VGG, Xception, and ResNet architectures to build and compare their performance on this task.

## Dataset

The dataset used for this project consists of rice images categorized into various classes. Ensure you have the dataset prepared in the following structure:

```
dataset/
|-- train/
|   |-- class1/
|   |   |-- img1.jpg
|   |   |-- img2.jpg
|   |-- class2/
|   |   |-- img1.jpg
|   |   |-- img2.jpg
|-- validation/
|   |-- class1/
|   |   |-- img1.jpg
|   |   |-- img2.jpg
|   |-- class2/
|   |   |-- img1.jpg
|   |   |-- img2.jpg
```
## Models

The project implements three models:
1. VGG
2. Xception
3. ResNet

These models are pre-trained on ImageNet and fine-tuned on the rice image dataset.

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- TensorFlow 2.x
- Keras
- NumPy
- Matplotlib
- scikit-learn

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rice-image-classification.git
cd rice-image-classification
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare your dataset as mentioned in the [Dataset](#dataset) section.
2. Train the models:

```bash
python train_vgg.py
python train_xception.py
python train_resnet.py
```

3. Evaluate the models:

```bash
python evaluate.py
```

4. Make predictions on new images:

```bash
python predict.py --image_path path_to_image
```

## Results

The performance of each model will be evaluated based on accuracy, precision, recall, and F1-score. The results will be displayed after running the evaluation script.

**EDA results:**


![EDA ](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/62f30fb3-a27f-4161-ae29-649701f1d78a)

![Sample dataset](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/44472b28-1b32-45c7-8d5c-064713f02d38)

Validation, train and test:

![Validation, train, test](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/4dd91341-1cbb-47ff-b3af-7eb3101b555b)

## VISUALIZATION:

**Performance matrices:**

CNN:

![CNN CR](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/7c5ea3bb-05d0-4af5-8acf-27b8ea60d6a2)
![CNN confusion matrix](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/22903748-d153-4c09-861b-929f136ef14a)
![CNN trainning and validation loss](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/2d96c299-0234-4c72-885e-a2ac71bc5d4b)


Xception:

![resnet cr](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/00410940-650c-4ed4-b051-3e433e65f755)
![Xception ocnfusion matrix](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/4a173c4d-01b5-4d9b-b230-51fefad84304)
![Xception trainning and validation loss](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/1d0da694-c98d-436d-a720-c460c11f9e47)

VGG16:

![Vgg16 cr](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/8070afa0-a580-4b9e-ac2a-85081b2a74a5)
![VGG16 training and validation loss](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/dd5ea0f0-086b-41d2-aa95-f055543d4070)
![VGG16 confusion matrix](https://github.com/SayantikaLaskar/DL-Simplified/assets/127471376/d1c480a7-5593-4c50-b510-e27126d90b0d)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


