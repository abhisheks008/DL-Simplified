# Models

This folder contains the Jupyter notebook (`hindi_sentiment.ipynb`) implementing 4 deep learning models for Hindi sentiment classification.

## Implementation summary

### 1. BiLSTM (built from scratch in PyTorch)
- Custom `nn.Module` class with Embedding → BiLSTM → Dropout → Linear layers
- Word-level tokenization (whitespace split), custom vocabulary built from training data (1467 tokens)
- Manual training loop (no HuggingFace Trainer)
- ~287k parameters
- 10 epochs, peak performance at epoch 9

### 2. MuRIL (`google/muril-base-cased`)
- Google's BERT-base model pretrained on 17 Indian languages
- Loaded via `AutoModelForSequenceClassification` with a fresh classification head
- WordPiece tokenization
- ~237M parameters
- 3 epochs, fine-tuned with HuggingFace Trainer

### 3. mBERT (`bert-base-multilingual-cased`)
- Google's BERT-base model pretrained on 104 languages (Wikipedia)
- ~178M parameters
- 3 epochs, fine-tuned with HuggingFace Trainer
- **Best performing model** in this comparison

### 4. IndicBERTv2 (`ai4bharat/IndicBERTv2-MLM-only`)
- AI4Bharat's RoBERTa-base model pretrained on 23 Indian languages
- ~278M parameters
- 3 epochs, fine-tuned with HuggingFace Trainer
- Substituted for IndicBERT v1 which failed to converge under default hyperparameters

## Training configuration (transformers)
- Batch size: 16 (train), 32 (eval)
- Learning rate: default Adam (~2e-5 via Trainer)
- Epochs: 3
- Max sequence length: 128 tokens
- Mixed precision (fp16): True
- Weight decay: 0.01

## Results

| Model | Accuracy | F1 Score |
|---|---|---|
| BiLSTM | 0.683 | 0.677 |
| MuRIL | 0.717 | 0.717 |
| IndicBERTv2 | 0.779 | 0.769 |
| **mBERT** | **0.788** | **0.788** |

See the top-level README for full analysis and conclusions.
