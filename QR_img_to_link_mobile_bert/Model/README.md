# Model

## Overview

This notebook fine-tunes a MobileBERT transformer model to classify QR codes as benign or malicious, based on the URL decoded from each QR code image.

---

## Notebook

code.ipynb


---

## Workflow

- Import Libraries
- Load QR Code Images (benign and malicious folders)
- Decode Embedded URLs using pyzbar
- Build Labeled Dataset (url, label)
- Train-Test Split (stratified)
- Tokenization using MobileBERT tokenizer
- Convert to TensorFlow Datasets
- Model Fine-Tuning (TFAutoModelForSequenceClassification)
- Model Training
- Performance Evaluation
- Save Model

---

## Data Preprocessing

- Decoded URLs from QR code images using pyzbar
- Benign QR codes labeled 0, malicious QR codes labeled 1
- Decoded dataset saved to `decoded_urls.csv`
- Checked for duplicate URLs
- Stratified train-test split (80/20) to preserve class balance
- Tokenized URLs using the MobileBERT tokenizer (padding, truncation, max length 128)
- Converted tokenized data into TensorFlow `Dataset` objects, batched (batch size 16)

---

## Model Architecture

- **Base Model:** `google/mobilebert-uncased` (pretrained transformer)
- **Task Head:** Sequence classification head with 2 output labels (benign / malicious)
- **Tokenizer:** MobileBERT tokenizer (max sequence length 128)

**Loss Function:** Sparse Categorical Crossentropy (from logits)
**Optimizer:** Adam (learning rate 2e-5)
**Metric:** Accuracy

---

## Training

- Trained for 3 epochs
- Validation performed on the held-out test set during training
- Model evaluated on the test set after training using `model.evaluate()`

---

## Evaluation

- Classification report (precision, recall, F1-score) for benign vs. malicious classes
- Confusion matrix
- Duplicate URL check for dataset quality

---

## Saved Model

The fine-tuned model and tokenizer are saved locally under:

safescan_model/
├── config.json
├── special_tokens_map.json
├── tf_model.h5
├── tokenizer_config.json
├── tokenizer.json
└── vocab.txt


This allows the model to be reloaded later without retraining.

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

## Running the Notebook

Start Jupyter Notebook and run all cells sequentially.

```bash
jupyter notebook
```

Open:

code.ipynb


---

## Applications

- Malicious QR Code Detection
- QR Code Safety Screening
- Phishing Link Prevention
- Mobile Security Tools

---

## Future Improvements

- Balance the benign/malicious dataset if class imbalance exists
- Hyperparameter tuning (learning rate, batch size, epochs)
- Handle QR codes that fail to decode (image quality, damage)
- Experiment with other lightweight transformers (DistilBERT, TinyBERT)
- Deploy as a real-time QR scanning safety check

---

## Notes

QR code images that could not be decoded into a valid URL are excluded from the dataset.