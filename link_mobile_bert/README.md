# URL Classification using MobileBERT

## Overview

This project implements a transformer-based text classification model to categorize URLs into one of four classes. It uses MobileBERT (a lightweight BERT variant) fine-tuned on a labeled dataset of URLs, treating each URL as a text sequence for classification.

The workflow includes data preparation, tokenization, model fine-tuning, and evaluation.

---

## Project Structure

link_mobile_bert/
│
├── Dataset/
│ └── README.md
│
├── Image/
│
├── Model/
│ ├── saved_mobilebert_model/
│ │ ├── config.json
│ │ ├── special_tokens_map.json
│ │ ├── tf_model.h5
│ │ ├── tokenizer_config.json
│ │ ├── tokenizer.json
│ │ └── vocab.txt
│ ├── currfinal.ipynb
│ └── README.md
│
├── README.md
└── requirements.txt


---

## Workflow

- Import Libraries
- Load Dataset
- Sample and Split Data
- Label Encoding
- Tokenization (MobileBERT tokenizer)
- Model Fine-Tuning
- Model Training
- Performance Evaluation
- Prediction
- Save Model

---

## Required Libraries

- numpy
- pandas
- scikit-learn
- tensorflow
- transformers
- jupyter

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Applications

- URL / Link Classification
- Phishing or Malicious Link Detection
- QR Code Link Safety Screening
- Web Security Analytics

---

## Author

Developed as part of **Deep Learning Simplified**.