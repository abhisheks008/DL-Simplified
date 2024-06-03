## **Intrusion Detection using Neural Network**

### 🎯 **Goal**
The primary objective of this project is to develop an Intrusion Detection System (IDS) capable of distinguishing between normal network traffic and various types of attacks using machine learning models. The dataset used for training and evaluation is the KDD Cup 1999 dataset, a widely used benchmark dataset for IDS research.

### 🧵 **Dataset**
The dataset, sourced from the KDD Cup 1999 competition, contains network connection records captured over several weeks from a university department's local area network (LAN). It includes both normal and malicious activities, simulated through different types of attacks such as denial of service (DoS), user to root (U2R), remote to local (R2L), and probe attacks.

### 🧾 **Description**

This project involves preprocessing the dataset, performing exploratory data analysis (EDA), training multiple machine learning models, and comparing their performance. The models used include Artificial Neural Networks (ANN), Deep Neural Networks (Deep NN), and Convolutional Neural Networks (CNN).

### 🧮 **What I had done!**

1. **Data Preprocessing**:
   - Imported necessary libraries for data manipulation, visualization, and model training.
   - Loaded the KDD Cup 1999 dataset and performed basic preprocessing steps.
   - Mapped categorical features to numerical values and added attack type labels.

2. **Exploratory Data Analysis (EDA)**:
   - Visualized the distribution of protocol types, services, flags, and attack types.
   - Investigated correlations between different features using heatmap visualization.

3. **Feature Engineering**:
   - Removed highly correlated features to improve model performance.

4. **Model Training**:
   - Trained three types of models: ANN, Deep NN, and CNN.
   - Compiled and trained each model using the preprocessed dataset.

5. **Model Evaluation**:
   - Evaluated the performance of each model using accuracy metrics.
   - Plotted training and validation accuracy/loss curves for visualization.

6. **Comparison**:
   - Compared the accuracy of ANN, Deep NN, and CNN models to determine the most effective approach for intrusion detection.

### 🚀 **Models Implemented**

#### Artificial Neural Network (ANN):
- Configured with multiple dense layers and ReLU activation.
- Trained with sparse categorical cross-entropy loss and Adam optimizer.

#### Deep Neural Network (Deep NN):
- Designed with several densely connected layers, gradually reducing dimensionality.
- Utilized dropout layers for regularization to prevent overfitting.
- Trained using sparse categorical cross-entropy loss and Adam optimizer.

#### Convolutional Neural Network (CNN):
- Constructed with convolutional and max-pooling layers to capture local patterns.
- Incorporated dropout regularization to prevent overfitting.
- Trained with sparse categorical cross-entropy loss and Adam optimizer.

### 📚 **Libraries Needed**

- TensorFlow and Keras: For building and training machine learning models.
- NumPy and Pandas: For data manipulation and numerical operations.
- Matplotlib and Seaborn: For data visualization.
- Scikit-learn: For dataset splitting, evaluation, and feature engineering.

### 📊 **Exploratory Data Analysis Results**

- Attack Type Distribution
![Attack Type Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/attack_type.png)
- Flag Distribution
![Flag Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/flag.png)
- Logged-in Users Distribution
![Logged-in Users Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/logged_in.png)
- Protocol Type Distribution
![Protocol Type Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/protocol_type.png)

- Service Distribution
![Service Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/service.png)

- Target Distribution
![Target Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/target.png)

- Correlation Heatmap
![Correlation Heatmap](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/correlation_heatmap.png)


### 📈 **Performance of the Models**

- **ANN Accuracy**: 99.89%
- **Deep NN Accuracy**: 99.84%
- **CNN Accuracy**: 99.83%

<br>


- ANN

![ANN Accuracy](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/ann_accuracy.png)
![ANN Loss](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/ann_loss.png)

- DNN
  
![Deep NN Accuracy](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/deep_accuracy.png)
![Deep NN Loss](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/deep_loss.png)

- CNN
  
![CNN Accuracy](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/cnn_accuracy.png)
![CNN Loss](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/cnn_loss.png)

### 📢 **Conclusion**

In conclusion, this project successfully developed an Intrusion Detection  using deep learning models trained on the KDD Cup 1999 dataset. 
![Model Comparison](https://github.com/manishh12/DL-Simplified/blob/main/Intrusion%20Detection/Images/model_comparison.png)


### ✒️ **Your Signature**

[Manish Kumar Gupta]
