# QR Code to Link Classification using MobileBERT

## Overview

This project detects malicious QR codes by decoding the embedded URL from each QR code image and classifying it as benign or malicious using a fine-tuned MobileBERT transformer model.

The workflow includes QR code decoding, dataset construction, tokenization, model fine-tuning, and evaluation.

---

## Project Structure

QR_img_to_link_mobile_bert/
│
├── Dataset/
│ └── README.md
│
├── Image/
│
├── Model/
│ ├── safescan_model/
│ │ ├── config.json
│ │ ├── special_tokens_map.json
│ │ ├── tf_model.h5
│ │ ├── tokenizer_config.json
│ │ ├── tokenizer.json
│ │ └── vocab.txt
│ ├── code.ipynb
│ └── README.md
│
├── README.md
└── requirements.txt


---

## Workflow

- Import Libraries
- Load QR Code Images (benign and malicious)
- Decode URLs from QR Codes
- Build Labeled Dataset
- Train-Test Split
- Tokenization (MobileBERT tokenizer)
- Model Fine-Tuning
- Model Training
- Performance Evaluation
- Save Model

---

## Required Libraries

- pandas
- numpy
- matplotlib
- pillow
- pyzbar
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

- Malicious QR Code Detection
- QR Code Safety Screening
- Phishing Link Prevention
- Mobile Security Tools

---

## Author

Developed as part of **Deep Learning Simplified**.