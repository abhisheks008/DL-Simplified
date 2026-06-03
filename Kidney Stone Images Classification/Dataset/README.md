# Dataset — Kidney Stone Images

## Source
**Kaggle:** https://www.kaggle.com/datasets/safurahajiheidari/kidney-stone-images

## About the Dataset
- **Total Images:** ~1,299 CT scan images (Roboflow Universe export)
- **Classes:** `nc: 1` — single class `Tas_Var` (Turkish: "Stone Present") — all images contain stones
- **Task:** Binary classification — **Small Stone vs Large Stone** (median bounding box area split, threshold = 0.0015)
- **Annotation Format:** YOLO format (bounding box labels per image)
- **Splits:** Pre-divided into `train`, `valid`, and `test` (1054 / 123 / 123)

## Directory Structure (after download)
```
/kaggle/input/datasets/safurahajiheidari/
└── kidney-stone-images/
    ├── train/
    │   ├── images/   ← .jpg CT scan images
    │   └── labels/   ← .txt YOLO annotation files
    ├── valid/
    │   ├── images/
    │   └── labels/
    ├── test/
    │   ├── images/
    │   └── labels/
    ├── data.yaml
    ├── README.dataset.txt
    └── README.roboflow.txt
```

## Label Format (YOLO)
Each `.txt` label file contains one line per annotated stone:
```
class_id  x_center  y_center  width  height
```
All values (except `class_id`) are normalised to [0, 1].  
`class_id` is always `0` (`Tas_Var`). Multiple lines = multiple stones in the image.

## Classification Strategy
Since all images contain stones (`nc: 1`), classification uses the **largest bounding box area** per image:

- `max_area >= median (0.0015)` → **`large`** stone (label = 1)
- `max_area < median (0.0015)` → **`small`** stone (label = 0)

This guarantees a perfectly balanced 50/50 split and provides visually distinct classes — large stones occupy more of the CT image.

## How to Add in Kaggle
1. Open your Kaggle Notebook
2. Click **+ Add Data** (top right)
3. Search: `kidney-stone-images safurahajiheidari`
4. Click **Add**
5. Dataset mounts at `/kaggle/input/datasets/safurahajiheidari/kidney-stone-images/`

> **Note:** Set `DATASET_PATH = '/kaggle/input/datasets/safurahajiheidari/kidney-stone-images'` in Cell 1.
```
