import pandas as pd
import numpy as np
import torch
from transformers import BertTokenizer, BertForSequenceClassification, RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Text preprocessing using NLTK
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_words)

# Load dataset
data = pd.read_csv('path_to_your_dataset.csv')
data['text'] = data['text'].apply(preprocess_text)

# Split dataset
train_texts, val_texts, train_labels, val_labels = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

# Tokenization and Encoding for BERT
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
train_encodings = bert_tokenizer(list(train_texts), truncation=True, padding=True, max_length=128)
val_encodings = bert_tokenizer(list(val_texts), truncation=True, padding=True, max_length=128)

# Tokenization and Encoding for RoBERTa
roberta_tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
train_encodings_roberta = roberta_tokenizer(list(train_texts), truncation=True, padding=True, max_length=128)
val_encodings_roberta = roberta_tokenizer(list(val_texts), truncation=True, padding=True, max_length=128)

# Convert to PyTorch dataset
class SentimentDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels.iloc[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset_bert = SentimentDataset(train_encodings, train_labels)
val_dataset_bert = SentimentDataset(val_encodings, val_labels)
train_dataset_roberta = SentimentDataset(train_encodings_roberta, train_labels)
val_dataset_roberta = SentimentDataset(val_encodings_roberta, val_labels)

# Model definition for BERT
model_bert = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Model definition for RoBERTa
model_roberta = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)

# Training Arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=1,
    weight_decay=0.01,
)

# Evaluation Function
def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='binary')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }

# Training BERT Model
trainer_bert = Trainer(
    model=model_bert,
    args=training_args,
    train_dataset=train_dataset_bert,
    eval_dataset=val_dataset_bert,
    compute_metrics=compute_metrics,
)
trainer_bert.train()

# Training RoBERTa Model
trainer_roberta = Trainer(
    model=model_roberta,
    args=training_args,
    train_dataset=train_dataset_roberta,
    eval_dataset=val_dataset_roberta,
    compute_metrics=compute_metrics,
)
trainer_roberta.train()

# Evaluate models
bert_eval = trainer_bert.evaluate()
roberta_eval = trainer_roberta.evaluate()

print("BERT Evaluation:", bert_eval)
print("RoBERTa Evaluation:", roberta_eval)