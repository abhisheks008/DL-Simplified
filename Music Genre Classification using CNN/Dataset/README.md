# Dataset

## GTZAN Dataset - Music Genre Classification

- **Source**: [Kaggle - GTZAN Dataset](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)
- **Original**: Collected by George Tzanetakis and Perry Cook (2002)
- **Size**: ~1.2 GB

## Description

The GTZAN dataset contains 1000 audio tracks, each 30 seconds long. It includes 10 genres with 100 tracks per genre:

| Genre | Tracks |
|-------|--------|
| Blues | 100 |
| Classical | 100 |
| Country | 100 |
| Disco | 100 |
| Hip-Hop | 100 |
| Jazz | 100 |
| Metal | 100 |
| Pop | 100 |
| Reggae | 100 |
| Rock | 100 |

## Known Limitations

- Some tracks are mislabeled
- One jazz file (`jazz.00054.wav`) in the Kaggle copy is reportedly corrupted
- The dataset is relatively small by modern standards
- Tracks were collected from various sources with different recording qualities

## Download

```bash
kaggle datasets download -d andradaolteanu/gtzan-dataset-music-genre-classification -p /tmp/gtzan --unzip
```

> **Note**: Audio files are not committed to the repository due to their size. Download the dataset locally to reproduce results.
