## **MUSHROOM CLASSIFICATION USING DEEP LEARNING**

### 🎯 **Goal**

The objective of this project is to classify Mushrooms, as part of supervised learning to help recognise them.

### 🧵 **Dataset**

The Dataset consists of 2 sections, one which holds images of 9 catgeories of mushrooms and the other, of 2 more types to be used together with transfer learning from the model obtained from the first part.

The dataset is heavily varied, with some dark, some grayscaled as well as some truncated images. In addition, the classes themselves are heavily imbalanced.

### 🧾 **Description**

We focus on the first half, which is to create a model proficient in classifying mushrooms into 9 types.

### 🧮 **What I had done!**

To achieve our goals, following were implemented:

- A custom codebase to set in the dataset has been implemented as part of preprocessing.

- A cutom codebase to load data, by verifying images based on above has been setup to properly deal with images.

- A threshold of 300 images has been set to balance the classes.

- Images have been set to a fixed size of 224X224 pixels.

- Custom as well as pre-trained models were used for this task.

### 🚀 **Models Implemented**

models used:

- ResNet-50
- inception
- EfficientNet
- Xception
- VGG16
- Inception-ResNet-V2
- CNN-pytorch
- CNN-Keras
- CNN-Keras-Attention
- DenseNet121

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Pytorch

- Numpy

- os

- Matplotlib

### 📊 **Exploratory Data Analysis Results**

Mushrooms
<img src = 'https://github.com/abhisheks008/DL-Simplified/blob/main/Mushroom%20Classification%20using%20Deep%20Learning/Images/image%20visualization%20for%20mushroom%20classes.png'>

CNN-pytorch

<img src = 'https://github.com/abhisheks008/DL-Simplified/blob/main/Mushroom%20Classification%20using%20Deep%20Learning/Images/cnn%20stats.png'>

DenseNet121

<img src = 'https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_mushroom/Mushroom%20Classification%20using%20Deep%20Learning/Images/Densenet121%20Accuracy.png' style="display:inline-block;">
<img src = 'https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_mushroom/Mushroom%20Classification%20using%20Deep%20Learning/Images/Densenet121%20Loss.png' style="display:inline-block;">

CNN-keras-Attention

<img src = 'https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_mushroom/Mushroom%20Classification%20using%20Deep%20Learning/Images/CNN-Attention%20Loss.png' style="display:inline-block;">

<img src = 'https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_mushroom/Mushroom%20Classification%20using%20Deep%20Learning/Images/CNN-Attention%20Accuracy.png' style="display:inline-block;">

Inception

<img src = 'https://github.com/abhisheks008/DL-Simplified/blob/main/Mushroom%20Classification%20using%20Deep%20Learning/Images/indep%20stats.png'>

Xception

<img src = 'https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_mushroom/Mushroom%20Classification%20using%20Deep%20Learning/Images/Xception%20Accuracy.png' style="display:inline-block;">
<img src = 'https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_mushroom/Mushroom%20Classification%20using%20Deep%20Learning/Images/Xception%20Loss.png' style="display:inline-block;">

### 📈 **Performance of the Models based on the Accuracy Scores**

Metrics:

| Models | Accuracy | Loss (MAE[M] / Crossentropy[C]) |
|--------|---------------------|--------------------------|
| ResNet-50 | 22.22% | 2.0996(C) |
| inception | 63.41%  | 1.0985(C) | 
| CNN-pytorch | 39.69% | 0.1002(C) |
| CNN-Keras | 44.94% | 1.7207(C) |
| CNN-Keras-Attention | 55.55% | 1.4879(C) |
| DenseNet121 | 72.84% | 0.8877(C) |
| Xception | 65.19%  | 1.2220(C) | 
| EfficientNet | 13.59% | 1.0252(M) |
| Inception-ResNet-V2 | 64.69% | 1.1645(C) |
| VGG16 | 51.61% | 1.3962(C) |

### 📢 **Conclusion**

We conclude the following:

DenseNet121, Xception, Inception-ResNet-V2 and CNN-Keras-Attention work pretty well for the task, with DenseNet121 being the better choice of them all.

### ✒️ **Your Signature**

Original Contributor: Piyush Bhujbal [https://www.linkedin.com/in/piyush-bhujbal-637a621a5/]

README and Model enhanced by: Arihant Bhandari [https://github.com/Arihant-Bhandari]
