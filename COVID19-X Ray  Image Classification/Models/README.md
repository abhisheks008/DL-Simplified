# COVID19-X Ray Image Classification

## 🎯 Goal
The main purpose of this project is to **classify between X-Ray Images to find X-rays for COVID-19** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset**

## 🧾 Description

This project involves the comparative analysis of **Five** Keras image detection models, namely **MobileNetV2** , **VGG16** , **InceptionV3** , **DenseNet121** and **Xception**  applied to a specific dataset. The dataset consists of annotated images related to a particular domain, and the objectives include training and evaluating these models to compare their accuracy scores and performance metrics. Additionally, exploratory data analysis (EDA) techniques are employed to understand the dataset's characteristics, explore class distributions, detect imbalances, and identify areas for potential improvement. The methodology encompasses data preparation, model training, evaluation, comparative analysis of accuracy and performance metrics, and visualization of EDA insights. 

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
![alt text](../Images/Xception_predictions/61a8aed3-bd82-4ff9-8ab9-5dd37a41d889.png)</br>

![alt text](../Images/Xception_predictions/86bf04a4-43cc-4741-b300-8ad978c46132.png)</br>

![alt text](../Images/Xception_predictions/89435ec5-a3b2-4942-a735-3ec28f9a918c.png)</br>

![alt text](../Images/Xception_predictions/fb82b37b-d970-48cc-a159-8e9587f35f1a.png)</br>



### MobileNetV2
Utilizing transfer learning with the MobileNetV2 model allows us to leverage pre-trained weights, drastically reducing the training time needed for image classification tasks. This strategy is especially beneficial when working with limited training data, as we can capitalize on the comprehensive representations learned by the base model from a vast dataset such as ImageNet.

**Reason for choosing :-** 
 Very lightweighted (14 MB) , better accuracy, very less parameters (3.5M) , less inference speed when using GPU (CPU - 25.9, GPU - 3.8)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/MobieNetV2_predictions/4d8f7d2a-3ef1-4942-820b-3055bb4dc16f.png)</br>

![alt text](../Images/MobieNetV2_predictions/6bbe9b43-1bc7-47e1-9aaa-69b4fa8ef1c6.png)</br>

![alt text](../Images/MobieNetV2_predictions/92336470-2301-4a96-9a6e-fba21558bff6.png)</br>

![alt text](../Images/MobieNetV2_predictions/feaf9857-f711-41b8-8086-343dc8610c46.png)</br>



### VGG16
I will utilize the VGG16 (Visual Geometry Group) architecture, which have deeper and complex structures. These models are renowned for their exceptional performance on various image recognition tasks. 

**Reason for choosing :-** 
 Highest accuracy (90.1%) , less depth (16) , inference speed less when using GPU (CPU - 69.5 , GPU - 4.2)


Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/VGG16_predictions/04701e86-c359-4103-899a-55faa0e6ea08.png)</br>
![alt text](../Images/VGG16_predictions/4baaf1a6-0eed-4833-bf01-21628c39cf0e.png)</br>
![alt text](../Images/VGG16_predictions/4e652e15-23c6-4317-861f-9bd5d14a5940.png)</br>
![alt text](../Images/VGG16_predictions/af7f9523-cc21-454a-8f1c-35facfb2a89e.png)</br>



### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/InceptionV3_predictions/54a01ad5-ad98-4506-94a6-51cf178b3c4d.png)</br>
![alt text](../Images/InceptionV3_predictions/55c53623-3f9b-4cf3-8624-7a509b7e7478.png)</br>
![alt text](../Images/InceptionV3_predictions/8b73d11e-6df6-4332-9807-d0e37e2bb100.png)</br>
![alt text](../Images/InceptionV3_predictions/9f819a75-9fca-4a51-99ac-097194a7d43e.png)</br>






### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet121_predictions/0e775fe9-7a73-49cd-bf74-3fa33f76e2a5.png)</br>
![alt text](../Images/DenseNet121_predictions/5ef690cb-9c3b-476b-8aeb-c63847941837.png)</br>
![alt text](../Images/DenseNet121_predictions/7e024ac4-f3b4-4832-a776-0c2bb93b2c56.png)</br>
![alt text](../Images/DenseNet121_predictions/8af20033-5829-4bdc-aeef-db9b5f63c387.png)</br>


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

![alt text](../Images/bar_chart.png)


### Pie Chart :-
A pie chart illustrating the distribution of labels in the training dataset. The percentage value displayed on each segment indicates the relative frequency of each label category.

![alt text](../Images/pie.png)

### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.


![alt text](../Images/image_path_distribution.png)



## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |86% ( Validation Accuracy: 0.8627)|
|InceptionV3  | 78% (Validation Accuracy: 0.7843) |
|DenseNet121      |  90% (Validation Accuracy: 0.9020) |
|VGG16  |  80% (Validation Accuracy: 0.8039) |
|MobileNetV2       | 80% (Validation Accuracy: 0.8039) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that DenseNet121 and Xception were able to perform good on this dataset.**

 Even though on data analysis we found that the distribution of the dataset isn't consistent for all the classes and the data is also less in size.

## ✒️ Your Signature

Full name:- Aaradhya Singh                      
Github Id :- https://github.com/kyra-09  
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024