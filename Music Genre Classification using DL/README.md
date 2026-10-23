# Music Genre Classification using Deep Learning

Classify music into 10 genres using mel-spectrograms and deep learning models trained on the GTZAN dataset.

## Dataset

**GTZAN** — 1,000 audio tracks, 10 genres (100 tracks each, 30s per clip)

Genres: blues, classical, country, disco, hiphop, jazz, metal, pop, reggae, rock

Source: [GTZAN Dataset on Kaggle](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)

## Preprocessing

- Audio loaded using librosa (SR = 22050 Hz), corrupted files skipped (e.g., `jazz.00054.wav`)
- Each 30s clip split into 10 x 3s segments to increase training samples (~10x)
- Mel-spectrograms extracted (128 mel bands, hop_length=512) with per-sample standardization
- Train/Val/Test split (70/15/15) by **track** (not segment) to prevent data leakage
- SpecAugment (frequency + time masking) applied during training

## Models

| Model | Segment Acc | Track Acc |
|-------|:-----------:|:---------:|
| Custom CNN | 64.91% | 70.67% |
| VGG16 | 84.59% | 88.67% |
| ResNet50 | **82.66%** | **89.33%** |
| EfficientNet-B0 | 82.05% | 88.67% |

- **Best model: ResNet50** (89.33% track-level accuracy)
- Track-level accuracy uses probability averaging across all segments of a track
- Label smoothing (0.1), ReduceLROnPlateau, and EarlyStopping (patience=8) used for training
- Transfer learning models use ImageNet-pretrained backbones with 2-phase training (head warmup + full fine-tuning)

## Kaggle Notebook

Training notebook: [https://www.kaggle.com/code/gdhdgdhdh/notebook05619fb6c2](https://www.kaggle.com/code/gdhdgdhdh/notebook05619fb6c2)

## Web App

Streamlit app to upload a `.wav` file, view the mel-spectrogram, and get the predicted genre with confidence scores.

Before starting the app, provide `Model/genre_classifier.keras`.
Generate it by running the final export cell in `Model/Music_Genre_Classification.ipynb`,
or download the trained artifact from the project release.

```bash
pip install -r requirements.txt
streamlit run "Web App/app.py"
```

## Folder Structure

```
├── Dataset/                  # GTZAN dataset (not included)
├── Images/                   # Training plots and evaluation charts
├── Model/
│   ├── Music_Genre_Classification.ipynb   # Training notebook
│   ├── genre_classifier.keras             # Best trained model (ResNet50)
│   └── model_metadata.json                # Model config and results
├── Web App/
│   └── app.py                # Streamlit web app
├── requirements.txt
└── README.md
```
