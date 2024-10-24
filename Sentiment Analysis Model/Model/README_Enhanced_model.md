# Sentiment Analysis with BERT/RoBERTa

This project implements a sentiment analysis model using pre-trained BERT/RoBERTa models from the Hugging Face `transformers` library. It classifies textual data into positive or negative sentiments.

## Overview

Sentiment analysis is a technique used to determine the sentiment expressed in a given piece of text. This project uses `BERT` and `RoBERTa`, two powerful models for natural language understanding, to achieve this. The models are fine-tuned on a custom dataset for binary sentiment classification.

## Dataset

The dataset consists of three CSV files:
- `Train.csv`: Training data with two columns, `text` and `label`
- `Test.csv`: Testing data with two columns, `text` and `label`
- `Valid.csv`: Validation data with two columns, `text` and `label`

The `label` column should contain binary values (0 or 1), representing the sentiment of each text sample.

## Prerequisites

- Python 3.8+
- PyTorch
- Transformers
- Pandas
- scikit-learn

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/sentiment-analysis-bert-roberta.git
    cd sentiment-analysis-bert-roberta
    ```

2. Install the required packages:
    ```bash
    pip install transformers torch pandas scikit-learn
    ```

3. Ensure that your dataset is placed in a `Dataset` directory:
    ```
    ├── Dataset
    │   ├── Train.csv
    │   ├── Test.csv
    │   └── Valid.csv
    ```

## Usage

1. Load and preprocess the dataset:
   The code reads the training, testing, and validation datasets, and tokenizes the text data using the BERT tokenizer.

2. Choose a pre-trained model:
   Set `model_name` to either `bert-base-uncased` for BERT or `roberta-base` for RoBERTa.

3. Prepare data for training and validation:
   The texts are tokenized and converted to tensors, which are then used to create training, validation, and test datasets.

4. Train the model:
   The model is fine-tuned using the `Trainer` API from the Hugging Face `transformers` library.

5. Evaluate the model:
   After training, the model's performance is evaluated on the validation and test sets using metrics like accuracy, F1 score, precision, and recall.

## Code Structure

The code structure is as follows:

```python
# Import necessary libraries
import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Load data
df_train = pd.read_csv('../Dataset/Train.csv')
df_test = pd.read_csv('../Dataset/Test.csv')
df_valid = pd.read_csv('../Dataset/Valid.csv')

# Choose a model
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Tokenize and prepare datasets
...

# Train the model
trainer.train()

# Evaluate the model
...

# Test the model
...
