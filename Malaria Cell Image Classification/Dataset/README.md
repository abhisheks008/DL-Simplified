# Datasets

The dataset used in the project is taken from TensorFlow Datasets. A similar dataset is also available on Kaggle.

## Link for dataset

The dataset is available on [Kaggle](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria/data) and [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/malaria).

## About the dataset

The Malaria dataset contains a total of 27,558 cell images with equal instances of parasitized and uninfected cells from the thin blood smear slide images of segmented cells.

Additional Documentation: [Papers With Code](https://paperswithcode.com/dataset/malaria-dataset)

Homepage: [National Library of Medicine](https://lhncbc.nlm.nih.gov/publication/pub9932)

Splits:

| Split   | Examples |
| ------- | -------- |
| 'train' | 27,558   |

Feature structure:

```
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
})
```
