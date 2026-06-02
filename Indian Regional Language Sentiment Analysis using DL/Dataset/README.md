# Dataset

## Source
[AI4Bharat IndicSentiment-Translated](https://huggingface.co/datasets/ai4bharat/IndicSentiment-Translated) on HuggingFace.

## About
The Indic Sentiment Analysis dataset (Translated version) contains product reviews in Hindi (Devanagari script) labeled with binary sentiment (Positive / Negative). The dataset spans multiple product categories including electronics, home appliances, entertainment apps, transportation, and more.

## Statistics
- **Validation split:** 156 reviews (used as training data in this project, since the dataset has no separate train split)
- **Test split:** 1000 reviews (998 used after dropping 2 rows with missing labels)
- **Class distribution:** approximately balanced (52% Positive, 48% Negative in validation)
- **Language:** Hindi (Devanagari script)
- **Format:** Parquet (loaded via HuggingFace `datasets` library)

## Columns used
- `INDIC REVIEW`: the Hindi review text (input)
- `LABEL`: sentiment label, either "Positive" or "Negative" (target)

Other columns (CATEGORY, BRAND, ASPECTS, etc.) were not used in this project but could be leveraged for richer analysis in future work.

## Loading
```python
from datasets import load_dataset
dataset = load_dataset("ai4bharat/IndicSentiment-Translated")
```
