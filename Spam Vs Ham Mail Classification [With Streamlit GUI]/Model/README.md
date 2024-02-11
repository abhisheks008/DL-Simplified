*SPAM vs HAM Email Classification*<br>
*🎯 Goal*<br>

The main goal of this project is to develop a robust deep learning model for classifying emails as either spam (SPAM) or legitimate (HAM). Additionally, the project aims to create a Streamlit GUI for a user-friendly interface in real-time email classification.<br>

*🧵 Dataset*<br>

The dataset used for this project is available [ https://www.kaggle.com/datasets/omokennanna/simple-spam-classification ]. It consists of two columns: 'text' containing the email content and 'label' indicating whether the email is spam or ham.<br>

*🧾 Description*<br>

This project utilizes a deep learning model with an embedding layer, bidirectional LSTM layers, and a dense output layer. The model is trained on the provided dataset to classify emails as spam or ham. A Streamlit GUI is implemented to enable users to perform real-time email classification.

*🧮 What I had done!*<br>

1. **Data Preparation:**<br>

    - The dataset is loaded and split into training and testing sets.<br>
    - Missing values are handled, and the text data is preprocessed.<br>

2. **Model Architecture:**<br>
    - The Machine learning model I used several algorithm for better accuracy.<br>

    - The deep learning model comprises an embedding layer, LSTM layers, and a dense output layer with a sigmoid activation function.<br>

    - The deep learning model comprises an embedding layer, bidirectional LSTM layers, and a dense output layer with a sigmoid activation function.<br>
3. **Training the Model:**

The model is trained on the preprocessed dataset using the Adam optimizer and binary crossentropy loss.
The training process is monitored for convergence and effectiveness.<br>
4. **Streamlit GUI:**

A Streamlit GUI is implemented for real-time email classification.<br>
Users can input an email, and the model predicts whether it is spam or ham.<br>
<br>

*🚀 Models Implemented*<br>
1. Machine Learning Model
2. Deep Learning Model with LSTM Layers
3. Deep Learning Model with Bidirectional LSTM Layers

**Why these models:**

1. Machine Learning Model:<br>

    This traditional machine learning model serves as a baseline and allows us to compare the performance of deep learning models against a more conventional approach. It may use classic algorithms like Support Vector Machines, Random Forest, or Logistic Regression, depending on the nature of the problem.<br>

2. Deep Learning Model with LSTM Layers:<br>

    Long Short-Term Memory (LSTM) layers are particularly effective for sequential data. This model is well-suited for capturing long-range dependencies and patterns within the input data. It's a suitable choice when dealing with sequences, such as time-series data or natural language processing tasks.<br>
3. Deep Learning Model with Bidirectional LSTM Layers:<br>

    Bidirectional LSTM layers enhance the LSTM model by processing sequences in both forward and backward directions. This allows the model to capture information from past and future time steps simultaneously. Bidirectional LSTMs are beneficial when the context from both directions is essential for understanding the input data.<br>

*📚 Libraries Needed*<br>

1. TensorFlow
2. scikit-learn
3. pandas
4. maplotlib
5. seaborn
6. streamlit

<br>
*📊 Exploratory Data Analysis Results*<br>


Insight: In the Dataset we have 88% Ham Data and 12% Spam Data . The distribution of classes are imbalanced which will create a challenge in accurately classifying emails . <br>




*📈 Performance of the Models based on the Accuracy Scores*<br>

bnb=BernoulliNB()
1. Machine Learning Model [ BernoulliNB ] : 96%
2. Deep Learning Model Accuracy[LSTM  Model]: 88.58%
3. Deep Learning Model Accuracy[Bidirectional LSTM  Model]: 98.56%


*📢 Conclusion*<br>

The SPAM vs HAM Email Classification project, coupled with the Streamlit GUI, provides an effective solution for real-time email categorization. The deep learning model demonstrates promising accuracy, and the user-friendly interface makes it accessible for practical use.<br>

*✒️ Your Signature*<br>

Dipayan Majumder<br>
github.com/dipayan22<br>