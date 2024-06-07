# **Almond Varieties Image Classification**

### 🎯 Goal
The primary goal of this project is to develop an accurate and efficient image classification system capable of distinguishing between different varieties of almonds. By leveraging advanced deep learning models, the project aims to provide a robust solution for the automated identification of almond varieties, which can be beneficial for various applications in agriculture, food industry, and quality control.

### Purpose
The purpose of this project includes the following:

1. Automation of Almond Classification: To automate the process of identifying almond varieties, reducing the need for manual inspection and classification.
2. Enhancing Accuracy: To achieve high accuracy in classification using state-of-the-art deep learning models (InceptionV3, VGG19, and ResNet50), ensuring reliable identification of almond types.
3. Efficiency in Processing: To provide a fast and efficient method for processing large volumes of almond images, making it scalable for industrial applications.
4. Support for Agricultural Research: To contribute to agricultural research by providing a tool that can help in studying and monitoring different almond varieties.
5. Quality Control: To aid in quality control processes by accurately identifying and sorting almond varieties, ensuring product consistency and quality in the food industry.
Through this project, we aim to demonstrate the practical application of deep learning models in agricultural and industrial contexts, showcasing how technology can enhance productivity and accuracy in classification tasks.

### 🧵 Dataset : https://www.kaggle.com/datasets/mahyeks/almond-varieties/data

### 🧾 Description
This project focuses on developing a sophisticated image classification system to identify different varieties of almonds using deep learning techniques. The system leverages three state-of-the-art convolutional neural network (CNN) architectures: InceptionV3, VGG19, and ResNet50, each known for their robustness and high performance in image recognition tasks.

**Key Features**
Model Implementations: Utilizes three prominent CNN models:

- InceptionV3: Known for its efficiency and factorized convolutions, reducing computational cost while maintaining high accuracy.
- VGG19: Characterized by its deep yet simple architecture, using 3x3 convolutional layers to achieve excellent image recognition performance.
- ResNet50: Employs residual learning to train very deep networks, addressing the vanishing gradient problem and achieving high accuracy.

### 🚀 Models Implemented
- **InceptionV3**: Chosen for its balance between efficiency and accuracy, making it suitable for large-scale image classification with moderate computational resources.
- **VGG19**: Selected for its simplicity and high performance in tasks requiring detailed feature extraction, making it a strong baseline model.
- **ResNet50**: Opted for its ability to train very deep networks without suffering from vanishing gradients, allowing for the capture of intricate image details necessary for accurate classification of almond varieties.

### 📚 Libraries Needed
- TensorFlow: For building and training deep learning models.
- Keras: For simplifying the creation and training of neural networks.
- NumPy: For numerical computations and array operations.
- Pandas: For data manipulation and analysis.
- Matplotlib: For plotting and visualizing data.
- Pillow: For image processing tasks.

### 📊 Exploratory Data Analysis Results
A total of 1556 images of the four varieties were captured.
![Screenshot 2024-06-07 203324](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/baa18e75-2a03-4905-994d-cfb1ee128b46)

### 📈 Performance of the Models based on the Accuracy Scores

**InceptionV3 Performance**
![InceptionV3_results](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/824d4893-3d6f-404c-8094-48ae64f888cc)

**VGG19 Performance**
![VGG19_results](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/e648c009-1a20-4662-9f5a-72d39a88be3c)

**ResNet50 Performance**
![ResNet_results](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/709f2625-7d23-499b-9af9-71014c1c063f)

### 📢 Conclusion
This project successfully demonstrates the use of advanced deep learning models to classify different varieties of almonds. By leveraging InceptionV3, VGG19, and ResNet50, the project highlights the effectiveness and performance of these architectures in image classification tasks.

### Accuracy Results
1. InceptionV3
	- Training Accuracy: 99.75%
	- Validation Accuracy: 99.65%
2. VGG19
	- Training Accuracy: 95.71%
	- Validation Accuracy: 98.95%
3. ResNet50
	- Training Accuracy: 48.91%
	- Validation Accuracy: 59.03%

**Best Fitted Model**
Based on the accuracy scores, InceptionV3 is the best-fitted model for this project, achieving the highest training and validation accuracy. This indicates that InceptionV3 is most effective for classifying almond varieties with excellent precision.

- InceptionV3: Best performance with near-perfect accuracy, suitable for deployment.
- VGG19: High accuracy but slightly lower than InceptionV3, still very reliable.
- ResNet50: Underperformed in this context, likely due to training issues or data requirements.
In conclusion, InceptionV3 is recommended for practical applications in almond variety classification due to its superior accuracy and efficiency.

## ✒️ Contributor
### Name : Abhijeet Kaithwas
LinkedIn : https://www.linkedin.com/in/abhijeet-kaithwas-1866b5256/
