# 🩺 Facial Skin Diseases Classification using Deep Learning

> **GSSoC 2026 Contribution** | Deep Learning Simplified Repository

---

## 📌 Project Overview

This project focuses on classifying skin diseases using multiple deep learning architectures and comparing their performance to identify the most effective model. The workflow includes dataset preparation, exploratory data analysis (EDA), model training, evaluation, and comparison.

---

## 📂 Dataset

### Original Dataset Mentioned in Issue

**Facial Skin Diseases Dataset (Kaggle)**

The original dataset provided in the issue contained only a single class (Acne), making it unsuitable for multi-class classification and comparison of deep learning architectures.

After discussing the limitation in the issue thread, a multi-class dataset was used for meaningful evaluation.

### Dataset Used

**DermNet Dataset (Kaggle)**

Source: https://www.kaggle.com/datasets/shubhamgoel27/dermnet

DermNet contains dermatology images across multiple skin disease categories and is suitable for image classification tasks.

### Subset Used

A balanced 7-class subset was created for training and evaluation.

| Class                                            | Train Images | Test Images |
| ------------------------------------------------ | ------------ | ----------- |
| Actinic Keratosis / Basal Cell Carcinoma         | 300          | 60          |
| Eczema                                           | 300          | 60          |
| Melanoma / Skin Cancer / Nevi & Moles            | 300          | 60          |
| Nail Fungus & Other Nail Disease                 | 300          | 60          |
| Psoriasis / Lichen Planus                        | 300          | 60          |
| Tinea Ringworm / Candidiasis / Fungal Infections | 300          | 60          |
| Warts Molluscum & Other Viral Infections         | 300          | 60          |
| **Total**                                        | **2100**     | **420**     |

---

## 🔍 Exploratory Data Analysis (EDA)

The following exploratory analysis was performed before model training:

* Class distribution analysis across all selected categories
* Visualization of sample images from each disease class
* Verification of dataset balance before training

---

## 🧠 Models Implemented

The following deep learning models were trained and evaluated:

| # | Model          |
| - | -------------- |
| 1 | Custom CNN     |
| 2 | VGG16          |
| 3 | ResNet50       |
| 4 | EfficientNetB0 |
| 5 | MobileNetV2    |
| 6 | DenseNet121    |
| 7 | Xception       |

### Training Configuration

* Transfer learning using ImageNet pretrained weights
* Fine-tuning of higher layers
* Data augmentation using rotation, shifts, zoom, shear, and horizontal flipping
* Adam optimizer
* EarlyStopping and ReduceLROnPlateau callbacks
* Categorical Crossentropy loss

---

## 📊 Results

### Model Performance Comparison

| Model          | Test Accuracy | Test Loss |
| -------------- | ------------- | --------- |
| VGG16          | **56.19%**    | 1.4381    |
| Xception       | 47.62%        | 1.4501    |
| MobileNetV2    | 38.81%        | 1.7851    |
| ResNet50       | 38.10%        | 1.7304    |
| DenseNet121    | 35.48%        | 2.1343    |
| Custom CNN     | 24.05%        | 2.9582    |
| EfficientNetB0 | 14.29%        | 1.9900    |

### Best Performing Model

**VGG16 achieved the highest test accuracy of 56.19%.**

The model showed better feature extraction capability on the selected DermNet subset compared to the other evaluated architectures.

---

## ✅ Conclusion

Seven deep learning architectures were evaluated on a balanced subset of the DermNet dataset.

Among all evaluated architectures, VGG16 achieved the highest test accuracy (56.19%) and delivered the best overall performance on the selected DermNet subset. These results highlight the effectiveness of transfer learning for skin disease classification tasks.

---

## 🗂️ Project Structure

```text
Facial Skin Diseases Classification using DL/
│
├── Images/
│   ├── all_models_comparison.png
│   ├── all_models_loss.png
│   ├── model_comparison.csv
│   └── history plots, confusion matrices, and classification reports
│
├── Dataset/
│   └── dataset_info.md
│
├── Model/
│   ├── README.md
│   └── FacialSkinDetection_Complete.ipynb
│
├── requirements.txt
└── .gitignore
```

---

## 🚀 How to Run

### Google Colab

1. Open the notebook in Google Colab.
2. Enable GPU runtime.
3. Run all cells sequentially.
4. The dataset will be downloaded automatically using kagglehub.

### Local Environment

```bash
pip install -r requirements.txt
jupyter notebook FacialSkinDetection_Complete.ipynb
```

A GPU is recommended for training.

---

## 📦 Requirements

Main dependencies:

* tensorflow
* kagglehub
* scikit-learn
* matplotlib
* seaborn
* opencv-python
* pandas
* numpy

See `requirements.txt` for the complete list.

---

## 📁 Model Weights

Trained model weights are not included in this repository due to storage limitations.

The complete notebook is provided to reproduce all experiments and results.

---

## 👩‍💻 Contributor

**Radhika**

GitHub: @Radhika-789

GSSoC 2026 Contributor

---

## 📜 License

This project is contributed as part of the Deep Learning Simplified open-source repository under GSSoC 2026.
