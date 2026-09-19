# Model

## Overview

This notebook fine-tunes a MobileBERT transformer model to classify URLs into one of four categories, treating each URL as a text sequence.

---

## Notebook

currfinal.ipynb


---

## Workflow

- Import Libraries
- Load Dataset
- Sample Data (10,000 rows)
- Train-Test Split
- Label Encoding
- Tokenization using MobileBERT tokenizer
- Model Fine-Tuning (TFAutoModelForSequenceClassification)
- Model Training
- Performance Evaluation
- Prediction
- Save Model

---

## Data Preprocessing

- Sampled 10,000 rows from the full dataset for training/testing
- Split data into train and test sets
- Encoded target labels using LabelEncoder
- Tokenized URL text using the MobileBERT tokenizer (padding, truncation, max length 128)

---

## Model Architecture

- **Base Model:** `google/mobilebert-uncased` (pretrained transformer)
- **Task Head:** Sequence classification head with 4 output labels
- **Tokenizer:** MobileBERT tokenizer (max sequence length 128)

**Loss Function:** Sparse Categorical Crossentropy
**Optimizer:** Adam (learning rate 2e-5)
**Metric:** Accuracy

---

## Training

- Trained for 3 epochs with a batch size of 100
- Validation performed on the held-out test set during training

---

## Evaluation

- Classification report (precision, recall, F1-score) across all 4 classes
- Predictions generated using argmax over model logits

---

## Saved Model

The fine-tuned model and tokenizer are saved locally under:

saved_mobilebert_model/
├── config.json
├── special_tokens_map.json
├── tf_model.h5
├── tokenizer_config.json
├── tokenizer.json
└── vocab.txt


This allows the model to be reloaded later without retraining.

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

## Running the Notebook

Start Jupyter Notebook and run all cells sequentially.

```bash
jupyter notebook
```

Open:

currfinal.ipynb


---

## Applications

- URL / Link Classification
- Phishing or Malicious Link Detection
- QR Code Link Safety Screening
- Web Security Analytics

---

## Future Improvements

- Use class names instead of generic labels (Class 0–3) for clearer reporting
- Hyperparameter tuning (learning rate, batch size, epochs)
- Address potential class imbalance
- Experiment with other lightweight transformers (DistilBERT, TinyBERT)
- Expand training data beyond the 10,000-row sample

---

## Notes

The fine-tuned model and tokenizer are saved locally after training for later reuse or deployment.