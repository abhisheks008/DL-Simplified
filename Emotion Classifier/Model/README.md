## **Emotion Classification**

### 🎯 **Goal**
The main objective of this project is to classify emotions in textual data using various deep learning models including Convolutional Neural Networks (CNN), Artificial Neural Networks (ANN), and Recurrent Neural Networks (RNN).

### 🧵 **Dataset**
The dataset used in this project is a labeled dataset containing text comments and corresponding emotions such as 'joy' and 'fear'.

### 🧾 **Description**

This project involves building and comparing different neural network models to classify emotions in text comments. It includes data preprocessing, model creation, training, evaluation, and visualization of results.

### 🧮 **What I had done!**

1. **Data Preprocessing**:
   - Imported necessary libraries for data manipulation, visualization, and model training.
   - Loaded the dataset and performed basic exploratory data analysis.
   - Cleaned the text data by removing special characters and converting text to lowercase.
   - Split the dataset into training and testing sets.

2. **Exploratory Data Analysis**:
   - Visualized the distribution of emotions and various text features like word count, character count, and average word length.
   - Identified the top 20 most common words in the dataset.

3. **Text Tokenization and Padding**:
   - Tokenized the text data and converted it into sequences of integers.
   - Padded the sequences to ensure uniform input length for the models.
   - Created an embedding matrix using Word2Vec for word embeddings.

4. **Model Creation and Training**:
   - **CNN Model**: Built a Convolutional Neural Network with embedding, convolutional, pooling, flatten, and dense layers.
   - **ANN Model**: Built an Artificial Neural Network with embedding, flatten, and dense layers.
   - **RNN Model**: Built a Recurrent Neural Network using LSTM layers.
   - Compiled and trained each model on the training dataset.

5. **Model Evaluation**:
   - Evaluated each model's performance using the test dataset.
   - Plotted training and validation accuracy and loss curves for each model.

6. **Comparison**:
   - Compared the accuracy of the CNN, ANN, and RNN models.

### 🚀 **Models Implemented**

#### Convolutional Neural Network (CNN):
- Embedding layer with pre-trained word embeddings.
- Convolutional and pooling layers to capture local patterns.
- Dense layers for final classification.
- Compiled with binary cross-entropy loss and Adam optimizer.

#### Artificial Neural Network (ANN):
- Embedding layer with pre-trained word embeddings.
- Dense layers with ReLU activation for feature extraction.
- Output layer with sigmoid activation for binary classification.
- Compiled with binary cross-entropy loss and Adam optimizer.

#### Recurrent Neural Network (RNN):
- LSTM layer to capture temporal dependencies.
- Global Max Pooling layer for dimensionality reduction.
- Dense layer for final classification.
- Compiled with sparse categorical cross-entropy loss and Adam optimizer.

### 📚 **Libraries Needed**

- TensorFlow and Keras: For building and training deep learning models.
- NumPy and Pandas: For numerical operations and data manipulation.
- Matplotlib and Seaborn: For data visualization.
- scikit-learn: For dataset splitting and evaluation.
- NLTK: For text preprocessing and tokenization.
- Gensim: For training Word2Vec model.

### 📊 **Exploratory Data Analysis Results**

Visualizations include:
- Distribution of emotions.
- Word count, character count, and average word length distributions.
- Top 20 most common words.

### 📈 **Performance of the Models**

- **CNN Accuracy**: 95.94%
- **ANN Accuracy**: 94.21%
- **RNN Accuracy**: 94.44%

### 📢 **Conclusion**

In conclusion, this project successfully implemented and trained different neural network models for emotion classification in text data. Among the models, the CNN achieved the highest accuracy. The models demonstrated good performance in capturing the patterns and nuances in the text data to accurately classify emotions.

### ✒️ **Your Signature**

[Manish Kumar Gupta]