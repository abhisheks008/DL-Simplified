## **Online Food Delivery Preferences**

### 🎯 **Goal**

The project focuses on two primary objectives:

Predict whether customers will place future orders using CNN, RNN, and a hybrid RNN+LSTM model based on demographic data such as age, occupation, monthly income, and family size.
Perform sentiment analysis on customer reviews to better understand customer experiences, using DNN, LSTM, and GRU models to classify the reviews as positive or negative.


### 🧵 **Dataset**

Link : https://www.kaggle.com/datasets/benroshan/online-food-delivery-preferencesbangalore-region/data

The dataset consists of 388 entries with 55 columns, providing detailed insights into customer preferences and experiences in online food delivery. Key variables include:

1. **Demographics**: Age, gender, marital status, occupation, income, and education levels.
2. **Geographical Data**: Latitude, longitude, pin codes.
3. **Service Preferences**: Meal and medium preferences (e.g., "Medium (P1)", "Meal (P1)"), ease, convenience, and time-saving benefits.
4. **Delivery Experience**: Factors like restaurant choices, payment options, food quality, tracking systems, and road conditions.
5. **Challenges**: Common issues such as late deliveries, hygiene concerns, wrong orders, missing items, and delivery delays.
6. **User Feedback**: Reviews, Google Maps accuracy, politeness of delivery personnel, and the influence of ratings.
7. **Outcome**: Whether this consumer will buy again or not (e.g., "Output").

### 🧾 **Description**

This project is divided into two main tasks:

Customer Reordering Behavior Prediction:
For predicting whether a customer will reorder, CNN, RNN, and RNN+LSTM models were used. These models are trained on the structured dataset containing demographic data and behavioral factors.

Sentiment Analysis of Customer Reviews:
For text-based sentiment analysis, DNN, LSTM, and GRU models were developed. These models aim to classify customer reviews as positive or negative, helping businesses understand customer satisfaction more effectively.

### 🧮 **What I had done!**

1) Data Preprocessing:
-Removed missing and irrelevant data (e.g., 'Nil' reviews).
-Tokenized reviews and converted them into sequences suitable for deep learning models.

2) Exploratory Data Analysis (EDA):
-Analyzed the distribution of customer demographics such as age, income, family size etc.
-Created visualizations like bar charts and word clouds for reviews to understand sentiment polarity.

3) Model Implementation for Prediction:
-Built CNN, RNN, and RNN+LSTM models to predict customer reordering behavior.
-Experimented with different architectures to capture patterns in structured data.

4) Model Implementation for Sentiment Analysis:
-Developed DNN, LSTM, and GRU models for customer review analysis.
-These models were optimized to handle varying text lengths and interpret user sentiment effectively.

5) Evaluation and Comparison:
-Compared models using accuracy, precision, recall, and F1-score.
-Identified the most accurate models for each task.

### 🚀 **Models Implemented**

For Customer Reordering Prediction:
CNN (Convolutional Neural Network): Captures local patterns and relationships in structured data such as demographic information.
RNN (Recurrent Neural Network): Captures sequential dependencies between behavioral factors, though it can suffer from vanishing gradients.
RNN + LSTM (Hybrid Model): Handles long-term dependencies more effectively than standard RNNs, providing more accurate predictions for reordering behavior.

For Sentiment Analysis:
DNN (Deep Neural Network): A feedforward network used for simple yet effective sentiment classification.
LSTM (Long Short-Term Memory): Captures long-term dependencies in reviews, making it suitable for longer texts.
GRU (Gated Recurrent Unit): An efficient variant of LSTM, offering similar capabilities with fewer parameters.

### 📚 **Libraries Needed**

1. **os**  
- Provides functions for interacting with the operating system (e.g., file and directory management).  

2. **pandas**  
   - Used for data manipulation and analysis, especially with DataFrames.  

3. **numpy**  
   - Supports numerical operations, including working with arrays, matrices, and mathematical computations.  

4. **scipy**  
   - Provides statistical functions and tools for scientific computing.  

5. **matplotlib**  
   - A plotting library used for creating visualizations like graphs and charts.  

6. **seaborn**  
   - A data visualization library built on Matplotlib, offering advanced statistical plots.  

7. **scikit-learn (sklearn)**  
   - A machine learning library providing tools for:
     - Data preprocessing (e.g., LabelEncoder, StandardScaler)  
     - Model evaluation (e.g., classification_report, accuracy_score)  
     - Train-test data splitting (e.g., train_test_split)  

8. **tensorflow**  
   - A deep learning framework used to build and train neural networks.  

9. **tensorflow.keras**  
   - A high-level neural network API within TensorFlow, offering:
     - Model creation using Sequential  
     - Neural network layers (e.g., Dense, LSTM, GRU, Dropout)  
     - Regularization techniques (e.g., L2 regularizers)  
     - Text processing tools (e.g., Tokenizer, pad_sequences) .

### 📊 **Exploratory Data Analysis Results**

<h2>Demographic  Details</h2>
![Age Group]
(https://github.com/Pratzybha/Images/blob/main/Images/AgeGroup.png)

![Demographic  Details]
(https://github.com/Pratzybha/Images/blob/main/Images/DemographicDetails.png)

<h2>Correlation Calculation</h2>
![Correlation Calculation]
(https://github.com/Pratzybha/Images/blob/main/Images/CorrelationCalculation.png)

<h2>Features That Influence Users To Use Online Food Delivery</h2>
![Features That Influence Users To Use Online Food Delivery]
(https://github.com/Pratzybha/Images/blob/main/Images/FeaturesOnlineDelivery%201.png)

<h2>Features That Discourage Users To Use Online Food Delivery</h2>
![Features That Discourage Users To Use Online Food Delivery]
(https://github.com/Pratzybha/Images/blob/main/Images/FeaturesOnlineDelivery%202.png)

<h2>Time Factor</h2>
![Time Factor]
(https://github.com/Pratzybha/Images/blob/main/Images/FeaturesOnlineDelivery%203.png)

### 📈 **Performance of the Models based on the Accuracy Scores**

| Model      | Accuracy |
|------------|----------|
| CNN        | 90%      |
| RNN        | 92%      |
| RNN + LSTM | 92.3%    |
| DNN        | 84%      |
| LSTM       | 92%      |
| GRU        | 88%      |


### 📢 **Conclusion**

The project successfully demonstrates the potential of deep learning models for both customer behavior prediction and sentiment analysis.

The RNN + LSTM Hybrid model provided the best performance for sentiment analysis, achieving an accuracy of 92.3%.
The LSTM model effectively predicted reordering behavior with 92% accuracy.
These insights help food delivery companies better understand customer preferences and enhance their service quality.


### ✒️ **Your Signature**

Your Name: [Pratibha Balgi]

GitHub: [https://github.com/Pratzybha]

LinkedIn: [https://www.linkedin.com/in/pratibhabalgi2410/]
