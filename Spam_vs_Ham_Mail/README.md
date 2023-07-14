# Spam vs Ham Mail Classifier

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

This repository contains a spam vs ham mail classifier app built with Streamlit GUI. The classifier is based on a pretrained XGBoost (XGB) model, which achieved the highest accuracy among the models evaluated. It can help you identify whether an email is spam or ham (non-spam).

## Table of Contents

- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Background

Spam emails continue to be a nuisance, cluttering our inboxes and wasting our time. This project addresses the problem by providing a spam vs ham mail classifier app that uses a pretrained XGBoost model. The app allows users to predict whether an email is spam or ham, providing a convenient way to filter unwanted emails effectively.

## Installation

To use the spam vs ham mail classifier app, follow these steps:

1. Clone this repository to your local machine:

```shell
git clone https://github.com/pooranjoyb/DL-Simplified.git
```
2. Change into the project's directory:
```shell
cd Spam_vs_Ham_Mail
```
3. Install the required dependencies:

```shell
pip install -r requirements.txt
```
## Usage
To use the spam vs ham mail classifier app, follow these steps:

1. Run the Streamlit app:

```shell
python -m src
```
2. The app will open in your default web browser. You can then interact with the app's interface.
3. Enter the email content in the provided text area.
4. Click the "Predict" button to classify the email as spam or ham.

## Dataset
The dataset used for training the pretrained XGBoost model is not included in this repository. However, you can use your own labeled dataset or obtain a suitable dataset from public sources. Ensure that your dataset has a balanced distribution of spam and ham emails for optimal performance.
The dataset used here is [Kaggle Dataset](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv)

## Model Training
The pretrained XGBoost model was trained in a Jupyter Notebook, which is provided in the repository. You can refer to the notebook for details on the model training process, including the data preprocessing steps and model configuration.

## Contributing
Contributions to the spam vs ham mail classifier app are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request. Let's work together to make the app even better.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as you see fit.
