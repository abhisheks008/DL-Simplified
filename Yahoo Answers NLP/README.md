<div align = 'center'>
  <h1>Yahoo Answers NLP</h1>
  </div>
<img src = "https://github.com/Aadi71/DL-Simplified/blob/main/Yahoo%20Answers%20NLP/Images/yahoo-answers.png">

### Goal
The goal of this project is to create a deep learning model to analyse the Yahoo Answers.

### Dataset
The dataset for this project is taken from the Kaggle dataset website. Here is the link for the dataset: https://www.kaggle.com/datasets/yacharki/yahoo-answers-10-categories-for-nlp-csv

### What Have I Done?
- Imported all the required libraries and dataset for this project.
- Exploratory Data Analysis and Visualizing different aspects of the dataset.
- Finding number of observations and outliers in the dataset.
- Plotting different attributes of the dataset.
- Preprocessing of the dataset:
  - lower case the text
  - removing punctuations
  - removing stopwords
  - lemmatization 
  - removing HTML syntax or URL's
  - stripping the extra spaces
  - applying contraction
- Tokenization of data and applied text to sequence
- Applying Deep Learning algorithms for the Model Creation such as CNN and LSTM.

### Libraries used:
1. numpy.
2. pandas.
3. matplotlib.
4. seaborn.
5. sklearn.
6. os.
7. time.
8. Keras
9. Tenserflow
10. Contractions

### Visualization of question lengths per category:
<img src = "https://github.com/Aadi71/DL-Simplified/blob/main/Yahoo%20Answers%20NLP/Images/box%20plot.png">

### Model Creation:
LSTM gave more accuracy than CNN.

### CNN Performance Plot:
<img src = "https://github.com/Aadi71/DL-Simplified/blob/main/Yahoo%20Answers%20NLP/Images/CNN%20Plot.png">

### LSTM Performance Plot:
<img src = "https://github.com/Aadi71/DL-Simplified/blob/main/Yahoo%20Answers%20NLP/Images/LSTM%20Plot.png">

### Hence, we have trained two neural network models: **LSTM**(Accuracy: 46.26%) and **CNN**(38.97%)

### Author
Code contributed by: **Aadi Jain**
- Connect me through LinkedIn: https://www.linkedin.com/in/aadijain7102/
- Check out my GitHub Profile: https://github.com/Aadi71
