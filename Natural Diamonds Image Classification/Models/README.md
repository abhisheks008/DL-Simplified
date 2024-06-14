# Natural Diamonds Shape Prediction

## 🎯 Goal
The main purpose of this project is to **classify between shapes of natural diamond** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/harshitlakhani/natural-diamonds-prices-images/data**

## 🧾 Description

This project involves the comparative analysis of **Five** Keras image detection models, namely **MobileNetV2** , **ResNet50** , **InceptionV3** , **DenseNet121** and **Xception**  applied to a specific dataset. The dataset consists of annotated images related to a particular domain, and the objectives include training and evaluating these models to compare their accuracy scores and performance metrics. Additionally, exploratory data analysis (EDA) techniques are employed to understand the dataset's characteristics, explore class distributions, detect imbalances, and identify areas for potential improvement. The methodology encompasses data preparation, model training, evaluation, comparative analysis of accuracy and performance metrics, and visualization of EDA insights. 

## 🧮 What I had done!

### 1. Data Loading and Preparation:
    Loaded the dataset containing image paths and corresponding labels into a pandas DataFrame for easy manipulation and analysis.

### 2. Exploratory Data Analysis (EDA):
    Bar Chart for Label Distribution: Created a bar chart to visualize the frequency distribution of different labels in the dataset.

    Pie Chart for Label Distribution: Generated a pie chart to represent the proportion of each label in the dataset.

### 3. Data Analysis:
    Counted the number of unique image paths to ensure data uniqueness and quality.
        Analyzed the distribution of image paths by label for the top 20 most frequent paths.
        Displayed the number of unique values for each categorical column to understand data variety.
        Visualized missing values in the dataset using a heatmap to identify and address potential data quality issues.
        Summarized and printed the counts of each label.

### 4. Image Preprocessing and Model Training:
    Loaded and preprocessed the test images, ensuring normalization of pixel values for consistency.
        Iterated through multiple models (VGG16, ResNet50 , Xception) saved in a directory and made predictions on the test dataset.
        Saved the predictions to CSV files for further analysis and comparison.

### 5. Model Prediction Visualization:
    Loaded models and visualized their predictions on a sample set of test images to qualitatively assess model performance.
        Adjusted image preprocessing for models requiring specific input sizes (e.g., 299x299 for Xception).

## 🚀 Models Implemented

Trained the dataset on various models , each of their summary is as follows :-

### Xception

When implementing the Xception model in code, we leverage its sophisticated architecture to bolster our image classification tasks. By loading the pre-trained Xception model with weights from the ImageNet dataset, we harness its comprehensive knowledge.

**Reasons for choosing Xception:** :  Lightweight (88 MB) , 
**Excellent Accuracy** (Xception achieves high accuracy in image classification tasks .) , 
Reduced Parameters (22.9M) ,
Faster Inference Speed (CPU - 39.4, GPU - 5.2)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/Xception_predictions/87e1b064-5b35-40b8-874a-2e553df38b8b.png)</br>

![alt text](../Images/Xception_predictions/c17ae0c4-ead4-4dee-add5-9163685bf6e9.png)</br>

![alt text](../Images/Xception_predictions/e02782bf-4641-4b2d-bb23-9a21db42d50b.png)


### MobileNetV2
Utilizing transfer learning with the MobileNetV2 model allows us to leverage pre-trained weights, drastically reducing the training time needed for image classification tasks. This strategy is especially beneficial when working with limited training data, as we can capitalize on the comprehensive representations learned by the base model from a vast dataset such as ImageNet.

**Reason for choosing :-** 
 Very lightweighted (14 MB) , better accuracy, very less parameters (3.5M) , less inference speed when using GPU (CPU - 25.9, GPU - 3.8)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/MobieNetV2_predictions/1c6eb16a-ba0c-44bd-859f-dc93d04a512d.png)</br>

![alt text](../Images/MobieNetV2_predictions/d9f67487-8192-404a-af02-19c4f7c3f49c.png)</br>

![alt text](../Images/MobieNetV2_predictions/e4e2adc1-b1b2-4eaa-91b6-d722298cca6b.png)



### ResNet50
Employing transfer learning with the ResNet50 model enables us to exploit pre-trained weights, significantly reducing the training time required for image classification tasks. This approach is particularly advantageous when dealing with limited training data, as we can leverage the rich representations learned by the base model from a vast dataset like ImageNet.

**Reason for choosing :-** 
 Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)


Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/ResNet50_predictions/3ee68192-605b-4eb3-8960-f5cc9bdecc7c.png)</br>

![alt text](../Images/ResNet50_predictions/78e8c330-dbe5-4854-af96-7b270eb6df7c.png)</br>

![alt text](../Images/ResNet50_predictions/c3786613-ed4c-4c78-b4a9-83ac80816538.png)




### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/InceptionV3_predictions/55179ff7-4837-44f3-a81a-025523b5c7a8.png)</br>

![alt text](../Images/InceptionV3_predictions/8e8399a2-0ffe-4b8d-a05e-c7f901d950a6.png)</br>

![alt text](../Images/InceptionV3_predictions/d1011560-3542-43e3-936e-6611cd244546.png)



### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/DenseNet121_predictions/11a9071b-c31d-454b-9128-8f125b3d2d3b.png)</br>

![alt text](../Images/DenseNet121_predictions/7b2b72a2-6576-45f1-a217-8f8c5ee1b21a.png)</br>

![alt text](../Images/DenseNet121_predictions/7fd4efc6-778c-4c0f-9f42-8ad0a466e22e.png)</br>


## 📚 Libraries Needed

1. **NumPy:** Fundamental package for numerical computing.
2. **pandas:** Data analysis and manipulation library.
3. **scikit-learn:** Machine learning library for classification, regression, and clustering.
4.  **Matplotlib:** Plotting library for creating visualizations.
5.  **Keras:** High-level neural networks API, typically used with TensorFlow backend.
6. **tqdm:** Progress bar utility for tracking iterations.
7. **seaborn:** Statistical data visualization library based on Matplotlib.

## 📊 Exploratory Data Analysis Results

### Bar Chart :-
 A bar chart showing the distribution of labels in the training dataset. It visually represents the frequency of each label category, providing an overview of how the labels are distributed across the dataset.

![alt text](../Images/bar.png)

### Pie Chart :-
A pie chart illustrating the distribution of labels in the training dataset. The percentage value displayed on each segment indicates the relative frequency of each label category.

![alt text](../Images/pie.png)

### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.

![alt text](../Images/image_path.png)

## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |85% ( Validation Accuracy: 0.8530)|
|InceptionV3  | 84% (Validation Accuracy: 0.8478) |
|DenseNet121      |  85% (Validation Accuracy: 0.8530) |
|ResNet50  |  82% (Validation Accuracy: 0.8150) |
|MobileNetV2       | 85% (Validation Accuracy: 0.8517) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that DenseNet121 and Xception were able to perform good on this dataset.**

 Even though on data analysis we found that the distribution of the dataset isn't consistent for all the classes and the data is also less in size.

## ✒️ Your Signature

Full name:- Aaradhya Singh                      
Github Id :- https://github.com/kyra-09  
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024