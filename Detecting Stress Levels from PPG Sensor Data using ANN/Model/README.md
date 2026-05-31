# Stress Level Detection from PPG Sensor Data — Model README

## Problem Statement
Multi-class classification of physiological stress levels (No Stress, Interruption, Time Pressure)
using HRV features derived from PPG sensor data.

## Dataset
- Source: [Heart Rate Prediction to Monitor Stress Level](https://www.kaggle.com/datasets/vinayakshanawad/heart-rate-prediction-to-monitor-stress-level)
- Train samples: 369,289 | Test samples: 73,858
- Features: 34 HRV features (time-domain, frequency-domain, non-linear)
- Classes: no stress (54.2%), interruption (28.5%), time pressure (17.3%)

## Models Implemented

| Model   | Test Accuracy | Notes |
|---------|--------------|-------|
| ANN     | 99.93%       | Baseline feedforward, 3 Dense layers |
| 1D-CNN  | **99.99%**   | Best model, 2 Conv1D layers |
| LSTM    | 99.90%       | Slowest training (~43s/epoch) |
| GRU     | 99.94%       | Lighter than LSTM, competitive accuracy |

## Best Model: 1D-CNN
- Architecture: Conv1D(64) → MaxPool → Conv1D(32) → Flatten → Dense(64) → Dense(3)
- Precision / Recall / F1: 1.00 across all 3 classes
- Misclassifications: 10 out of 73,858 test samples

## Preprocessing
- Merged 3 feature CSV files on `uuid` key
- Dropped `uuid` and `datasetId` columns
- Label encoded target (`condition`)
- StandardScaler normalization
- 80/20 stratified train-test split
- Reshaped to (samples, 34, 1) for sequence models

## Conclusion
1D-CNN achieves near-perfect classification while being 4x faster per epoch than LSTM/GRU.
For tabular HRV features, local pattern detection via convolution outperforms recurrent approaches.
ANN is a strong baseline given the well-separated feature space visible in the correlation heatmap.
