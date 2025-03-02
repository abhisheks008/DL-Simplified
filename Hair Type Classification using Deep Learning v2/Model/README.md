## **PROJECT TITLE**

### 🎯 **Goal**

The goal of the project is to classify different hair types.

### 🧵 **Dataset**

The dataset is taken from Kaggle.
Link: https://www.kaggle.com/datasets/kavyasreeb/hair-type-dataset

### 🧾 **Description**

The project is used to classify different hair types like staright, curly etc. It is useful to beauty parlours as they can recommend beauty products based on the hair type and also helpful for healthcare specialists as they can identify hair diseases for different hair types.

### 🧮 **What I had done!**

1. First I did some EDA on the data.
2. Then I preprocessed the data and split it into training and validation sets.
3. Then I trained 3 models on the data and also found out their performance metrics
4. At the end I created an ensemble model with the 3 models which are ResNet50, VGG16 and InceptionResNet

### 🚀 **Models Implemented**

1. ResNet50 - I have chosen this because of its skip connections which solves the vanishing gradient problem allowing it to do better feature extraction.
2. VGG16 - Chosen it as its simple yet effective architecture.
3. InceptionResNet - Chosen for its combination of Inception modules and residual connections.

### 📚 **Libraries Needed**

- Matplotlib
- pandas
- numpy
- sklearn
- tensorflow (keras)

### 📊 **Exploratory Data Analysis Results**

![image](https://github.com/user-attachments/assets/f7de162c-66ac-4b7f-b490-44bd29b87d40)


### 📈 **Performance of the Models based on the Accuracy Scores**

1. ResNet50 :- 85%
2. VGG16 :- 84%
3. InceptionResNet :- 84%

### 📢 **Conclusion**

ResNet50 performs the best for this project as it attains the highest accuracy of 85% out of the 3 models.

### ✒️ **Your Signature**

Subhrajyoti Basu
