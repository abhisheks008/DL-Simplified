# Persian Alphabet Classification with Hybrid CNN-LSTM Model

This repository contains the code and models for classifying Persian alphabets using a hybrid CNN-LSTM deep learning model.

## Overview

In this repo, I developed a novel deep learning approach for classifying Persian alphabet characters. We utilized a hybrid model combining Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks to effectively capture spatial and sequential patterns in the input data, respectively.

## Dataset

The dataset used in this project consists of 51,744 images of Persian alphabets and numbers. The images are organized into folders based on their corresponding labels, making it suitable for training and evaluating machine learning models for Persian alphabet classificatiaon.

You can download the dataset from [Kaggle](https://www.kaggle.com/datasets/mostafamohammadi1/persian-alphabets-and-numbers).

## Files

- `model/notebook.ipynb`: Jupyter notebook containing the Python code for training the hybrid CNN-LSTM model and evaluating its performance on the test dataset.
- `model/cnn_model.h5 | lstm_model.h5 | hybrid_model.h5` : Model files containing the weights and architecture of the trained standalone and hybrid model of CNN and LSTM architectures.

## Usage

To use the pre-trained model for inference, follow these steps:

1. Clone or download this repository to your local machine.
2. Open the Jupyter notebook `notebook.ipynb` using Jupyter Notebook or JupyterLab.
3. Follow the instructions in the notebook to load the pre-trained model and perform inference on your own data.

## Requirements

1. To run the Jupyter notebook, you need the following dependencies:

- Python 3
- Jupyter Notebook or JupyterLab
- TensorFlow 2.x
- NumPy
- Matplotlib
- Seaborn
- scikit-learn

2. You can install the required packages using pip:

```bash
pip install jupyter tensorflow numpy matplotlib seaborn scikit-learn
```

3. Download the dataset
4. Navigate to the `model/notebook.ipynb`
5. Run all the cells

## Additional Resources

Check out the Kaggle notebook for Persian Alphabet Classification using CNN and LSTM: [Kaggle Notebook](https://www.kaggle.com/code/gowrivinaykamalakars/persian-alphabet-classification-using-cnn-and-lstm)

## Contributor:
<p align="center">
  <img src="https://github.com/sgvkamalakar.png" height="200" width="200"/>
</p>
<p align="center">
  Kamalakar Satapathi
</p>

 
Connect with me on [![LinkedIn](https://img.shields.io/badge/-Kamalakar_Satapathi-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sgvkamalakar)

Explore my magical codes [![GitHub](https://img.shields.io/badge/-Sgvkamalakar-181717?style=flat-square&logo=github)](https://github.com/sgvkamalakar)

