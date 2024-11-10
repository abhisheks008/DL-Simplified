## **Hate Speech Detection**

### 🎯 **Goal**

The main goal of the project was to develop a deep learning model that accurately identifies and classifies hate speech in text data and to help identify and filter harmful language, promoting safer and more respectful online interactions.

### 🧵 **Dataset**

The dataset is taken from CrowdFlower - https://data.world/crowdflower/hate-speech-identification

### 🧾 **Description**

This project focuses on detecting hate speech in text using deep learning techniques. It involves preprocessing text data, training a neural network model, and evaluating its performance in classifying content as either hate speech or non-hate speech. The model aims to enhance online content moderation by identifying harmful language effectively, contributing to safer digital spaces.

### 🧮 **What I had done!**

1. **Data Loading**: Import the labeled text dataset.
2. **Preprocessing**: Clean text by removing noise, tokenizing, and normalizing.
3. **EDA**: Analyze class distribution and visualize data patterns.
4. **Model Building**: Create a neural network with embedding and LSTM layers.
5. **Training**: Train the model with a split of training and validation data.
6. **Evaluation**: Assess performance using metrics like accuracy and F1-score.
7. **Visualization**: Plot accuracy and loss to check model performance.
8. **Prediction**: Use the model to classify new text as hate speech or non-hate speech.

### 🚀 **Models Implemented**

The project uses an LSTM (Long Short-Term Memory) model with an embedding layer to detect hate speech. LSTM was chosen because it effectively captures the context and long-term dependencies in sequential text data, making it well-suited for understanding language patterns. The embedding layer helps convert words into dense vectors, enhancing the model's ability to grasp semantic relationships, while a final dense layer with a sigmoid activation performs binary classification of the text.

### 📚 **Libraries Needed**

Here are all the libraries used in this project:

1. **NumPy**: For numerical operations and array handling.
2. **Pandas**: For data manipulation and analysis.
3. **Matplotlib**: For creating visualizations and plots.
4. **Seaborn**: For statistical data visualization.
5. **NLTK (Natural Language Toolkit)**: For text preprocessing tasks like tokenization and stopword removal.
6. **Scikit-learn**: For data splitting, metrics evaluation, and preprocessing utilities.
7. **TensorFlow/Keras**: For building and training the deep learning model.
8. **re (Regular Expressions)**: For text cleaning and preprocessing.
9. **String**: For handling text processing tasks.

### 📊 **Exploratory Data Analysis Results**
![model_deployment_01](https://github.com/user-attachments/assets/1c8cb248-9ff1-4dd3-af0f-f00e080854f9)
![model_deployment_02](https://github.com/user-attachments/assets/341dab93-3293-4f2e-9a8f-1464a2b4a57a)


### 📈 **Performance of the Models based on the Accuracy Scores**

The project used an **LSTM (Long Short-Term Memory) Network** as the main algorithm. It achieved an accuracy of approximately **85%** on the test dataset. The results indicated a strong performance in detecting hate speech, with balanced precision, recall, and F1-score, showcasing its effectiveness in handling complex and context-dependent text data.


### 📢 **Conclusion**

Differentiating hate speech from offensive language is a challenging task. Our approach, which involves text pre-processing and feature extraction (e.g., n-gram tf-idf, sentiment polarity, doc2vec, and readability scores), demonstrates the benefits of using these features for classification. The evaluation of models based on accuracy and F1-scores highlights the complexity of the problem. While the results show the potential of the proposed features, further analysis and error review could improve feature extraction methods and help address existing challenges in detecting toxic language on platforms like Twitter.

### ✒️ **Your Signature**

Adwitya Chakraborty
