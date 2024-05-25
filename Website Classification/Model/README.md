## **URL Classification**

### 🎯 **Goal**
The main goal of this project is to classify URLs into different categories based on their content. This classification task involves training deep learning models to accurately predict the category of a given URL, such as adult content, arts, business, computers, games, health, home, kids, news, recreation, reference, science, shopping, society, or sports.

### 🧵 **Dataset**
The dataset used in this project is the [URL Classification Dataset](https://www.kaggle.com/datasets/shaurov/website-classification-using-url/data?select=URL+Classification.csv), which contains URLs along with their corresponding categories.

### 🧾 **Description**

This project focuses on building and training machine learning models to classify URLs into predefined categories. It involves preprocessing the dataset, visualizing the distribution of categories, and training multiple models to achieve high classification accuracy.

### 🧮 **What I had done!**

1. **Data Preprocessing**:
   - Imported necessary libraries for data manipulation, visualization, and model training.
   - Loaded the URL Classification dataset using Pandas.

2. **Data Visualization**:
   - Visualized the distribution of categories in the dataset using count plots.
   - Created count plots for the entire dataset, training dataset, and test dataset to understand the distribution of categories.

3. **Dataset Splitting**:
   - Split the dataset into training and test sets for model training and evaluation.

4. **Text Preprocessing**:
   - Applied text preprocessing techniques such as tokenization and padding to prepare the URL text data for model training.

5. **Model Building**:
   - Utilized three different models for URL classification:
     - Convolutional Neural Network (CNN)
     - Bidirectional Long Short-Term Memory (BiLSTM)
     - Multinomial Naive Bayes (MNB)
   - Designed and configured the architecture of each model with appropriate layers, activations, and regularization techniques.

6. **Model Training**:
   - Trained CNN and BiLSTM models using the preprocessed training data.
   - Implemented early stopping during training to prevent overfitting and restore the best weights.
   - Trained MNB model using a pipeline with text preprocessing steps.

7. **Model Evaluation**:
   - Evaluated the trained models using the test data to calculate accuracy and other relevant metrics.
   - Generated classification reports to assess the performance of each model.

8. **Visualization of Results**:
   - Plotted model training and validation loss and accuracy curves to visualize the learning process and performance of the models over epochs.
   - Compared the accuracies of the CNN, BiLSTM, and MNB models using a bar graph.

### 🚀 **Models Implemented**

#### Convolutional Neural Network (CNN):
- Designed a CNN model architecture consisting of embedding, convolutional, max pooling, flattening, dropout, and dense layers.
- Compiled the model with appropriate loss function and optimizer.
- Trained the model using the training data and evaluated its performance.

#### Bidirectional Long Short-Term Memory (BiLSTM):
- Constructed a BiLSTM model architecture with embedding, bidirectional LSTM, dense, and output layers.
- Compiled the model with suitable loss function and optimizer.
- Trained the model on the training data and assessed its performance.

### Multinomial Naive Bayes (MNB)

- **Model Pipeline Construction**: Created a pipeline that includes a `CountVectorizer` for tokenizing the text data, a `TfidfTransformer` for transforming token counts to TF-IDF representations, and a `MultinomialNB` classifier for training the model.
- **Text Vectorization and Transformation**: Used `CountVectorizer` to convert URLs into a matrix of token counts and `TfidfTransformer` to normalize these counts to reflect the importance of each word.
- **Model Training**: Trained the Multinomial Naive Bayes model on the preprocessed training data, optimizing with Laplace smoothing to handle zero probabilities.
- **Performance Evaluation**: Evaluated the model's performance using accuracy, precision, recall, and F1-score metrics, and generated confusion matrices to visualize classification results. 

### 📚 **Libraries Needed**

- Pandas: For data manipulation and analysis.
- NumPy: For numerical operations.
- Seaborn and Matplotlib: For data visualization.
- Scikit-learn: For machine learning tasks such as dataset splitting and evaluation.
- Keras (with TensorFlow backend): For building and training deep learning models.
- CountVectorizer
- TfidfTransformer
- MultinomialNB
- Pipeline

### 📊 **Exploratory Data Analysis Results**

## 1. URL Length Boxplot

![URL Length Boxplot](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/url_length_boxplot.png)

## 2. URL Length Distribution

![URL Length Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/url_length_distribution.png)

## 3. Training Dataset Category Distribution

![Training Dataset Category Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/train_dataset_count_plot.png)

## 4. Test Dataset Category Distribution

![Test Dataset Category Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/test_dataset_count_plot.png)

## 5. Overall Category Distribution

![Overall Category Distribution](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/category_count_plot.png)

## 6. Category Distribution Pie Chart

![Category Distribution Pie Chart](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/category_pie_chart.png)


### 📈 **Performance of the Models based on the Accuracy Scores**

- **Convolutional Neural Network (CNN) Accuracy**: 81.81%
- **Bidirectional Long Short-Term Memory (BiLSTM) Accuracy**: 91.55%
- **Multnominal Naive Bayes (MNB)**: 95.16%



`Accuracy`

![Accuracy](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/model_accuracy_plot_cnn.png)

`Loss`

![Loss](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/model_loss_plot_cnn.png)


`confusion matrix mnb`

![conf_mat](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/confusion_matrix_mnb.png)

`comparison`

![Comparison](https://github.com/manishh12/DL-Simplified/blob/main/Website_Classification/Images/model_accuracy_comparison.png)



Compare the accuracy scores of both models to determine the most effective model for URL classification.

### 📢 **Conclusion**

In conclusion, this project successfully implemented and trained deep learning models MNB, CNN and BiLSTM, for URL classification based on content categories. Both models were trained and evaluated using appropriate techniques, and their performance was assessed based on accuracy scores. The results demonstrate the effectiveness of deep learning models in classifying URLs into predefined categories.

### ✒️ **Your Signature**

[Manish Kumar Gupta]
