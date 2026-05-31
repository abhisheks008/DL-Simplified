# Multimodal Fake News Detection using Text and Image

## Goal
To build a fake news detection system that combines both text and image features from news articles. Most existing approaches handle text or image separately — this project combines both modalities to achieve better detection accuracy.

## Dataset
**FakeNewsNet** — https://github.com/KaiDMML/FakeNewsNet

| Subset | Real | Fake |
|--------|------|------|
| PolitiFact | 624 | 432 |
| GossipCop | 16,817 | 5,323 |
| **Total** | **17,441** | **5,755** |

- Contains news title, body text, images, and social context
- Ground truth labels verified by professional fact-checkers
- Two subsets: PolitiFact (political news) and GossipCop (entertainment news)

## Models Implemented

### Model 1 — LSTM + VGG16 (Baseline)
- **Text:** LSTM (Long Short-Term Memory) — handles sequential text, remembers context across long sentences
- **Image:** VGG16 — 16-layer CNN pretrained on ImageNet, extracts basic visual features
- **Purpose:** Simple baseline with low computational cost to benchmark other models

### Model 2 — DistilBERT + MobileNetV2 (Lightweight)
- **Text:** DistilBERT — 40% smaller than BERT, retains 97% of BERT's language understanding
- **Image:** MobileNetV2 — lightweight CNN using depthwise separable convolutions
- **Purpose:** Shows multimodal detection works even with efficient, deployment-ready models

### Model 3 — BERT-base-uncased + ResNet50 (Primary)
- **Text:** BERT-base-uncased — 12 transformer layers, bidirectional context understanding, 110M parameters
- **Image:** ResNet50 — 50-layer deep CNN with residual connections to prevent vanishing gradients
- **Purpose:** Most widely used combination in fake news research literature

### Model 4 — RoBERTa-base + EfficientNetB0 (Advanced)
- **Text:** RoBERTa — trained on 10x more data than BERT, better at detecting subtle fake news patterns
- **Image:** EfficientNetB0 — state-of-the-art CNN with compound scaling, more accurate than ResNet50
- **Purpose:** Advanced model showing if newer architectures improve over BERT+ResNet50

## Results

| Model | Accuracy | F1 Score | Precision | Recall | ROC-AUC |
|-------|----------|----------|-----------|--------|---------|
| Model 1 — LSTM + VGG16 | 0.7519 | 0.0000 | 0.0000 | 0.0000 | 0.5003 |
| Model 2 — DistilBERT + MobileNetV2 | 0.8446 | 0.6736 | 0.7032 | 0.6464 | 0.8760 |
| Model 3 — BERT + ResNet50 | 0.8366 | 0.6761 | 0.6653 | 0.6872 | 0.8861 |
| Model 4 — RoBERTa + EfficientNetB0 | **0.8478** | **0.6741** | 0.7192 | 0.6342 | 0.8746 |

## Key Observations
- Model 1 (LSTM baseline) predicts majority class only — expected for a simple baseline
- Models 2, 3, 4 all achieve above 84% accuracy showing transformer models handle fake news well
- Model 4 (RoBERTa + EfficientNetB0) achieves the best overall accuracy of **84.78%**
- Model 3 (BERT + ResNet50) achieves the best ROC-AUC of **0.8861**
- Combining text and image features consistently outperforms single-modality approaches

## Project Structure

Multimodal Fake News Detection using Text and Image/
├── Dataset/
│   └── README.md
├── Images/
│   ├── label_distribution.png
│   ├── title_length_distribution.png
│   ├── cm_Model_1_LSTM_VGG16.png
│   ├── cm_Model_2_DistilBERT_MobileNetV2.png
│   ├── cm_Model_3_BERT_ResNet50.png
│   ├── cm_Model_4_RoBERTa_EfficientNetB0.png
│   └── model_comparison.png
├── Model/
│   ├── multimodal_fake_news_detection.ipynb
│   └── README.md
└── requirements.txt

## Libraries Used
- **PyTorch** — deep learning framework
- **Torchvision** — pretrained CNN models (VGG16, ResNet50, MobileNetV2, EfficientNetB0)
- **HuggingFace Transformers** — BERT, DistilBERT, RoBERTa
- **Scikit-learn** — evaluation metrics
- **Pandas, NumPy** — data processing
- **Matplotlib, Seaborn** — visualization

## GSSoC Track
AI/ML and AI Agents

## Author
[DivyanshiVats13](https://github.com/DivyanshiVats13)