Data Preprocessing
Sentiment Analysis:

A sentiment analyzer is used to assign sentiment scores to each data point.
Scores are converted to categorical labels:
Negative: -1
Neutral: 0
Positive: 1
A new column named "category" is added to the dataset containing these labels.
Text Normalization:

Lemmatization and stemming are applied to reduce words to their base or root form.
This reduces variations of words (e.g., "running", "runs", "ran" become "run").
Undersampling:

(Optional) If the dataset has class imbalance (unequal distribution of sentiment classes), undersampling is used to balance the classes.
This can improve model performance.
TF-IDF:

TF-IDF (Term Frequency-Inverse Document Frequency) is used to represent the text data numerically.
It considers the importance of a word based on its frequency in a document and its rarity across the corpus.
Deep Learning Models
LSTM (Long Short-Term Memory):

An LSTM model is trained to capture long-term dependencies within the text sequences.
This is useful for sentiment analysis as sentiment can be influenced by words further back in the sentence.
CNN (Convolutional Neural Network):

A CNN model is trained to identify local patterns within the text data.
This can be helpful for capturing sentiment expressed through specific phrases or word combinations.
CNN + LSTM:

An ensemble model combining CNN and LSTM is trained.
This leverages the strengths of both models: CNN for local features and LSTM for long-term dependencies.

Accuracy scores:
LSTM:0.90
CNN:0.88
CNN+LSTM:0.89
