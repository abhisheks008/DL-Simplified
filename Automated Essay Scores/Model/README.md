## **PROJECT TITLE**

### 🎯 **Goal**

The main goal of this project is to develop deep learning models (LSTM, GRU, CNN) for automated essay scoring. The purpose is to reduce grading time and provide consistent feedback to students based on their essays.

### 🧵 **Dataset**

The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/competitions/learning-agency-lab-automated-essay-scoring-2/code). It consists of student-written essays annotated with scores based on a rubric covering various criteria.

### 🧾 **Description**

This project aims to implement and compare several deep learning models to automatically score student essays. It involves preprocessing text data, training LSTM, GRU, and CNN models, and evaluating their performance using metrics like Quadratic Weighted Kappa (QWK).

### 🧮 **What I had done!**

- Preprocessed the text data by cleaning and tokenizing essays.
- Implemented LSTM, GRU, and CNN models using TensorFlow and Keras.
- Conducted exploratory data analysis (EDA) to understand the dataset's characteristics.
- Evaluated model performance using metrics such as Quadratic Weighted Kappa (QWK) and accuracy.

### 🚀 **Models Implemented**

- **LSTM**: Chosen for its ability to capture long-term dependencies in sequential data like essays.
- **GRU**: Selected for its simpler architecture compared to LSTM, potentially offering faster training times.
- **CNN**: Adapted for text classification to capture local patterns in essays.

### 📚 **Libraries Needed**

- numpy==1.21.2
- pandas==1.3.3
- nltk==3.6.5
- scikit-learn==0.24.2
- tensorflow==2.7.0
- matplotlib==3.4.3
- seaborn==0.11.2
- keras==2.6.0

### 📊 **Exploratory Data Analysis Results**

![Distribution of Essay Scores](<../Images/Score Distribution.png>)
![Distribution of Essay Length](<../Images/Length Distribution.png>)

### 📈 **Performance of the Models based on the Accuracy Scores**

- **LSTM**: QWK - 0.6764
- **GRU**: QWK - 0.9048
- **CNN**: QWK - 0.9239


### 📢 **Conclusion**

Based on the evaluation results, the LSTM model outperformed the GRU and CNN models in terms of accuracy and Quadratic Weighted Kappa. This indicates its effectiveness in scoring student essays accurately. Further optimization and fine-tuning of models could potentially improve performance.

### ✒️ **Your Signature**

Ojaswi Chopra

---

Connect with me on [LinkedIn](https://www.linkedin.com/ojaswichopra) | [GitHub](https://github.com/ojaswichopra)