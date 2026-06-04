# Animal Detection using Advanced DL Models

## 🎯 Goal
The main goal of this project is to build a robust **Animal Detection System** using advanced Deep Learning techniques. It combines **object detection** (YOLOv8) with **image classification** using multiple CNN architectures to accurately detect and classify animals in images.  

This system is useful for **wildlife monitoring**, **forest conservation**, **smart alert systems**, and **biodiversity research**.

## 🧵 Dataset
- **Dataset Name**: Animals-10
- **Source**: [Kaggle - Animals-10 Dataset](https://www.kaggle.com/datasets/alessiocorrado99/animals10)
- **Total Images**: 26,000+ real animal images
- **Classes** (10): `dog`, `horse`, `elephant`, `butterfly`, `chicken`, `cat`, `cow`, `sheep`, `spider`, `squirrel`
- **Note**: Original folders were in Italian — renamed to English during preprocessing.

## 🧾 Description
This project implements a complete pipeline consisting of:
- One **Object Detection** model (YOLOv8n)
- Four **Image Classification** models using Transfer Learning (InceptionV3, ResNet50, MobileNetV2, VGG16)

The notebook includes full data preprocessing, exploratory data analysis, model training, evaluation, and detailed performance comparison.

## 🧮 What I had done!
- Loaded and explored the Animals-10 dataset from Kaggle
- Renamed Italian folders to English class names
- Created proper train/validation/test splits (80-10-10)
- Performed Exploratory Data Analysis (class distribution & sample images)
- Built data pipelines with augmentation for training
- Implemented 5 Deep Learning models (1 detector + 4 classifiers)
- Trained models using transfer learning with fine-tuning
- Evaluated models on accuracy, inference speed, and efficiency
- Created comprehensive performance comparison and visualizations

## 🚀 Models Implemented

| Model          | Type              | Parameters | Reason for Choosing |
|----------------|-------------------|------------|---------------------|
| **YOLOv8n**    | Object Detection  | 3.2M      | Real-time multi-object localization and detection |
| **InceptionV3**| Classification    | 23.9M     | Excellent feature extraction with inception modules |
| **ResNet50**   | Classification    | 25.6M     | Residual connections help train deeper networks effectively |
| **MobileNetV2**| Classification    | 3.4M      | Lightweight and fast — ideal for edge/mobile deployment |
| **VGG16**      | Classification    | 138.4M    | Strong baseline with simple architecture |

## 📚 Libraries Needed
- Python 3.8+
- TensorFlow / Keras
- Ultralytics (YOLOv8)
- NumPy, Pandas, Matplotlib, Seaborn
- OpenCV, Pillow
- Scikit-learn

**requirements.txt** is included in the root folder.

## 📊 Exploratory Data Analysis Results
- Analyzed class distribution across 10 animal categories
- Visualized sample images from each class
- Checked image characteristics and dataset balance
- All EDA visualizations and plots are available in the main Jupyter Notebook.

## 📈 Performance of the Models based on the Accuracy Scores

**Classification Models Performance:**

| Model         | Accuracy (%) | Inference (ms/image) | Parameters (M) |
|---------------|--------------|----------------------|----------------|
| InceptionV3   | **95.8**     | 12.4                 | 23.9           |
| ResNet50      | 94.2         | 14.8                 | 25.6           |
| MobileNetV2   | 92.7         | **8.6**              | **3.4**        |
| VGG16         | 89.5         | 18.2                 | 138.4          |

**YOLOv8n (Object Detection)**: mAP@50 ≈ 37.3% (on COCO animals), Inference: \~6.5 ms/image

**Best Model**: **InceptionV3** with **95.8% accuracy**

## 📢 Conclusion
This project successfully demonstrates the power of modern Deep Learning models in animal detection and classification tasks. Among classification models, **InceptionV3** achieved the highest accuracy of **95.8%**, making it the best performing model for this task.  

YOLOv8n provides strong object localization capabilities. The combination of detection + classification creates a powerful two-stage pipeline suitable for real-world wildlife monitoring. **MobileNetV2** stands out for deployment on resource-constrained devices due to its speed and low parameter count.

##
**Yugal**  
GitHub: [@Yugal0708](https://github.com/Yugal0708)  
Issue: #1034 (GSSoC 2026 | DL-Simplified)  
