# Model

## Overview

This notebook implements a multi-label emotion classification system using an LSTM neural network. The model processes textual comments and predicts multiple emotion labels simultaneously.

**Note:** Model accuracy is still being improved.

---

## Workflow

- Import Libraries
- Load Dataset
- Data Cleaning
- Train-Test Split
- Tokenization
- Sequence Padding
- LSTM Model Development
- Model Training
- Performance Evaluation
- Prediction

---

## Data Preprocessing

- Dropped the id column
- Converted boolean label columns to 0/1
- Split data into text (features) and emotion labels (targets)
- Tokenized text using a vocabulary of the top 10,000 words
- Converted text to integer sequences
- Padded sequences to a fixed length (maxlen=100)

---

## Neural Network Architecture

The model consists of:

- Embedding Layer (vocab size 10,000, output dimension 128)
- LSTM Layer (128 units, dropout 0.2, recurrent dropout 0.2)
- Dense Layer (64 neurons, ReLU)
- Output Layer (29 neurons, Sigmoid)

**Loss Function:** Binary Crossentropy
**Optimizer:** Adam
**Metric:** Accuracy

---

## Training

- Trained across multiple fit calls with varying batch sizes and epoch counts to iteratively continue training
- Batch cross-entropy loss used to handle the multi-label nature of the task

---

## Evaluation

- Classification report (precision, recall, F1-score)
- Confusion matrix visualization

---

## Required Libraries

- numpy
- pandas
- scikit-learn
- tensorflow
- seaborn
- jupyter

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Running the Notebook

Start Jupyter Notebook and run all cells sequentially.

```bash
jupyter notebook
```

---

## Applications

- Emotion Detection in Text
- Sentiment/Emotion Analytics
- Social Media Monitoring
- Customer Feedback Analysis

---

## Future Improvements

- Implement a Bidirectional LSTM
- Add additional dropout layers to reduce overfitting
- Use pretrained embeddings such as GloVe or Word2Vec
- Experiment with transformer-based architectures such as BERT
- Add proper evaluation with model.evaluate() on the held-out test set

---

## Notes

This notebook is a work in progress; accuracy is currently limited and further tuning is planned.