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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


