## **Avocados Classification**

### **Goal**
The project aims to predict whether an avocado is conventional or organic using Deep learning models.

### **Dataset**

https://www.kaggle.com/datasets/neuromusic/avocado-prices

### **Description**

The main goal of this project is to develop a Dl model that can accurately predict whether an avocado is conventional or organic based on various features such as `Size of Bags`,`Volume`,`Price` etc. The purpose of this project is to categorize avocados for better market segmentation and analysis

### **What I had done!**


1. Data loading and exploration: Loaded the dataset, examined its structure, and performed initial exploratory data analysis (EDA) to gain insights into the data distribution, missing values, and relationships between variables.

2. Data preprocessing: Conducted data preprocessing steps such as handling missing values, encoding categorical variables, and scaling numerical features to prepare the data for model training.

3. Feature selection: Applied feature selection techniques to identify the most relevant features that contribute significantly to the prediction of heart strokes. This helps in reducing model complexity and improving performance.

4. Model development: Three models were developed: Feedforward Neural Network (FNN),TabNet, and Long Short-Term Memory (LSTM). Each model was trained and evaluated based on accuracy.

###  **Models Implemented**
```bash
  a.LSTM (Long Short-Term Memory In avocado classification, LSTM 
  classifies by taking sequential input data and processing it through 
  memory cells, which learn to retain relevant information. It builds the 
  model using multiple LSTM layers to capture complex patterns, and then 
  applies a dense layer for final classification based on the learned 
  temporal dependencies, resulting in accurate avocado classification.
```
```bash
  b. Feedforward Neural Network (FNN): Developed an FNN model using the Keras library 
  with multiple hidden layers and appropriate activation functions. Trained the model using  
  the preprocessed data and fine-tuned hyperparameters to achieve optimal performance.
```
```bash
  c. Recurrent Neural Network (RNN): TABNET classifies using a unique 
  attention mechanism that selects and updates relevant features during 
  training. It builds the model by iteratively selecting subsets of 
  features, employing shared decision trees, and gradually learning 
  feature importance, leading to an interpretable and efficient model 
  for accurate avocado classification..
```
### **Libraries Needed**

- Pandas
- Tensorflow
- Seaborn
- Sklearn
- pathlib
- numpy
- keras
- torch

### 📈 **Performance of the Models based on the Accuracy Scores**

| Model            | Accuracy                                                               |
| ----------------- | ------------------------------------------------------------------ |
| TabNet |  0.79 |
| LSTM |9389041095890411 |
| FNN| 1.0 |

![Comparison graph](https://github.com/RAJharsh02/Avocados-classification/assets/118257196/60225a7c-e5eb-4904-8ec4-db7f079e2d60)

### 📢 **Conclusion**

In conclusion, this project aimed to classify Avocados using DL models. Among the models developed, the Feedforward Neural Network (fNN) achieved the highest accuracy of 100%. This suggests that the temporal dependencies captured by the FNN architecture are valuable in slassifying Avocados.

### ✒️ **Author**

- Code contributed by *Harsh Raj* @ #SSoC_2023

<a href="harshraj2828@gmail.com"><img src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" width="30px" alt="Email"></a>
&nbsp; &nbsp;
<a href = https://github.com/RAJharsh02><img src = "https://www.vectorlogo.zone/util/preview.html?image=/logos/github/github-tile.svg"  width="30px" alt="Github"> </a>

- README.md modified by *Mariam* @ #DWoC_2023

<a href="https://www.linkedin.com/in/mariam-m7084"><img src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" width="30px" alt="linkedin"></a>
&nbsp; &nbsp;

<a href = https://github.com/mariam7084/><img src = "https://www.vectorlogo.zone/util/preview.html?image=/logos/github/github-tile.svg"  width="30px" alt="Github"> </a>
