# Insect Detection and Classification using DL

## 🎯 Goal
The main purpose of this project is to **identify and classify different insects such as moth , butterfly , scorpion , grasshopper etc.** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/vencerlanz09/insect-village-synthetic-dataset**

## 🧾 Description

This project involves the comparative analysis of **Five** Keras image detection models, namely **ResNet101V2** , **ResNet50V2** , **InceptionV3** , **DenseNet121** and **Xception**  applied to a specific dataset. The dataset consists of annotated images related to a particular domain, and the objectives include training and evaluating these models to compare their accuracy scores and performance metrics. Additionally, exploratory data analysis (EDA) techniques are employed to understand the dataset's characteristics, explore class distributions, detect imbalances, and identify areas for potential improvement. The methodology encompasses data preparation, model training, evaluation, comparative analysis of accuracy and performance metrics, and visualization of EDA insights. 

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
![alt text](../Images/Xception_predictions/35d1cedc-35ce-4b22-8902-0e910812e0f0.png)</br>

![alt text](../Images/Xception_predictions/4cf60ed1-2d77-47f6-92b0-36d8aa288246.png)</br>

![alt text](../Images/Xception_predictions/630a36ad-e213-4bff-b3bd-196f8735c95e.png)</br>

![alt text](../Images/Xception_predictions/c4c6adf8-d347-4a62-9ec1-6b1163dcaf02.png)



### ResNet101V2

Incorporating the ResNet101V2 model into our codebase brings a wealth of advantages to our image processing workflows. By initializing the pre-trained ResNet101V2 model with weights from the ImageNet dataset, we tap into its profound understanding of visual data.

**Reasons for selecting ResNet101V2:**
- Deep Architecture (ResNet101V2's deeper network allows for learning complex patterns and features in images.)
- Proven Accuracy (ResNet101V2 consistently ranks high in various image recognition benchmarks.)
- Extensive Parameters (44.5M)
- Robust Efficiency (CPU - 50, GPU - 15)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/ResNet101V2_predictions/1a2bbd11-337c-4763-b853-9c34877eaab3.png)

![alt text](../Images/ResNet101V2_predictions/776d63f5-4fd0-41fc-bfd2-90ea5872f76b.png)

![alt text](../Images/ResNet101V2_predictions/9b8bd6b4-b5cb-4c8c-ad12-29aca4d74d00.png)

![alt text](../Images/ResNet101V2_predictions/ead5d95c-7b1f-4e59-a9c6-f28e56c574c0.png)



### ResNet50V2

Implementing transfer learning with the ResNet50V2 model allows us to benefit from pre-trained weights, significantly reducing the training duration necessary for image classification tasks. This strategy is particularly advantageous when dealing with limited training data, as we can leverage the comprehensive representations learned by the base model from extensive datasets like ImageNet.

**Reasons for opting for ResNet50V2:** Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/Resnet50V2_predictions/3ea9611d-9697-460b-bfaf-4c418cee524c.png)</br>

![alt text](../Images/Resnet50V2_predictions/7098ef1d-a285-437a-a23a-d4cf99d385a9.png)</br>

![alt text](../Images/Resnet50V2_predictions/8f659648-c411-4792-a3fc-3a3116a9ab57.png)</br>

![alt text](../Images/Resnet50V2_predictions/b3f8ba55-849c-47b6-b705-59fe79005f17.png)





### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/InceptionV3_predictions/28c05d19-f793-4a18-859a-13e8e68756b5.png)</br>

![alt text](../Images/InceptionV3_predictions/3df0fda8-f842-4a34-91c5-4687e1112e14.png)</br>

![alt text](../Images/InceptionV3_predictions/68e783d1-408d-4314-8b3c-a9c1439a6494.png)</br>

![alt text](../Images/InceptionV3_predictions/8a4134d7-8ad2-4eac-a738-b3453efded17.png)



### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet121/1cce4d35-a9e2-49e6-bec1-8f540ef6c640.png)</br>

![alt text](../Images/DenseNet121/aedd4d8a-e516-42a4-b16b-1a063173efaa.png)</br>

![alt text](../Images/DenseNet121/e0e74036-b174-421c-9222-757ca1059eb7.png)</br>

![alt text](../Images/DenseNet121/ef9173f3-63b2-4119-ad96-81a93c4c1aac.png)

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

![alt text](../Images/pie_chart.png)

### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.


![alt text](../Images/image_path_distribution.png)

## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |97% ( Validation Accuracy: 0.9680)|
|InceptionV3  | 96% (Validation Accuracy: 0.9650) |
|DenseNet121     | 95% (Validation Accuracy:0.9520) |
|ResNet50V2  | 92% (Validation Accuracy: 0.9220) |
|ResNet101V2     | 90% (Validation Accuracy: 0.9010) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that Xception , InceptionV3 and DenseNet121 were able to perform good on this dataset.**

Even though most of  the models implemented above are giving above 90% accuracy which is great when it comes to image recognition.

## ✒️ Your Signature

Full name:-Aaradhya Singh                      
Github Id :- https://github.com/kyra-09  
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024