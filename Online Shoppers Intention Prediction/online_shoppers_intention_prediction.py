#!/usr/bin/env python3
"""Online Shoppers Intention Prediction - Complete Pipeline

This script loads the online shoppers dataset, preprocesses the data,
trains four deep learning models, evaluates them, saves the models and
encoders, and generates diagnostic visualizations.
"""

from pathlib import Path
import os
import warnings
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, GRU
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

warnings.filterwarnings('ignore')

DATA_PATH = Path('Dataset') / 'online_shoppers_intention.csv'
MODEL_DIR = Path('Models')
IMAGE_DIR = Path('Image')

MODEL_DIR.mkdir(parents=True, exist_ok=True)
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found at {DATA_PATH}.\n"
        f"Please place `online_shoppers_intention.csv` inside the `Dataset/` folder."
    )

print('Starting Online Shoppers Intention Prediction pipeline')
print(f'Dataset path: {DATA_PATH.resolve()}')

# ---------------------------------------------------------------------------
# STEP 1: LOAD DATA
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 1: LOAD DATA')
print('=' * 70)

df = pd.read_csv(DATA_PATH)
print(f'\nDataset Shape: {df.shape}')
print(f'Rows: {df.shape[0]} | Columns: {df.shape[1]}')
print('\nFirst 3 rows:')
print(df.head(3).to_string(index=False))
print('\nColumn types:')
print(df.dtypes)
print('\nMissing values:')
print(df.isnull().sum())

# ---------------------------------------------------------------------------
# STEP 2: CLEAN DATA
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 2: CLEAN DATA')
print('=' * 70)

duplicate_count = df.duplicated().sum()
print(f'Duplicate rows found: {duplicate_count}')
if duplicate_count > 0:
    df = df.drop_duplicates()
    print(f'Dropped duplicates. New shape: {df.shape}')
else:
    print('No duplicates found')

missing_counts = df.isnull().sum()
missing_total = missing_counts.sum()
if missing_total == 0:
    print('No missing values found')
else:
    print('Missing values detected:')
    print(missing_counts[missing_counts > 0])
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median(), inplace=True)
    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].mode()[0], inplace=True)
    print('Missing values filled')

# ---------------------------------------------------------------------------
# STEP 3: EXPLORATORY DATA ANALYSIS
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 3: EXPLORATORY DATA ANALYSIS')
print('=' * 70)

print('\nDescriptive statistics:')
print(df.describe(include='all').transpose())
if 'Revenue' in df.columns:
    revenue_dist = df['Revenue'].value_counts()
    print('\nRevenue distribution:')
    print(revenue_dist)
    print('\nClass balance (%):')
    print((revenue_dist / len(df) * 100).round(2))

# ---------------------------------------------------------------------------
# STEP 4: PREPROCESSING
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 4: PREPROCESSING')
print('=' * 70)

numeric_features = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = df.select_dtypes(include=['object']).columns.tolist()
print(f'\nNumeric features ({len(numeric_features)}): {numeric_features}')
print(f'Categorical features ({len(categorical_features)}): {categorical_features}')

X = df.drop('Revenue', axis=1)
y = df['Revenue']

# Encode categorical columns so models can process them as numeric values
label_encoders = {}
for col in categorical_features:
    if col in X.columns:
        encoder = LabelEncoder()
        X[col] = encoder.fit_transform(X[col].astype(str))
        label_encoders[col] = encoder
        print(f'Encoded {col} with {len(encoder.classes_)} classes')

le_target = LabelEncoder()
y = le_target.fit_transform(y.astype(str))
print(f'Encoded target Revenue: {list(le_target.classes_)}')

print(f'\nFeatures shape: {X.shape}')
print(f'Target shape: {y.shape}')

# ---------------------------------------------------------------------------
# STEP 5: TRAIN/TEST SPLIT
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 5: TRAIN-TEST SPLIT')
print('=' * 70)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print(f'\nTraining set: {X_train.shape}')
print(f'Test set: {X_test.shape}')
print('\nTraining target distribution:')
print(pd.Series(y_train).value_counts())
print('\nTest target distribution:')
print(pd.Series(y_test).value_counts())

# ---------------------------------------------------------------------------
# STEP 6: FEATURE SCALING
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 6: FEATURE SCALING')
print('=' * 70)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print('StandardScaler fitted on training data')
print(f'Training mean: {X_train_scaled.mean():.6f} | std: {X_train_scaled.std():.6f}')
print(f'Test mean: {X_test_scaled.mean():.6f} | std: {X_test_scaled.std():.6f}')

# ---------------------------------------------------------------------------
# STEP 7: BUILD MODELS
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 7: BUILDING MODELS')
print('=' * 70)

early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

model1 = Sequential([
    Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid'),
])
model1.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
print('\nBuilt model: MLP')
model1.summary()

# Reshape scaled data into sequences for RNN models
X_train_lstm = X_train_scaled.reshape((X_train_scaled.shape[0], X_train_scaled.shape[1], 1))
X_test_lstm = X_test_scaled.reshape((X_test_scaled.shape[0], X_test_scaled.shape[1], 1))

model2 = Sequential([
    LSTM(64, activation='relu', input_shape=(X_train_lstm.shape[1], 1), return_sequences=True),
    Dropout(0.3),
    LSTM(32, activation='relu'),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid'),
])
model2.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
print('\nBuilt model: LSTM')
model2.summary()

model3 = Sequential([
    GRU(64, activation='relu', input_shape=(X_train_lstm.shape[1], 1), return_sequences=True),
    Dropout(0.3),
    GRU(32, activation='relu'),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid'),
])
model3.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
print('\nBuilt model: GRU')
model3.summary()

model4 = Sequential([
    Dense(256, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dropout(0.4),
    Dense(128, activation='relu'),
    Dropout(0.4),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid'),
])
model4.compile(optimizer=Adam(learning_rate=0.0005), loss='binary_crossentropy', metrics=['accuracy'])
print('\nBuilt model: Deep Feedforward')
model4.summary()

# ---------------------------------------------------------------------------
# STEP 8: TRAIN MODELS
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 8: TRAINING MODELS')
print('=' * 70)

print('\nTraining Model 1: MLP')
history1 = model1.fit(
    X_train_scaled,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0,
)
print('Model 1 training complete')

print('\nTraining Model 2: LSTM')
history2 = model2.fit(
    X_train_lstm,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0,
)
print('Model 2 training complete')

print('\nTraining Model 3: GRU')
history3 = model3.fit(
    X_train_lstm,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0,
)
print('Model 3 training complete')

print('\nTraining Model 4: Deep Feedforward')
history4 = model4.fit(
    X_train_scaled,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0,
)
print('Model 4 training complete')

# ---------------------------------------------------------------------------
# STEP 9: EVALUATE MODELS
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 9: EVALUATING MODELS')
print('=' * 70)

predictions = []
probabilities = []
scores = {}

# Evaluate each model on the same test set and capture metrics for comparison
for name, model, X_eval in [
    ('MLP', model1, X_test_scaled),
    ('LSTM', model2, X_test_lstm),
    ('GRU', model3, X_test_lstm),
    ('Deep Network', model4, X_test_scaled),
]:
    y_pred_proba = model.predict(X_eval, verbose=0).flatten()
    y_pred = (y_pred_proba > 0.5).astype(int)
    predictions.append(y_pred)
    probabilities.append(y_pred_proba)

    scores[name] = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, zero_division=0),
        'Recall': recall_score(y_test, y_pred, zero_division=0),
        'F1-Score': f1_score(y_test, y_pred, zero_division=0),
        'ROC-AUC': roc_auc_score(y_test, y_pred_proba),
    }
    print(f'\n{name} Metrics:')
    for metric_name, metric_value in scores[name].items():
        print(f'   {metric_name}: {metric_value:.4f}')

acc1, acc2, acc3, acc4 = (
    scores['MLP']['Accuracy'],
    scores['LSTM']['Accuracy'],
    scores['GRU']['Accuracy'],
    scores['Deep Network']['Accuracy'],
)
prec1, prec2, prec3, prec4 = (
    scores['MLP']['Precision'],
    scores['LSTM']['Precision'],
    scores['GRU']['Precision'],
    scores['Deep Network']['Precision'],
)
rec1, rec2, rec3, rec4 = (
    scores['MLP']['Recall'],
    scores['LSTM']['Recall'],
    scores['GRU']['Recall'],
    scores['Deep Network']['Recall'],
)
f1_1, f1_2, f1_3, f1_4 = (
    scores['MLP']['F1-Score'],
    scores['LSTM']['F1-Score'],
    scores['GRU']['F1-Score'],
    scores['Deep Network']['F1-Score'],
)
auc1, auc2, auc3, auc4 = (
    scores['MLP']['ROC-AUC'],
    scores['LSTM']['ROC-AUC'],
    scores['GRU']['ROC-AUC'],
    scores['Deep Network']['ROC-AUC'],
)

# ---------------------------------------------------------------------------
# STEP 10: SAVE MODELS AND ENCODERS
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 10: SAVING MODELS AND ENCODERS')
print('=' * 70)

model1.save(MODEL_DIR / '01_mlp_model.h5')
print('Saved: 01_mlp_model.h5')
model2.save(MODEL_DIR / '02_lstm_model.h5')
print('Saved: 02_lstm_model.h5')
model3.save(MODEL_DIR / '03_gru_model.h5')
print('Saved: 03_gru_model.h5')
model4.save(MODEL_DIR / '04_deep_network_model.h5')
print('Saved: 04_deep_network_model.h5')

with open(MODEL_DIR / 'feature_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
print('Saved: feature_scaler.pkl')
with open(MODEL_DIR / 'label_encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)
print('Saved: label_encoders.pkl')
with open(MODEL_DIR / 'target_encoder.pkl', 'wb') as f:
    pickle.dump(le_target, f)
print('Saved: target_encoder.pkl')

# ---------------------------------------------------------------------------
# STEP 11: MODEL COMPARISON
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 11: MODEL COMPARISON')
print('=' * 70)

comparison_df = pd.DataFrame(
    [
        {'Model': k, **v}
        for k, v in scores.items()
    ]
)
print('\nPerformance Comparison:')
print(comparison_df.to_string(index=False))

best_idx = comparison_df['F1-Score'].idxmax()
best_model_name = comparison_df.loc[best_idx, 'Model']
print(f'\nBest Model: {best_model_name} (F1-Score: {comparison_df.loc[best_idx, "F1-Score"]:.4f})')

# ---------------------------------------------------------------------------
# STEP 12: VISUALIZATIONS
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 12: GENERATING VISUALIZATIONS')
print('=' * 70)

plt.style.use('seaborn-v0_8-darkgrid')

# Training history
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Model Training History Comparison', fontsize=16, fontweight='bold')

for ax, history, title in zip(
    axes.flatten(),
    [history1, history2, history3, history4],
    ['MLP', 'LSTM', 'GRU', 'Deep Network'],
):
    ax.plot(history.history['accuracy'], label='Train', linewidth=2)
    ax.plot(history.history['val_accuracy'], label='Val', linewidth=2)
    ax.set_title(f'{title} - Accuracy')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Accuracy')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(IMAGE_DIR / '01_training_history.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved: 01_training_history.png')

# Model performance comparison
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Model Performance Metrics Comparison', fontsize=16, fontweight='bold')
metrics_list = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
for idx, metric in enumerate(metrics_list):
    ax = axes[idx // 3, idx % 3]
    bars = ax.bar(comparison_df['Model'], comparison_df[metric], color=colors, edgecolor='black', linewidth=1.5)
    ax.set_title(metric)
    ax.set_ylim(0, 1)
    ax.grid(True, alpha=0.3, axis='y')
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.3f}', ha='center', va='bottom', fontsize=9)
axes[1, 2].axis('off')
plt.tight_layout()
plt.savefig(IMAGE_DIR / '02_model_comparison.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved: 02_model_comparison.png')

# Confusion matrices
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Confusion Matrices - All Models', fontsize=16, fontweight='bold')
for idx, (y_pred, label) in enumerate(zip(predictions, ['MLP', 'LSTM', 'GRU', 'Deep Network'])):
    ax = axes[idx // 2, idx % 2]
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        cbar=False,
        xticklabels=['No Purchase', 'Purchase'],
        yticklabels=['No Purchase', 'Purchase'],
        ax=ax,
    )
    ax.set_title(label)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
plt.tight_layout()
plt.savefig(IMAGE_DIR / '03_confusion_matrices.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved: 03_confusion_matrices.png')

# ROC curves
fig, ax = plt.subplots(figsize=(10, 8))
for y_proba, label, auc_score in zip(
    probabilities,
    ['MLP', 'LSTM', 'GRU', 'Deep Network'],
    [auc1, auc2, auc3, auc4],
):
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    ax.plot(fpr, tpr, linewidth=2.5, label=f'{label} (AUC={auc_score:.3f})')
ax.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('ROC Curves - All Models')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(IMAGE_DIR / '04_roc_curves.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved: 04_roc_curves.png')

# Feature importance via correlation
feature_target_corr = pd.DataFrame({
    'Feature': X.columns,
    'Correlation': [np.corrcoef(X[col], y)[0, 1] for col in X.columns],
}).sort_values('Correlation', key=abs, ascending=False).head(15)
fig, ax = plt.subplots(figsize=(12, 8))
colors_bar = ['#FF6B6B' if x < 0 else '#4ECDC4' for x in feature_target_corr['Correlation']]
ax.barh(feature_target_corr['Feature'], feature_target_corr['Correlation'], color=colors_bar, edgecolor='black', linewidth=1.5)
ax.set_xlabel('Correlation with Revenue')
ax.set_title('Top 15 Features by Correlation')
ax.grid(True, alpha=0.3, axis='x')
for bar in ax.patches:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.3f}', ha='left' if width >= 0 else 'right', va='center', fontsize=9)
plt.tight_layout()
plt.savefig(IMAGE_DIR / '05_feature_importance.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved: 05_feature_importance.png')

# Data distribution
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
revenue_counts = pd.Series(y).value_counts()
axes[0].pie(
    revenue_counts,
    labels=['No Purchase', 'Purchase'],
    autopct='%1.1f%%',
    colors=['#FF6B6B', '#4ECDC4'],
    startangle=90,
    textprops={'fontsize': 11, 'fontweight': 'bold'},
)
axes[0].set_title('Target Distribution')
train_revenue = pd.Series(y_train).value_counts()
test_revenue = pd.Series(y_test).value_counts()
x_pos = np.arange(2)
width = 0.35
axes[1].bar(x_pos - width / 2, [train_revenue.get(0, 0), train_revenue.get(1, 0)], width, label='Train', color='#4ECDC4', edgecolor='black')
axes[1].bar(x_pos + width / 2, [test_revenue.get(0, 0), test_revenue.get(1, 0)], width, label='Test', color='#FF6B6B', edgecolor='black')
axes[1].set_xticks(x_pos)
axes[1].set_xticklabels(['No Purchase', 'Purchase'])
axes[1].set_ylabel('Count')
axes[1].set_title('Train vs Test Distribution')
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig(IMAGE_DIR / '06_data_distribution.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved: 06_data_distribution.png')

# ---------------------------------------------------------------------------
# FINAL SUMMARY
# ---------------------------------------------------------------------------
print('\n' + '=' * 70)
print('STEP 13: FINAL SUMMARY')
print('=' * 70)
print(f"\nBest model: {best_model_name} with F1-Score = {comparison_df.loc[best_idx, 'F1-Score']:.4f}")
print(f'All models and visualizations have been saved in:')
print(f'  - {MODEL_DIR.resolve()}')
print(f'  - {IMAGE_DIR.resolve()}')
print('\nPipeline complete!')
