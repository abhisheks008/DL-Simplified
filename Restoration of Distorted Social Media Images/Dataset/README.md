# Dataset: Flickr-Faces-HQ (FFHQ) Small

This directory contains metadata and integration instructions for the facial dataset used in the restoration pipeline.

## Dataset Overview
The project utilizes the **Flickr-Faces-HQ (FFHQ) Small** dataset, a reduced version of the high-quality FFHQ dataset provided by NVIDIA. It is specifically selected for training facial restoration models due to its diversity in age, ethnicity, and facial accessories.

- **Source**: [Kaggle - tommykamaz/faces-dataset-small](https://www.kaggle.com/datasets/tommykamaz/faces-dataset-small)
- **Original Data**: [NVIDIA FFHQ Repository](https://github.com/NVlabs/ffhq-dataset)
- **Total Samples**: 3,143 images
- **Resolution**: 1024 x 1024 (Downsampled to 256 x 256 in the training pipeline)
- **Format**: PNG
- **License**: Creative Commons BY-NC-SA 4.0 (NVIDIA) / CC BY 4.0 (Kaggle Version)

## Integration Workflow
The training pipeline handles dataset acquisition autonomously via `kagglehub`. Manual download into this directory is not required for the standard execution flow.

### Automated Synchronization
The `facial_restoration_gan.ipynb` notebook executes the following retrieval logic:

```python
import kagglehub
path = kagglehub.dataset_download('tommykamaz/faces-dataset-small')
```

The data is stored in the `kagglehub` cache directory (e.g., `~/.cache/kagglehub/`) to maintain workspace cleanliness and avoid redundant storage in the project root.

### Data Preprocessing
Images are processed via the `FaceDataset` class with the following invariants:
1. **Normalization**: Tensors are normalized to the range `[0, 1]`.
2. **Resizing**: Bi-linear interpolation to a fixed resolution of **256 x 256**.
3. **Synthetic Distortion**: Real-time application of JPEG compression (10-50 quality), Gaussian noise, and blur to create paired training samples.

## Folder Structure Guidelines
If manually adding data, ensure the following structure within the `Dataset/` directory:
```text
Dataset/
└── images/
    ├── 00001.png
    ├── 00002.png
    └── ...
```
All `.png` and `.jpg` files located recursively within this folder will be indexed by the dataset loader.
