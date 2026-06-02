# Indian Regional Language Sentiment Analysis using Deep Learning

## PROJECT TITLE
Indian Regional Language Sentiment Analysis using Deep Learning (Hindi)

## GOAL
Build and compare multiple deep learning models for sentiment classification on Hindi text reviews. The project addresses the under-served problem of sentiment analysis in Indian regional languages, which represent half a billion+ speakers but have limited NLP tooling compared to English.

## DATASET
[AI4Bharat IndicSentiment-Translated](https://huggingface.co/datasets/ai4bharat/IndicSentiment-Translated)

- 156 reviews in the validation split (used as training data in this project)
- 1000 reviews in the test split (used for evaluation; 2 rows with NaN labels were dropped, leaving 998)
- Binary labels: Positive vs Negative
- Hindi text in Devanagari script

## DESCRIPTION
This project compares 4 different deep learning architectures on Hindi product review sentiment classification, ranging from a from-scratch BiLSTM baseline to multiple pretrained transformer-based models including Indic-specialized ones. The work is part of issue [#1065](https://github.com/abhisheks008/DL-Simplified/issues/1065). Kannada and Tamil support is planned for follow-up PRs.

## WHAT I HAD DONE
1. Loaded the AI4Bharat IndicSentiment-Translated dataset using HuggingFace's `datasets` library
2. Performed EDA: checked class balance, text length distribution, and sample reviews
3. Preprocessed data: label encoding (Negative=0, Positive=1) and tokenization (model-specific)
4. Implemented and trained 4 deep learning models:
   - BiLSTM (from-scratch PyTorch implementation with custom training loop)
   - MuRIL (Google's Indic-specialized BERT)
   - mBERT (Google's general multilingual BERT)
   - IndicBERTv2 (AI4Bharat's Indic-specialized RoBERTa)
5. Evaluated each model on the test set
6. Generated confusion matrices and training curves
7. Compared all 4 models with accuracy and F1 metrics

## MODELS USED

| Model | Architecture | Parameters | Pretraining |
|---|---|---|---|
| BiLSTM | Bidirectional LSTM | ~287k | None (random initialization) |
| MuRIL | BERT-base | ~237M | 17 Indian languages + English |
| mBERT | BERT-base | ~178M | 104 languages (Wikipedia) |
| IndicBERTv2 | RoBERTa-base | ~278M | 23 Indian languages |

## LIBRARIES NEEDED
- pandas
- numpy
- torch (PyTorch)
- transformers (HuggingFace)
- datasets (HuggingFace)
- huggingface_hub
- scikit-learn
- matplotlib
- seaborn

See `requirements.txt` for exact dependencies.

## VISUALIZATION
See the `Images/` folder for:
- Confusion matrices for each model
- Training curves (loss, accuracy, F1)
- Final model comparison bar chart

## ACCURACIES

| Model | Accuracy | F1 Score |
|---|---|---|
| BiLSTM | 0.683 | 0.677 |
| MuRIL | 0.717 | 0.717 |
| IndicBERTv2 | 0.779 | 0.769 |
| **mBERT** | **0.788** | **0.788** |

## CONCLUSION
- **mBERT achieved the best performance** at 78.8% accuracy / 0.79 F1, slightly edging out IndicBERTv2 (77.9% / 0.77).
- **MuRIL underperformed expectations** at 71.7%, despite being Indic-specialized. Possible reasons include checkpoint compatibility issues (LayerNorm naming mismatch warnings with newer `transformers` versions) and the small training set size (156 examples) not letting specialized pretraining shine.
- **The from-scratch BiLSTM baseline (68.3%)** showed clear overfitting after epoch 7, with training loss continuing to drop while test loss climbed back up. This demonstrates the value of pretrained transformers on small datasets.
- **IndicBERT v1 (ALBERT-based) failed to converge** under our default hyperparameters, getting stuck near random performance (~50% accuracy). It was substituted with IndicBERTv2 which uses modern checkpoint formats.
- All pretrained transformer models outperformed the from-scratch BiLSTM, validating the transfer learning approach for low-resource Indic NLP.
- Surprisingly, generic multilingual pretraining (mBERT) slightly edged out Indic-specialized pretraining (IndicBERTv2 / MuRIL) at this small data scale.

## FUTURE WORK
- Extend to Kannada and Tamil (planned follow-up PRs as per issue #1065)
- Hyperparameter tuning for IndicBERT v1 (lower learning rate, more epochs)
- Use a larger training set
- Explore cross-lingual transfer learning

## YOUR NAME
Mallika Suri | [GitHub: @snowhiteohno] | GSSoC 2026
