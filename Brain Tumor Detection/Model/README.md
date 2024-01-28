# BRAIN TUMOR DETECTION 🧠💻
## 🎯 Goal

The primary objective of this project is to develop Convolution models capable of determining whether an individual has a brain tumor or not. This prediction is based on the analysis of magnetic resonance imaging (MRI) scans of the brain. The project seeks to leverage advanced machine learning techniques to create a model that can effectively discern the presence or absence of a brain tumor within the intricate details captured by MRI images.

## 🧵 Dataset

Dataset Link: [Brain Tumor Detection Dataset](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection)

The dataset comprises approximately 3060 MRI images of the brain, categorized into:
- Non-Tumorous Images: 1500
- Tumorous Images: 1500
- Additional 60 images in the "pred" folder.

## 🧾 Description

This project aims to develop a model capable of accurately detecting the presence of a brain tumor in MRI images. The dataset is used for training and testing the models.

## 🧮 What I had done!

1. **Data Preprocessing:**
   - Load and explore the dataset.
   - Handle missing data and outliers.
   - Normalize and resize images.

2. **Train-Test Split:**
   - Split the dataset into training (80%) and testing (20%) sets.

3. **Model Training:**
   - Implement CNN (Convolutional Neural Network).
   - Utilize pre-trained models: VGG16 and RESNET 50.
   - Fine-tune models for brain tumor detection.

4. **Evaluation:**
   - Assess model performance on the test set.
   - Analyze and interpret the results.

## 🚀 Models Implemented

- **CNN (Convolutional Neural Network):**
  - Suitable for image classification tasks.
  
- **VGG16:**
  - Well-known for its simplicity and effectiveness.
  
- **RESNET 50:**
  - Addresses vanishing gradient problem with deep networks.

### Why these algorithms?
Chose these models due to their effectiveness in image classification tasks and availability of pre-trained weights for transfer learning.

## 📚 Libraries Needed

- TensorFlow
- Keras
- Scikit-learn
- Matplotlib
- Pandas
- Numpy

## 📊 Exploratory Data Analysis Results

### TUMOROUS BRAIN MRI IMAGES
<div style="display: grid; grid-template-columns: repeat(3, 200px); gap: 5px; margin-bottom: 20px;">
  <img src="https://user-images.githubusercontent.com/72621930/219711653-f89efe73-84ae-4b76-aae3-4f175776b767.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219716592-507e25fc-3aa3-40eb-8a88-73ec99d56914.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219711854-6e64f8c8-1a43-469f-ac7e-57cff0c5ce4a.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219712189-12c1172f-5c4f-40b0-9e13-f7e709e9850c.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219712231-6a43351d-747a-4cca-9755-0261cda9a834.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219720376-70ecb711-a8c8-496b-be3b-f1f5b3d00563.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219720379-e72a9146-04e1-41bb-acf3-e82e347019ab.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219720393-1e9ea66e-dbce-4d70-a04e-5b4ee1bbec9f.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219720422-a400acf6-1ce4-47c5-81d2-faabfed37317.jpg" width="200" height="200">
</div>

### SOME OF THE NON-TUMOROUS BRAIN MRI IMAGES
<div style="display: grid; grid-template-columns: repeat(3, 200px); gap: 5px;">
  <img src="https://user-images.githubusercontent.com/72621930/219717582-a8399573-1365-41b9-881d-34962845d91f.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219717613-839ba23c-4cbe-4273-95a9-78e1205384ff.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219717624-9b7aeb0b-4c00-44e4-afe6-0c2f5c8500ac.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219717644-0a572148-ae31-4cae-ab1e-8feacc417a03.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219717672-6a4f85a5-d68b-458a-aeeb-351b7d8e14ee.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219722662-fb86a286-5b53-4874-9be3-1dee25e550b5.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219722703-c45da0bb-c5e9-4fb0-a7c7-5359b6d89790.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219722807-fd2786d6-ddf2-4d12-97c2-ffdbfc5bfe81.jpg" width="200" height="200">
  <img src="https://user-images.githubusercontent.com/72621930/219722814-f0b7ec73-981f-4dcc-8be4-e9afe831fb72.jpg" width="200" height="200">
</div>

## 📈 Performance of the Models based on Accuracy Scores
| ![CNN Plot](../Images/cnn_plot.png) | ![RESNET50 Plot](../Images/resnet50.png) | ![VGG Plot](../Images/vgg_plot.png) |
|---|---|---|

- **CNN:**
  - Training Accuracy: 95%
  - Test Accuracy: 92%

- **VGG16:**
  - Training Accuracy: 97%
  - Test Accuracy: 94%

- **RESNET 50:**
  - Training Accuracy: 98%
  - Test Accuracy: 96%

## 📢 Conclusion

The models, especially RESNET 50, performed well in detecting brain tumors from MRI images. The choice of model can depend on the trade-off between computational complexity and accuracy.

## ✒️ Your Signature

Abhilash S Bharadwaj 📌

[Abhilash1781](https://github.com/Abhilash1781) 🌐
