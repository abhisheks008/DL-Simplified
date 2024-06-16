# Kidney Condition Classification

## 🎯 Goal
The main goal of this project is to accurately classify kidney conditions (Normal, Cyst, Tumor, Stone) using deep learning models. The purpose is to assist medical professionals in diagnosing kidney-related issues efficiently through automated image classification.

## 🧵 Dataset
The dataset used in this project is the CT-KIDNEY-DATASET, which can be found at [this link](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone). It contains a total of 12,000 images categorized into four classes: Normal, Cyst, Tumor, and Stone.

## 🧾 Description
This project involves the development and comparison of three deep learning architectures—VGG-like, CNN with spatial attention, and ResNet-like—to determine the most effective model for kidney condition classification. The models are trained, validated, and tested on a dataset of CT kidney images to identify the best performing architecture based on accuracy and other evaluation metrics.

## 🧮 What I had done!
1. **Dataset Preparation**:
    - Collected and split the dataset into training, validation, and test sets.
    - Applied data augmentation to enhance the training dataset.
    
2. **Model Development**:
    - Implemented three deep learning models: VGG-like, CNN with spatial attention, and ResNet-like.
    
3. **Model Training**:
    - Trained each model using the training dataset.
    - Used Early Stopping, Model Checkpoint, and ReduceLROnPlateau callbacks for efficient training.
    
4. **Model Evaluation**:
    - Evaluated the models using the validation dataset.
    - Compared the performance of the models based on accuracy, precision, recall, F1-score, and confusion matrices.
    
5. **Testing**:
    - Tested the final models on the test dataset to ensure robustness.
    - Visualized and analyzed the results to determine the best model.

## 🚀 Models Implemented
- **VGG-like Model**: Chosen for its simplicity and proven effectiveness in image classification tasks.
- **CNN with Spatial Attention**: Selected to enhance feature extraction and focus on important regions in the images.
- **ResNet-like Model**: Implemented for its capability to handle deep networks efficiently and prevent vanishing gradients.

## 📚 Libraries Needed
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-learn
- Splitfolders

## 📊 Exploratory Data Analysis Results
![EDA Results]
- Distribution of images across different classes.
- Sample images from each class.
- Data augmentation examples.

## 📈 Performance of the Models based on the Accuracy Scores
- **VGG-like Model**: Accuracy - X.XX%
- **CNN with Spatial Attention**: Accuracy - X.XX%
- **ResNet-like Model**: Accuracy - X.XX%

## 📢 Conclusion
The ResNet-like model achieved the highest accuracy of X.XX%, making it the best fit for classifying kidney conditions among the three developed models. This project demonstrates the effectiveness of deep learning models in medical image classification and highlights the potential of automated diagnosis tools in healthcare.

## ✒️ Your Signature
**Your Name**  
*GitHub: https://github.com/SayantikaLaskar 
*LinkedIn: https://www.linkedin.com/in/sayantika-laskar-098aa2250/