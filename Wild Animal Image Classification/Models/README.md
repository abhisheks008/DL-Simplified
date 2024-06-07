# Insect Detection and Classification using DL

## 🎯 Goal
The main purpose of this project is to **identify and classify different wild animals such as tiger , hyena , lion , fox etc.** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/whenamancodes/wild-animals-images**

## 🧾 Description

This project involves the comparative analysis of **Five** Keras image detection models, namely **DenseNet169** , **ResNet50V2** , **InceptionV3** , **DenseNet121** and **Xception**  applied to a specific dataset. The dataset consists of annotated images related to a particular domain, and the objectives include training and evaluating these models to compare their accuracy scores and performance metrics. Additionally, exploratory data analysis (EDA) techniques are employed to understand the dataset's characteristics, explore class distributions, detect imbalances, and identify areas for potential improvement. The methodology encompasses data preparation, model training, evaluation, comparative analysis of accuracy and performance metrics, and visualization of EDA insights. 

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
![alt text](../Images/Xception_predictions/2452c871-86ea-4f08-9f4e-1bb3e41cfb3d.png)</br>

![alt text](../Images/Xception_predictions/41921a4a-2f65-4dd0-8634-f52ffaffb6de.png)</br>

![alt text](../Images/Xception_predictions/568e7211-0eaa-4ba5-a872-dde8cb534372.png)</br>

![alt text](../Images/Xception_predictions/d3cd5bf1-38cd-43ab-88fe-4251288fe88d.png)</br>


### DenseNet169

Incorporating the DenseNet169 model into our codebase brings a wealth of advantages to our image processing workflows. By initializing the pre-trained DenseNet169 model with weights from the ImageNet dataset, we tap into its profound understanding of visual data.

**Reasons for selecting DenseNet169:**
- Deep Architecture (DenseNet169's deeper network allows for learning complex patterns and features in images.)
- Proven Accuracy (DenseNet169 consistently ranks high in various image recognition benchmarks.)
- Extensive Parameters (14.3M)
- Robust Efficiency (CPU - 40, GPU - 12)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/DenseNet169_predictions/39be4709-81c1-4e47-a160-e826084b3565.png)</br>

![alt text](../Images/DenseNet169_predictions/49094e58-a086-48f2-82c3-d3369adc8fdc.png)</br>

![alt text](../Images/DenseNet169_predictions/818ee25a-af56-4dc5-b2d6-a39786e8335c.png)</br>

![alt text](../Images/DenseNet169_predictions/a7731182-5c50-4e63-b1bf-000a71086768.png)</br>


### ResNet50V2

Implementing transfer learning with the ResNet50V2 model allows us to benefit from pre-trained weights, significantly reducing the training duration necessary for image classification tasks. This strategy is particularly advantageous when dealing with limited training data, as we can leverage the comprehensive representations learned by the base model from extensive datasets like ImageNet.

**Reasons for opting for ResNet50V2:** Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/Resnet50V2_predictions/288b503e-ad83-4756-9f84-345513c03188.png)</br>

![alt text](../Images/Resnet50V2_predictions/695db48c-a679-45e1-b856-e9e9bdf61e95.png)</br>

![alt text](../Images/Resnet50V2_predictions/838d663e-91d8-4a4c-9746-5c79a4dc9d35.png)</br>

![alt text](../Images/Resnet50V2_predictions/bf7eaef2-7a16-4dba-9d7b-c7861ac1e154.png)


### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/InceptionV3_predictions/0164b9bf-bd42-4d79-ba7e-0260a2a3eb0c.png)</br>

![alt text](../Images/InceptionV3_predictions/4a7026fa-0867-4596-805c-08f93bfb02f1.png)</br>

![alt text](../Images/InceptionV3_predictions/66a827a9-fac6-4633-a815-d01ad8f36718.png)</br>


![alt text](../Images/InceptionV3_predictions/90b2d288-e6e1-4b2b-bebc-9c70eb67dab4.png)</br>


### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet121/56103b40-5077-4054-bb55-51f1e20763c4.png)</br>

![alt text](../Images/DenseNet121/8669099f-0c8f-44fc-90e0-6de2a77aa054.png)</br>

![alt text](../Images/DenseNet121/ace4ba51-00c2-4744-9624-725601d95f43.png)</br>

![alt text](../Images/DenseNet121/dbe2b5af-fbfd-47ba-b969-b7eb0d73edf5.png)</br>



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


![alt text](../Images/bar.png)</br>

### Pie Chart :-
A pie chart illustrating the distribution of labels in the training dataset. The percentage value displayed on each segment indicates the relative frequency of each label category.

![alt text](../Images/pie.png)</br>

### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.


![alt text](../Images/image_path_distribution.png)


## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |100% ( Test Accuracy: 100.00%)|
|InceptionV3  | 99% (Test Accuracy: 99.81%) |
|DenseNet121     | 100% (Test Accuracy: 100.00%) |
|ResNet50V2  | 99% (Test Accuracy: 99.81%) |
|DenseNet169    | 99% (Test Accuracy: 99.42%) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that Xception and InceptionV3 were able to perform good on this dataset.**

Even though most of  the models implemented above are giving above 90% accuracy which is great when it comes to image recognition.

## ✒️ Your Signature

Full name:-Aaradhya Singh                      
Github Id :- https://github.com/kyra-09  
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024