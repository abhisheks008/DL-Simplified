# Dataset: River Images at Sao Carlos

**Source:** [Kaggle — River Images at Sao Carlos](https://www.kaggle.com/datasets/caetanoranieri/river-images-at-sao-carlos)

**Author:** Caetano Ranieri

## Description
Time-series river images captured by two cameras (SHOP, SHOP2) at Sao Carlos, 
Brazil between 2018–2022. Each image is labeled with a water level category.

## Structure
- Total images: 68,599
- Labels provided via: `flood_images_annot_2.csv`
- 4 classes: `low`, `medium`, `high`, `flood`
- 2 camera locations: `SHOP`, `SHOP2`

## How to Download
```bash
pip install kaggle
kaggle datasets download -d caetanoranieri/river-images-at-sao-carlos
```