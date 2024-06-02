## **AI Generated vs Real Images Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images, on whether they were AI generated or real images with human background like paintings and pictures.

### 🧵 **Dataset**

The dataset consists of 2 subfolders each with a subdirectory leading to the images. Images have been reshaped to 224X224 pixels for modelling.

### 🧾 **Description**

The project deals with binary classification, classifying images into the two classes: AIArt or RealArt.

### 🧮 **What I had done!**

To achieve our goals, following were implemented:

- Images were loaded using keras.utils and normalized into the range (0 to 1).

- Images have been set to a fixed size of 224X224 pixels.

- Custom as well as pre-trained models were used for this task.

### 🚀 **Models Implemented**

models used:

- ResNet-50
- Xception
- VGG16
- CNN-Keras
- Inception

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Numpy

- Matplotlib

### 📊 **Exploratory Data Analysis Results**


- **Real Art**

<p align="center">
  <img src = "https://github.com/Arihant-Bhandari/DL-Simplified/blob/AI_vs_REAL/AI%20Generated%20vs%20Real%20Images%20Classification%20using%20DL/Images/85220_africa-21787_1920.rev.1600192341.jpg"> height="400px" width="400px" />
  <img src = "https://github.com/Arihant-Bhandari/DL-Simplified/blob/AI_vs_REAL/AI%20Generated%20vs%20Real%20Images%20Classification%20using%20DL/Images/beautiful-scenery-in-autumn-season-illustration-ai-generative-free-free-photo.jpg"> height="400px" width="400px" />
</p>

- **AI Art**

<p align="center">
  <img src = "https://github.com/Arihant-Bhandari/DL-Simplified/blob/AI_vs_REAL/AI%20Generated%20vs%20Real%20Images%20Classification%20using%20DL/Images/1WA1ZUTaiGV9YO5lVEPPFhA.png" height="400px" width="400px" />
  <img src = "https://github.com/Arihant-Bhandari/DL-Simplified/blob/AI_vs_REAL/AI%20Generated%20vs%20Real%20Images%20Classification%20using%20DL/Images/1000_F_563719058_JXnzcPV4GRpWqmF5sqnqmbJ7ow3ca3DS.jpg" height="400px" width="400px" />
</p>

- **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- **Inception-Resnet-V2**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- **DenseNet121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

Metrics:

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| DenseNet-121 | 76.03% | 0.4916 |
| inception | 76.71%  | 0.4543 | 
| CNN | 67.81% | 0.6443 |
| Inception-Resnet-V2 | 80.82% | 0.5000 |
| Xception | 75.34%  | 0.5466 | 
| VGG16 | 78.77% | 0.5400 |

### 📢 **Conclusion**

We conclude the following:

VGG16 and inception work well on the dataset.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
