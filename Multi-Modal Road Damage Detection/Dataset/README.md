# Dataset — RDD2022 (Road Damage Dataset 2022)

## Source
**Kaggle:** https://www.kaggle.com/datasets/aliabdelmenam/rdd-2022

## Description
RDD2022 is a large-scale multi-country road damage dataset used for
automatic road damage detection and classification.

- **Size:** ~10.3 GB
- **Total Images:** 38,385
- **Countries covered:** Japan, India, Czech Republic, Norway, United States, China (Drone & MotorBike)
- **Damage Categories:**
  | Label | Description |
  |-------|-------------|
  | D00   | Longitudinal Cracks |
  | D10   | Transverse Cracks |
  | D20   | Alligator Cracks |
  | D40   | Potholes |

## Dataset Structure
```
   RDD_SPLIT/
    ├── train/
    ├── val/
    └── test/
        ├── images/    ← .jpg files (country-prefixed filenames)
        │   ├── China_Drone_*.jpg
        │   ├── China_MotorBike_*.jpg
        │   ├── Czech_*.jpg
        │   ├── India_*.jpg
        │   ├── Japan_*.jpg
        │   ├── Norway_*.jpg
        │   └── United_States_*.jpg
        │
        └── labels/    ← YOLO format .txt annotation files
            ├── China_Drone_*.txt
            ├── China_MotorBike_*.txt
            ├── Czech_*.txt
            ├── India_*.txt
            ├── Japan_*.txt
            ├── Norway_*.txt
            └── United_States_*.txt
```
