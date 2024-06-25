# Indian Medicinal Plants Classification

## 🎯 Goal
The main purpose of this project is to **identify and classify between different indian medicinal plants such as aloevera , hibiscus and tulsi etc.** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/crypticfate5/medicinal-plants**

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

![alt text](../Images/Xception_predictions/523a81d5-cad5-4ad5-8207-8f933a87eeec.png)</br>

![alt text](../Images/Xception_predictions/8de97206-d7ab-4f34-953c-6bba8ca20234.png)</br>

![alt text](../Images/Xception_predictions/aec75c37-8d34-4746-b6e7-ab5235933268.png)</br>

![alt text](../Images/Xception_predictions/cf8e5164-d831-4bea-846c-5d76fc4fe3a8.png)

### MobileNetV2

Incorporating the MobileNetV2 model into our codebase brings a wealth of advantages to our image processing workflows. By initializing the pre-trained MobileNetV2 model with weights from the ImageNet dataset, we tap into its profound understanding of visual data.

**Reasons for selecting MobileNetV2:**

- Lightweight Architecture: MobileNetV2's efficient design allows for rapid processing with fewer computational resources, making it ideal for deployment on mobile and embedded devices.
- Proven Accuracy: MobileNetV2 consistently performs well in various image recognition benchmarks, providing reliable and accurate results.
- Efficient Parameters: With 3.4M parameters, MobileNetV2 offers a good balance between model complexity and performance.
- High Efficiency: MobileNetV2 is optimized for speed, with a CPU efficiency of 6.1 and a GPU efficiency of 0.27, making it suitable for real-time applications.

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/MobileNetV2_predictions/9835610b-40ec-481a-9795-05c7fcd488fe.png)</br>

![alt text](../Images/MobileNetV2_predictions/9cbece09-ccb7-4302-a631-ad2461e8d073.png)</br>

![alt text](../Images/MobileNetV2_predictions/c873dbf7-0da8-42b4-a031-88745143368c.png)</br>

![alt text](../Images/MobileNetV2_predictions/eba505d6-96a4-4c1c-ae27-264e595419c4.png)




### ResNet50V2

Implementing transfer learning with the ResNet50V2 model allows us to benefit from pre-trained weights, significantly reducing the training duration necessary for image classification tasks. This strategy is particularly advantageous when dealing with limited training data, as we can leverage the comprehensive representations learned by the base model from extensive datasets like ImageNet.

**Reasons for opting for ResNet50V2:** Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/Resnet50V2_predictions/065094e9-6db8-4b82-b07c-97b33c12b04f.png)</br>

![alt text](../Images/Resnet50V2_predictions/160ea5fc-29db-404d-b38a-91bfde62c2bf.png)</br>

![alt text](../Images/Resnet50V2_predictions/3de06cdb-6173-4762-9ae8-ee6dff90fe70.png)</br>

![alt text](../Images/Resnet50V2_predictions/df005ad8-5a46-4cff-8e0b-3f7f54d2004e.png)



### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/InceptionV3_predictions/548927e9-6e23-44d7-91aa-14b4182a6e41.png)</br>

![alt text](../Images/InceptionV3_predictions/842d172b-d11a-4689-841b-f4f05ee77f2f.png)</br>

![alt text](../Images/InceptionV3_predictions/bf0ca2a7-656f-4300-994b-0cd8c3b032f8.png)</br>

![alt text](../Images/InceptionV3_predictions/e062f6a1-b369-46f2-b5ec-dc504c46933c.png)</br>

### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet121/2d6feef4-0905-4770-b3b7-19b11d2f81be.png)</br>
![alt text](../Images/DenseNet121/7c28ea47-6af4-40a8-b7f7-8fb40c897205.png)</br>
![alt text](../Images/DenseNet121/9276ea47-e4cc-4453-8c9f-c4c129c53e8f.png)</br>
![alt text](../Images/DenseNet121/a6658123-1644-4ddb-9fbb-3a66895d4495.png)


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


![alt text](../Images/pie_chart.png) </br>


### Image paths distribution :-
 Visualizes the distribution of top 20 image paths by label, displays unique values in categorical columns.



![alt text](../Images/image_path_distribution.png) </br>



## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |93% ( Validation Accuracy:0.9356)|
|InceptionV3  | 88% (Validation Accuracy: 0.8838) |
|DenseNet121     | 92% (Validation Accuracy:0.9203) |
|ResNet50V2  | 85% (Validation Accuracy: 0.8569) |
|MobileNetV2    | 86% (Validation Accuracy: 0.8636) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that  Xception and DenseNet121 were able to perform good on this dataset.**

Even though I haven't trained the models on entire dataset because of computational restraints . I only trained the models on 10% of the entire dataset. 

## ✒️ Your Signature

Full name:-Aaradhya Singh                      
Github Id :- https://github.com/kyra-09  
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024