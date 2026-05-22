## **AI GENERATED FRUITS AND REAL FRUITS CLASSIFICATION USING IMAGE PROCESSING**

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Computer%20Vision-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Models-ML%20%26%20DL-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Dataset-Kaggle-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Best%20Accuracy-100%25-brightgreen?style=for-the-badge" />
</p>

---

### 🎯 **Goal**

The aim of this project is to **identify and differentiate** between images of **real fruits** and **AI-generated fruits** using Image Processing and Machine Learning / Deep Learning methods.

**Real-world Significance:** As AI-generated imagery becomes increasingly photorealistic, the ability to detect synthetic content is critical — for food supply chain integrity, e-commerce product verification, and combating misinformation. This project demonstrates that even classical ML models can achieve near-perfect accuracy at this task with proper preprocessing.

---

### 🧵 **Dataset**

**Source:** Kaggle — [Dataset of AI Generated Fruits and Real Fruits](https://www.kaggle.com/datasets/osmankagankurnaz/dataset-of-ai-generated-fruits-and-real-fruits)

| Property | Details |
|---|---|
| Total Images | 306 |
| Classes | AI-Generated Apples, Real Apples |
| AI Generated Images | 150 |
| Real Images | 156 |
| Apple Types | Red, Green |
| Shot Types | Side shots, Top shots, various angles |
| Format | `.jpg` |

---

### 🧾 **Description**

This project tackles the growing challenge of distinguishing AI-generated visual content from real photographs — specifically applied to fruit images (apples). The dataset consists of 306 images of apples photographed from various angles, mixed with AI-generated counterparts.

Images are preprocessed (normalized to [0,1], resized to 128×128, reshaped) and trained on **7 models** spanning classical ML (LDA, SVM) and deep learning (VGG16, ResNet50), with PCA used for dimensionality reduction. Predictions are made on input images and model accuracies are compared to identify the best-performing approach.

---

### 🧮 **What I had done!**

1. **Loaded image paths** for both AI and Real categories using `glob`
2. **Visualized class distribution** — bar chart confirming 150 AI vs 156 Real images (near-balanced dataset)
3. **Displayed sample images** — 4 AI vs 4 Real apple images side-by-side for qualitative comparison
4. **Feature extraction & preprocessing:**
   - Normalized pixel values to [0, 1]
   - Resized all images to 128×128×3
   - Reshaped into flat arrays (128×384) for ML models
5. **Standardized data** using `StandardScaler` (zero mean, unit variance)
6. **Split data** into training (80%) and testing (20%) sets
7. **Applied PCA** — reduced to 200 components; cumulative variance plot shows ~39 components capture 90% of variance
8. **Trained LDA** classifier and evaluated on train/test sets
9. **Trained SVM** with 3 kernels (Linear, Polynomial degree-2, RBF) — computed Accuracy, Precision, Recall, F1-score, and Confusion Matrices
10. **Built CNN (VGG16)** — frozen ImageNet weights + Flatten + Dense(2, softmax); 10 epochs; plotted training curves
11. **Built CNN (ResNet50)** — frozen weights + Conv2D(64) + MaxPool + Dense(64) + Dropout(0.4) + Dense(2, softmax); 25 epochs; plotted training curves
12. **Made predictions** on sample input images using every trained model
13. **Saved all models** using `joblib`
14. **Compared all model accuracies** to determine the best performer

---

### 🚀 **Models Implemented**

| # | Model | Type | Why This Model? |
|---|-------|------|-----------------|
| 1 | **PCA** | Dimensionality Reduction | Compresses high-dimensional image data; cumulative variance plot reveals how many components capture meaningful signal |
| 2 | **LDA** | Classical ML | Maximizes class separability in lower-dimensional space — effective and lightweight for binary classification |
| 3 | **SVM – Linear Kernel** | Classical ML | Strong binary classification baseline; handles high-dimensional feature spaces well |
| 4 | **SVM – Polynomial Kernel** | Classical ML | Captures non-linear relationships via polynomial feature mappings (degree=2) |
| 5 | **SVM – RBF Kernel** | Classical ML | Most flexible SVM variant; maps data to infinite-dimensional space for complex decision boundaries |
| 6 | **CNN – VGG16** | Deep Learning (Transfer) | Pre-trained on ImageNet; strong feature extractor for image classification with minimal custom training |
| 7 | **CNN – ResNet50** | Deep Learning (Transfer) | Residual connections prevent vanishing gradients; captures richer hierarchical visual features |

**VGG16 Architecture:**
```
VGG16 (frozen ImageNet weights, input: 128×128×3)
  └── Flatten
  └── Dense(2, activation='softmax')
Optimizer: Adam | Loss: categorical_crossentropy | Epochs: 10
```

**ResNet50 Architecture:**
```
ResNet50 (frozen weights, input: 128×128×3)
  └── Conv2D(64, 3×3, relu)
  └── MaxPooling2D(2×2)
  └── Flatten → Dense(64, relu) → Dropout(0.4)
  └── Dense(2, softmax)
Optimizer: Adam | Loss: binary_crossentropy | Epochs: 25
```

---

### 📚 **Libraries Needed**

- `numpy` — array manipulation and numerical operations
- `pandas` — data handling
- `matplotlib` — plotting visualizations
- `seaborn` — enhanced statistical plots
- `scikit-learn` — ML models (PCA, LDA, SVM), preprocessing, metrics
- `scikit-image` (`skimage`) — image loading and resizing
- `opencv-python` (`cv2`) — image processing and RGB conversion
- `tensorflow` / `keras` — deep learning (VGG16, ResNet50)
- `Pillow` (PIL) — image loading for the SVM pipeline
- `joblib` — saving and loading trained models

---

### 📊 **Exploratory Data Analysis Results**

#### 1. Class Distribution

<!-- DRAG AND DROP: Class_Distribution_Bar_Chart.png here --><img width="684" height="484" alt="Class Distribution Bar Chart" src="https://github.com/user-attachments/assets/98745a98-2de6-4127-9e1f-5f5d5499855d" />



> The dataset contains **150 AI-generated** and **156 Real** apple images — a near-balanced binary classification dataset requiring no oversampling techniques.

---

#### 2. Sample Images — AI Generated vs Real

<!-- DRAG AND DROP: Sample_Images_Grid__AI_vs_Real_side_by_side_.png here --><img width="1383" height="621" alt="Sample Images Grid (AI vs Real side by side)" src="https://github.com/user-attachments/assets/48b2cef4-47be-4bee-a55f-72cdeebc03f9" />


> AI-generated images have smoother, more uniform textures and slightly unnatural lighting. Real images show natural variation, skin imperfections, and realistic shadows.

---

#### 3. PCA — Cumulative Explained Variance

<!-- DRAG AND DROP: PCA_Cumulative_Variance_Plot.png here --><img width="860" height="479" alt="PCA Cumulative Variance Plot" src="https://github.com/user-attachments/assets/bbc00fdf-aa6f-4a50-b652-423fa9e38530" />

> Approximately **39 principal components** explain 90% of the dataset variance (marked by dashed lines), confirming significant redundancy in raw pixel data and validating the use of classical ML on compressed features.

---

#### 4. SVM — Confusion Matrices (Test Set)

<!-- DRAG AND DROP: SVM_confusion_matrices.png here --><img width="1319" height="393" alt="SVM confusion matrices" src="https://github.com/user-attachments/assets/b6b467f9-5b40-41af-9136-690c4ad81414" />


> All three SVM kernels show minimal misclassifications. The **RBF kernel** achieves a perfect confusion matrix with **zero false positives and zero false negatives**.

---

#### 5. CNN Training Curves

**VGG16:**

<!-- DRAG AND DROP: VGG16_Training_Accuracy___Loss_Curves.png here --><img width="1183" height="393" alt="VGG16 Training Accuracy   Loss Curves" src="https://github.com/user-attachments/assets/02e05c4b-8cc8-452c-ac8a-c44c37a069ef" />


> VGG16 reaches **100% accuracy from epoch 2 onwards**. Loss drops steeply from 0.49 to near-zero — characteristic of transfer learning with well-learned ImageNet features.

---

**ResNet50:**

<!-- DRAG AND DROP: ResNet_Training_Accuracy___Loss_Curves.png here --><img width="1183" height="393" alt="ResNet Training Accuracy   Loss Curves" src="https://github.com/user-attachments/assets/e2c19b33-b435-4511-b0d7-35af961416d7" />

> ResNet50 achieves **100% training accuracy** with continuously decreasing loss across 10 epochs, demonstrating effective learning via residual connections.

---

### 📈 **Performance of the Models based on the Accuracy Scores**

| Model | Training Accuracy | Test Accuracy | Precision | Recall | F1-Score |
|-------|:-----------------:|:-------------:|:---------:|:------:|:--------:|
| LDA | 100% | **91.80%** | — | — | — |
| SVM (Linear Kernel) | 100% | **98.36%** | 0.967 | 1.00 | 0.983 |
| SVM (Polynomial Kernel) | 100% | **98.36%** | 0.967 | 1.00 | 0.983 |
| SVM (RBF Kernel) | 100% | **100%** ✅ | 1.00 | 1.00 | 1.00 |
| CNN – VGG16 | 70.49% → 100% | **~100%** | — | — | — |
| CNN – ResNet50 | 72.20% → 100% | **~100%** | — | — | — |

---

### 📢 **Conclusion**

This project successfully classifies apple images as AI-generated or real using both classical ML and deep learning approaches.

- **Best model: SVM (RBF Kernel)** — achieves **100% test accuracy** with zero misclassifications at the lowest computational cost, making it the recommended model for deployment.
- **VGG16 and ResNet50** both converge to ~100% accuracy via transfer learning but require significantly more compute.
- **LDA** provides a solid 91.80% accuracy baseline with near-zero computation — suitable for resource-constrained environments.
- Classical ML proved highly competitive with deep learning for this binary image classification task when features are well-preprocessed via PCA.

---

### ✒️ **Your Signature**

**Project by:** <br>
Name: Titiksha Agrawal   <br>
GitHub: https://github.com/AgrawalTitiksha   <br>
LinkedIn: https://www.linkedin.com/in/titiksha-agrawal-056004251/   <br>

**README Enhanced by:**   <br>
Name: Niladri Saikia   <br>
GitHub: https://github.com/niladrisaikia27   <br>
