## **Emojify Your Tweets 😉 : Unleash the Power of Neural Networks**

### 🎯 **`Goal`**
---
The Goal is of this project is to analyse a given Tweet sentence and predict a an appropriate Emoji for it.

### 🧵 **`Dataset`**
---
I have used [Twitter Emoji Prediction Dataset](https://www.kaggle.com/datasets/hariharasudhanas/twitter-emoji-prediction) and [Glove Vector Representation](https://www.kaggle.com/datasets/watts2/glove6b50dtxt)

### 🧾 **`Description`** 
---
Emojis are the lifeblood of online expression! This project explored predicting the perfect emoji for your tweets using neural networks. We built two models: a basic one (34% accuracy) and a powerful LSTM (93% accuracy) that considers word order. We fine-tuned the models for optimal performance and analyzed their strengths beyond just accuracy. This paves the way for even more accurate emoji prediction, making your tweets truly shine! 

### 🧮 **`What have I done`**
---
The first thing I did was to get a dataset with good number of examples and usability.
Then I spent quite good time in researching for different architectures and techniques that could be used to solve the problem and I found solutions that involved the use of word embeddings.

<h3>The first architecture is as follows:</h3>
<img src="./Images/Model1_Architecture.png" style = "border : 1px dashed white; border-radius:5px;"></img>

In this architecture , given a sentence we would split it into words and get its Glove vector representation i.e the embeddings. 
> - The Glove vector is a 50-dimensional vector that was trained over a large corpus of texts and documents.
> - and the vocabulory has 400k words.

Now once we obtain the embedding for each word in the sentence , we average out the embeddings and this mean vector is passed as an input to a Fully Connected NN that has an softmax output layer (There are 20 emojis in the dataset).
the model is then trained and results in a satifactory performance. 

<h3>The Second architecture is as follows:</h3>
<img src="./Images/Model2_Architecture.png" style = "border : 1px dashed white; border-radius:5px;" height = 600 width = 400></img>

The main problem with the previous model was that the average operation doesn't capture much useful information . So , the best option would be using an LSTM.<br>
Now to train the LSTM for a given sentence we need to pass each word to the LSTM cell 
i.e `Tx time steps`. So all the sentences need to be of same length and this can be done using padding and truncation operations.

We are gonna have 2 dictionaries `WORD_TO_VEC` and `WORD_TO_INDICES` <br>
> - `WORD_TO_VEC` : maps every word in the vocabulary to their vector representations.
> - `WORD_TO_INDICES` : maps every word in the vocabulary to their positions in the vocabulory.

Now the first operation is `sentence_to_indices`:<br>From the name its clear that we are going to replace each word in a sentence with their respective indices in the vocabulory and if word is not found its gonna be 0.

The second thing is building a `Embedding Layer`:<br>We will be converting the vocabulory into a matrix where each row is a vector representation `shape = (400k + 1, 50)` of words.We set it as weights to the Embedding Layer and put `training = False` as we dont want to update them.

The Final step is create a multi-layer LSTM architecture connected to a softmax layer with 20 units(20 emojis...).<br>
The model is then trained over 50 epochs and made to overfit the training data. Once it overfits use regularization techniques like Dropout to generalize well.

Now the model is saved in keras format and performance analysis is performed like calculating precision , recall , f1-score , accuracy and confusion matrix.

### 🚀 **`Models Implemented`**
 ---
I have used two different models 
- Fully Connected Neural Network.
- Multi-Layer LSTM Architecture.


### 📈 **`Performance of the Models based on the Accuracy Scores`**
---
<style>
    th{
        color : black;
        background-color:yellow;
    }
</style>
<table style = "border: 1px solid black;">
    <tr>
        <th>S.No</th>
        <th>Model Name</th>
        <th>Accuracy</th>
    </tr>
    <tr>
        <td>1.</td>
        <td>FCNN</td>
        <td>34.25%</td>
    </tr>
    <tr>
        <td>2.</td>
        <td>LSTM MODEL</td>
        <td>93.42%</td>
    </tr>
<table>

### 📢 **`Conclusion`**
---

In this project, I explored two different neural network architectures for predicting emojis from text data. The first architecture, a fully connected neural network with averaged word embeddings, achieved an accuracy of 34.25%. However, the second architecture, a multi-layer LSTM network, significantly outperformed the first model with an accuracy of 93.42% on training data and 92% over the test data. This demonstrates the importance of capturing sequential information in text data for tasks like emoji prediction.

Future work could involve exploring more advanced LSTM architectures or incorporating attention based models. Overall, this project successfully demonstrates the power of neural networks for emoji prediction and opens doors for further exploration in this exciting field.

### ✒️  **`Author`**
---
`Bingumalla Likith |
GSSoC 24 Contributor|
Issue Number #673`

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/bingumalla-likith-2633392b9)  [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/binguliki)