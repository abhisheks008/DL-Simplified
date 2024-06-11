# Skin Lesion Image Classification

## 🎯 Goal
The main purpose of this project is to **classify between different skin lesions such as Melanoma , Melanocytic nevus , Basal cell carcinoma etc** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/salviohexia/isic-2019-skin-lesion-images-for-classification**

## 🧾 Description

This project involves the comparative analysis of **Five** Keras image detection models, namely **MobileNetV2** , **ResNet50V2** , **InceptionV3** , **DenseNet121** and **Xception**  applied to a specific dataset. The dataset consists of annotated images related to a particular domain, and the objectives include training and evaluating these models to compare their accuracy scores and performance metrics. Additionally, exploratory data analysis (EDA) techniques are employed to understand the dataset's characteristics, explore class distributions, detect imbalances, and identify areas for potential improvement. The methodology encompasses data preparation, model training, evaluation, comparative analysis of accuracy and performance metrics, and visualization of EDA insights. 

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

![alt text](../Images/Xception_predictions/82a7a436-1879-44ca-8b62-3ca9ffc81fc1.png)</br>

![alt text](../Images/Xception_predictions/8a31b924-8aae-4773-9b1f-e96e5eccf2d8.png)</br>

![alt text](../Images/Xception_predictions/e228703d-a012-46bf-9176-8b95e206a7c9.png)</br>

![alt text](../Images/Xception_predictions/e513cfae-9fb4-4089-b382-ec9f5dfeeca7.png)</br>



### MobileNetV2

Incorporating the MobileNetV2 model into our codebase brings a wealth of advantages to our image processing workflows. By initializing the pre-trained MobileNetV2 model with weights from the ImageNet dataset, we tap into its profound understanding of visual data.

**Reasons for selecting MobileNetV2:**

- Lightweight Architecture (MobileNetV2's efficient design allows for quick processing with minimal computational resources.)
- Proven Accuracy (MobileNetV2 consistently performs well in various image recognition benchmarks, balancing accuracy and speed.)
- Reduced Parameters (3.4M, significantly fewer than many other models, enabling faster inference and reduced memory usage.)
- High Efficiency (CPU - 5, GPU - 1.4, making it highly suitable for deployment on resource-constrained devices.)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/MobileNetV2_predictions/94d85fd8-e41e-4b6e-bbea-8018e30dc41f.png)</br>

![alt text](../Images/MobileNetV2_predictions/a2b36fa1-7611-4492-a89f-f229528a11e7.png)</br>


![alt text](../Images/MobileNetV2_predictions/ad2cdd88-15cc-495e-bf9e-78cecb7b763a.png)</br>


![alt text](../Images/MobileNetV2_predictions/c7940184-ec89-4478-991f-aaa8e7e8f69d.png)</br>



### ResNet50V2

Implementing transfer learning with the ResNet50V2 model allows us to benefit from pre-trained weights, significantly reducing the training duration necessary for image classification tasks. This strategy is particularly advantageous when dealing with limited training data, as we can leverage the comprehensive representations learned by the base model from extensive datasets like ImageNet.

**Reasons for opting for ResNet50V2:** Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/Resnet50V2_predictions/0c43d4e1-cd17-4cf2-842d-e4b0dc6a65d2.png)</br>

![alt text](../Images/Resnet50V2_predictions/32f9234a-a912-4f29-9035-1d552b00e01f.png)</br>

![alt text](../Images/Resnet50V2_predictions/a6d974c3-445f-4a6c-bb6c-bbdb21cea904.png)</br>

![alt text](../Images/Resnet50V2_predictions/bb484090-43dd-47d7-9e99-a8a9d58672af.png)</br>




### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/InceptionV3_predictions/65d94200-3a53-4b44-8444-bd64f52630e3.png)</br>

![alt text](../Images/InceptionV3_predictions/a5b82a5f-d123-4ced-b3e4-db220f42b7ff.png)</br>

![alt text](../Images/InceptionV3_predictions/bd45fce8-a6ea-4b0c-979a-96c53f88be5a.png)</br>

![alt text](../Images/InceptionV3_predictions/f761cd91-7790-43b7-96f3-7a9361e7f70a.png)</br>



### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet121/1d6bee1c-8aa1-4f63-9850-77629d02dc8d.png)</br>

![alt text](../Images/DenseNet121/d0100609-bf58-45ef-a80f-227faf9c5781.png)</br>

![alt text](../Images/DenseNet121/fa275f84-dbe2-45f2-b34a-ca0b0897443f.png)</br>

![alt text](../Images/DenseNet121/fb7e6471-f268-4c15-be40-3f5ad694321e.png)</br>



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

![alt text](../Images/pie_chart.png)

### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.


![alt text](../Images/image_path_distribution.png)


## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  | 74% ( Validation Accuracy: 0.7427)|
|InceptionV3  | 73% (Validation Accuracy:0.7266) |
|DenseNet121     | 72% (Validation Accuracy:0.7193) |
|ResNet50V2  | 71% (Validation Accuracy:0.7149) |
|MobileNetV2   | 55% (Validation Accuracy:  0.5570) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that Xception and InceptionV3 were able to perform good on this dataset.**

For this particular dataset as we can see from bar chart the data per class varies in size by a lot which makes the data a bit inconsistent affecting the accuracy of the models. With this inconsistent dataset using even with optimization techniques the most accuracy I could get is approx 70% with all the models which is described to be a good accuracy for data this inconsistent.

## ✒️ Your Signature

Full name:-Aaradhya Singh                      
Github Id :- https://github.com/aaradhyasinghgaur </br>
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024