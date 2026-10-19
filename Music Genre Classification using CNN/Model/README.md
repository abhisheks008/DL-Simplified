# Model

## Music Genre Classification using CNN

### Notebook

- `music_genre_classification_using_cnn.ipynb` — full pipeline from audio loading to evaluation
- **Kaggle notebook (with outputs and trained model):** [Run on Kaggle](https://www.kaggle.com/code/gdhdgdhdh/notebook5a9d895139)

### Trained Model

The trained model (`music_genre_cnn.h5`, ~163MB) is not included in the repository due to GitHub file size limits. To obtain it:
1. Open the [Kaggle notebook](https://www.kaggle.com/code/gdhdgdhdh/notebook5a9d895139) and download from the Output section, or
2. Run the notebook locally to train and save the model

### Pipeline

1. **Audio Loading** — Load `.wav` files with `librosa` (skip corrupted files)
2. **Segmentation** — Split each 30s clip into 5s segments
3. **Feature Extraction** — Convert segments to mel-spectrograms using `librosa.feature.melspectrogram`
4. **Train/Test Split** — Split by track (not by segment) to prevent data leakage
5. **CNN Training** — Train a convolutional neural network on spectrogram images
6. **Evaluation** — Report accuracy, loss curves, and confusion matrix

### Results

See the main [README](../README.md) for accuracy scores and visualizations.
