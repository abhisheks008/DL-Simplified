## 🎯 Goal
The main goal of this project is to develop a Sudoku Solver using three different algorithms: Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), and Generative Adversarial Networks (GAN). The purpose is to compare the performance of these models and determine which is the most effective at solving Sudoku puzzles.

## 🧵 Dataset
The dataset used for this project is sudoku_dataset.csv. It contains 1000 Sudoku puzzles and their corresponding solutions


## 🧾 Description
This project involves the implementation of three different deep learning algorithms to solve Sudoku puzzles: Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), and Generative Adversarial Networks (GAN). Each model is trained to recognize and complete Sudoku grids, and their performance is evaluated and compared.

## 🧮 What I had done!
1. Loaded and preprocessed the dataset.
2. Performed EDA to understand the distribution and characteristics of the data.
3. Implemented three different models: CNN, RNN, and GAN.
4. Trained and evaluated each model.
5. Compared the models based on their accuracy scores.

## 🚀 Models Implemented
- **Convolutional Neural Network (CNN):** Chosen for its effectiveness in handling grid-like data such as images, making it suitable for Sudoku puzzles.
- **Recurrent Neural Network (RNN):** RNNs, especially LSTMs, are used for sequence learning, making them useful for predicting sequences of numbers.
- **Generative Adversarial Network (GAN):** GANs are used to generate new data, in this case, solving Sudoku puzzles by generating possible solutions.

## 📚 Libraries Needed
- pandas
- numpy
- matplotlib
- seaborn
- tensorflow
- sklearn

## 📊 Exploratory Data Analysis Results
Dataset Distribution
Dataset shape: (1000, 2)
Missing values in the dataset:
puzzle      0
solution    0
dtype: int64

### Visualizations

#### Distribution of Values in Puzzles
![Distribution of Values in Puzzles](images/eda.png)

#### Distribution of Values in Solutions
![Distribution of Values in Solutions](images/eda1.png)

#### Sample Puzzle Visualization
![Sample Puzzle](images/output.png)

#### Sample Solution Visualization
![Sample Solution](images/output1.png)

## 📈 Performance of the Models based on the Accuracy Scores

- **CNN:**
  - Training Loss: 0.8336
  - Training Accuracy: 80.30%
  - Test Accuracy: 80.30%
- **RNN:**
  - Training Loss: 0.2435
  - Training Accuracy: 97.10%
  - Test Accuracy: 97.10%
- **GAN:**
  - Epoch 300/300
  - D Loss: 0.1164
  - D Acc: 98.44%
  - G Loss: 2.9346
## 📢 Conclusion
In this project, we explored the use of CNN, RNN, and GAN models for solving Sudoku puzzles. The RNN model achieved the highest accuracy at 97.10%, making it the most effective model for this task. The CNN model also performed well, with an accuracy of 80.30%. The GAN model showed promising results in generating and solving puzzles, with a discriminator accuracy of 98.44%.

Based on accuracy scores, the RNN model is the best-fitted model for solving Sudoku puzzles among the three developed models.

## Contributor
Ashish Kumar Patel
