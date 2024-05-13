## 🌈 Colour Detection using DL (#527)


## 💡 Goal

In this project, we'll delve into the fascinating world of color detection using Deep Learning techniques. The goal is to accurately identify ten different colors from images.

## 📊 Dataset Exploration

We've sourced our dataset from [Color Dataset for Color Recognition](https://www.kaggle.com/datasets/adikurniawan/color-dataset-for-color-recognition). This dataset contains 10 class of color, each color class contains 25 images.

## 🧾 Description
The project aims to create a color detection system using deep learning techniques. It involves identifying ten different colors from images. The dataset used for training and testing contains images labeled with various colors. 

## 🧮 What I had done!
### 🔍 Data Preprocessing

Ensuring uniformity in image shapes and enhancing color contrast to extract meaningful features for our models. Also processed labels into probability distribution arrays for multi-class classification.

### 🧠 Model Selection

We're employing the latest DL architectures for our color detection task:

1. **Convolutional Neural Network (CNN)**: Known for its process in image classification.
2. **VGG16**: A state-of-the-art architecture with deep convolutional layers.
3. **ResNet15V2**: Harnessing the power of residual networks for accurate color recognition.
4. **CNN with Attention**: CNN with an overhead Attention allowing context into training and using ELU as activation and NADAM as optimizer function to converge faster.

## Models Implemented

### CNN Model

**Description:**
- Utilized a traditional Convolutional Neural Network (CNN) architecture.
- CNNs are well-suited for image classification tasks due to their ability to learn spatial hierarchies.

### VGG16 Model

**Description:**
- Employed the VGG16 architecture, known for its simplicity and effectiveness.
- VGG16 consists of 16 convolutional layers and is capable of capturing intricate features in images.

### ResNet50 Model

**Description:**
- Implemented the ResNet50 architecture, featuring residual connections.
- ResNet50's residual blocks mitigate the vanishing gradient problem, enabling training of deeper networks.

### CNN Model with Attention

**Description:**
- Applied overhead attention to the CNN architecture for faster convergence.
- USed robust functions to counter dying ReLU problem like ELU activation and using NADAM optimizer.

##  Libraries needed
Here are the libraries needed for this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- seaborn==0.11.2
- Pillow==8.4.0
- opencv-python==4.5.3.56
- keras==2.6.0
- tensorflow==2.6.0
- scikit-learn==0.24.2

### Exploratory data analysis results

### CNN Model
![CNN Model](https://github.com/abhisheks008/DL-Simplified/blob/main/Colour%20Detection%20using%20DL/Images/cnn%202.jpg)

### VGG16 Model
![VGG16 Model](https://github.com/abhisheks008/DL-Simplified/blob/main/Colour%20Detection%20using%20DL/Images/vgg16%202.jpg)

### ResNet50 Model
![ResNet16 Model](https://github.com/abhisheks008/DL-Simplified/blob/main/Colour%20Detection%20using%20DL/Images/res%202.jpg)

### CNN with Attention Model
![CNN with Attention](https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_colour_detect/Colour%20Detection%20using%20DL/Images/cnn_attention.png)

## 📈 Performance Evaluation

Let's visualize the accuracy scores of our models:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN        | 90%      | 0.326   |
| VGG16      | 82.5%    | 0.154   |
| ResNet50   | 87.5%    | 0.987   |
| CNN (Attention)   | 94%    | 0.193   |

## 🚀 Conclusion

1. **CNN Model with Attention**: With an accuracy of 94% and a low loss of 0.193, it's the clear winner in color detection.
2. **CNN Model**: With an accuracy of 90% and a low loss of 0.326, it's just falls short in color detection.
3. **VGG16 Model**: While respectable at 82.5% accuracy, it falls short compared to the CNN model.
4. **ResNet50 Model**: Despite its 87.5% accuracy, its higher loss indicates potential overfitting.

In conclusion, the CNN model with Attention emerges as the champion in accurately detecting colors from images.

## Your Signature
Model enhanced by: Arihant Bhandari[https://github.com/Arihant-Bhandari]
README enhanced by: Jahnvi sahni[https://github.com/jahnvisahni31]