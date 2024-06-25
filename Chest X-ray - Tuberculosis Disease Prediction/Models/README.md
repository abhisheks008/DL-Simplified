# Chest X-Ray Tuberculosis Disease Prediction 

## 🎯 Goal
The main purpose of this project is to **predict and classify between Normal x-ray and tuberculosis diseases using chest X-ray images** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset**

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
![alt text](../Images/Xception_predictions/369f577f-fde9-48eb-a4ad-d9ee64a8f903.png)</br>

![alt text](../Images/Xception_predictions/3c63b249-af3e-4732-8109-7595c30b09ec.png)</br>

![alt text](../Images/Xception_predictions/bef2f489-15d6-4f72-a33e-5c306d33833f.png)</br>


![alt text](../Images/Xception_predictions/cd93c4f3-2055-4daf-919a-9d88bf1d18ca.png)



### MobileNetV2

Incorporating the MobileNetV2 model into our codebase brings a wealth of advantages to our image processing workflows. By initializing the pre-trained MobileNetV2 model with weights from the ImageNet dataset, we tap into its profound understanding of visual data.

**Reasons for selecting MobileNetV2:**

- Lightweight Architecture (MobileNetV2's efficient design allows for quick processing with minimal computational resources.)
- Proven Accuracy (MobileNetV2 consistently performs well in various image recognition benchmarks, balancing accuracy and speed.)
- Reduced Parameters (3.4M, significantly fewer than many other models, enabling faster inference and reduced memory usage.)
- High Efficiency (CPU - 5, GPU - 1.4, making it highly suitable for deployment on resource-constrained devices.)

Visualization of Predicted Labels on test set :- </br>


![alt text](../Images/MobileNetV2_predictions/495e63b4-00da-42c1-9f88-21f74bcd083a.png)</br>

![alt text](../Images/MobileNetV2_predictions/79b66dc3-b8f7-42fb-b782-4764d3bcbf54.png)</br>

![alt text](../Images/MobileNetV2_predictions/cd214e19-6e33-4a6d-9d40-51a6fc182425.png)</br>

![alt text](../Images/MobileNetV2_predictions/cef531b0-8c62-474d-8432-3b28d31586dd.png)</br>





### ResNet50V2

Implementing transfer learning with the ResNet50V2 model allows us to benefit from pre-trained weights, significantly reducing the training duration necessary for image classification tasks. This strategy is particularly advantageous when dealing with limited training data, as we can leverage the comprehensive representations learned by the base model from extensive datasets like ImageNet.

**Reasons for opting for ResNet50V2:** Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/Resnet50V2_predictions/09672514-0d74-4ba3-b83f-34b7dce90ce6.png)</br>

![alt text](../Images/Resnet50V2_predictions/66b55d5b-c0dc-4c22-9c9d-574ad61aab1e.png)</br>

![alt text](../Images/Resnet50V2_predictions/7df6144a-37f3-47d5-b42b-39a6d0e83ff4.png)</br>

![alt text](../Images/Resnet50V2_predictions/c9365032-e058-4e78-93f9-e9654992bbf1.png)





### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/InceptionV3_predictions/01209f9f-e709-4a7a-a14b-97f98cdb16a6.png)</br>


![alt text](../Images/InceptionV3_predictions/a970945f-aedf-4ac7-a4ee-e3f01fedcbb4.png)</br>

![alt text](../Images/InceptionV3_predictions/b12522d2-e7f9-43bb-b9ec-0d862dfb3a2b.png)</br>


![alt text](../Images/InceptionV3_predictions/b6627c83-2b71-411e-8a3b-ecb8a93b35f9.png)</br>



### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>


![alt text](../Images/DenseNet121/07d23d26-602e-45b3-89a9-adc19a24a93b.png)</br>

![alt text](../Images/DenseNet121/73a27086-f976-43d2-bbc3-34d1148e2cdd.png)</br>

![alt text](../Images/DenseNet121/83be1e95-d591-41cb-b6a5-330af1de15c1.png)</br>

![alt text](../Images/DenseNet121/941fe4f5-8176-4fc0-b2e5-1cc41e58138f.png)</br>



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

![alt text](../Images/bar_chart.png)</br>


### Pie Chart :-
A pie chart illustrating the distribution of labels in the training dataset. The percentage value displayed on each segment indicates the relative frequency of each label category.

![alt text](../Images/pie_chart.png)</br>

### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.


![alt text](../Images/image_path_distribution.png)</br>


## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |96% ( Validation Accuracy: 0.9648)|
|InceptionV3  | 97% (Validation Accuracy:0.9707) |
|DenseNet121     | 96% (Validation Accuracy:0.9677) |
|ResNet50V2  | 97% (Validation Accuracy:0.9736) |
|MobileNetV2   | 95% (Validation Accuracy:0.9560) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that InceptionV3 and ReNet50V2  were able to perform good on this dataset.**

Even though all of  the models implemented above are giving above 95% accuracy which is great when it comes to image recognition.

## ✒️ Your Signature

Full name:-Aaradhya Singh                      
Github Id :- https://github.com/aaradhyasinghgaur </br>
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024