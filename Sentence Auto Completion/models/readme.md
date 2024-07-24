# Auto-Complete Sentence Using LSTM, GRU, and BiLSTM

## 🎯 Goal
The main goal of this project is to develop a deep learning-based auto-complete system that can predict the next word or phrase in a sentence. The purpose of this system is to enhance user typing experience by providing contextually relevant suggestions as the user types.

## 🧵 Dataset
- csv file name- sentence_auto_completion_dataset.csv
### Dataset Structure
The dataset consists of two columns:
- **incomplete_sentence**: The initial fragment of a sentence that needs completion.
- **completion**: The full sentence that completes the fragment.

## 🧾 Description
This project involves building a sentence auto-completion system using three different deep learning models: Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), and Bidirectional LSTM (BiLSTM). The system is designed to predict the next word in a given sentence, making it useful for applications such as text editors and chatbots.

## 🧮 What I Had Done!
1. **Data Collection**: Acquired and preprocessed the dataset for training and testing.
2. **Data Preprocessing**: Tokenized text data, padded sequences, and created training and validation datasets.
3. **Model Implementation**: Built and trained three different models: LSTM, GRU, and BiLSTM.
4. **Training**: Trained the models on the preprocessed dataset, monitoring the training and validation losses.
5. **Evaluation**: Evaluated the performance of each model using accuracy and other metrics.
6. **Results Analysis**: Compared the performance of the models based on their accuracy scores.
7. **Visualization**: Plotted loss and accuracy curves for each model to visualize performance.

## 🚀 Models Implemented
1. **LSTM (Long Short-Term Memory)**
   - Chosen for its ability to capture long-term dependencies in sequences.
2. **GRU (Gated Recurrent Unit)**
   - Selected for its simpler architecture compared to LSTM, which can lead to faster training times.
3. **BiLSTM (Bidirectional LSTM)**
   - Utilized to capture context from both past and future directions, potentially improving prediction accuracy.

## 📚 Libraries Needed
- `numpy`
- `pandas`
- `tensorflow` or `keras`
- `matplotlib`
- `scikit-learn`

## 📊 Exploratory Data Analysis Results
![EDA Image 1](Sentence Auto Completion\images\Distribution of senetences.png)
![EDA Image 2](images\word Cloud.png)
*Include images of visualizations from EDA*

## 📈 Performance of the Models Based on the Accuracy Scores
- **LSTM**
  - Accuracy: 87.41%
  - Results: The LSTM model showed steady improvement in accuracy, achieving a final validation accuracy of 87.41%.
- **GRU**
  - Accuracy: 87.41%
  - Results: The GRU model also performed consistently, reaching a final validation accuracy of 87.41%, similar to the LSTM model.
- **BiLSTM**
  - Accuracy: 8.33%
  - Results: The BiLSTM model achieved a final validation accuracy of 8.33%, indicating a less effective performance compared to LSTM and GRU.

## 📢 Conclusion
The LSTM and GRU models both achieved the highest accuracy of 87.41%, making them the best-performing models for the auto-complete sentence task. The BiLSTM model did not perform as well, with a final accuracy of 8.33%. The choice of LSTM and GRU is justified by their high accuracy in predicting the next word in a sentence, making them suitable for this auto-complete application.

## Contributor 
Ashish Kumar Patel
