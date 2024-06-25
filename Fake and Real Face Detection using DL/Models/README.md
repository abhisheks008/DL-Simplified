# Fake-VS-Real Face Detection

## 🎯 Goal
The main purpose of this project is to **detect and classify between real and fake faces** from the dataset (mentioned below) using various image detection/recognition models and comparing their accuracy.

## 🧵 Dataset

The link to the dataset is given below :-

**Link :- https://www.kaggle.com/datasets/hamzaboulahia/hardfakevsrealfaces**

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

![alt text](../Images/Xception_predictions/613de73b-43d0-4fde-91d4-6d618db7a7b5.png)</br>

![alt text](../Images/Xception_predictions/bfcf4aa0-1697-4043-881d-4555b4ec6477.png)</br>

![alt text](../Images/Xception_predictions/c7076c59-4507-4da1-967a-14c4b104a2d6.png)</br>

![alt text](../Images/Xception_predictions/f34c78bb-57d9-40c8-a851-0639ee25fdf1.png)




### DenseNet169

Incorporating the DenseNet169 model into our codebase brings a wealth of advantages to our image processing workflows. By initializing the pre-trained DenseNet169 model with weights from the ImageNet dataset, we tap into its profound understanding of visual data.

**Reasons for selecting DenseNet169:**
- Deep Architecture (DenseNet169's deeper network allows for learning complex patterns and features in images.)
- Proven Accuracy (DenseNet169 consistently ranks high in various image recognition benchmarks.)
- Extensive Parameters (14.3M)
- Robust Efficiency (CPU - 40, GPU - 12)

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet169_predictions/558d4761-1128-48d5-a7ea-db7be6523d6e.png)</br>

![alt text](../Images/DenseNet169_predictions/967037c6-cb62-4580-a16c-e29a3267000f.png)</br>

![alt text](../Images/DenseNet169_predictions/dfbb22ef-7ddd-4549-8ab6-17c330160711.png)</br>

![alt text](../Images/DenseNet169_predictions/fa526a44-08d3-4909-998f-03f2f70cf82b.png)



### ResNet50V2

Implementing transfer learning with the ResNet50V2 model allows us to benefit from pre-trained weights, significantly reducing the training duration necessary for image classification tasks. This strategy is particularly advantageous when dealing with limited training data, as we can leverage the comprehensive representations learned by the base model from extensive datasets like ImageNet.

**Reasons for opting for ResNet50V2:** Relatively lightweight (98 MB) , High Accuracy (92.1 % Top 5 accuracy), Moderate Parameters (25.6M) , Reasonable Inference Speed on GPU (CPU - 32.1, GPU - 4.7)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/Resnet50V2_predictions/121d3148-317f-4790-be95-5ae133948f75.png)</br>

![alt text](../Images/Resnet50V2_predictions/28c4d1c4-c37c-4468-ae6f-af44fc5ef0e1.png)</br>

![alt text](../Images/Resnet50V2_predictions/49ff56f9-48b5-4a9d-9649-262b69f43ec9.png)</br>


![alt text](../Images/Resnet50V2_predictions/a5fb6340-bf31-46c2-8022-2d6bce1ebabe.png)


### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. 

**Reason for choosing :-** 
lightweighted (92 MB) , better accuracy , less parameters (23.9M) , less inference speed (CPU - 42.2 , GPU - 6.9)

Visualization of Predicted Labels on test set :- </br>
![alt text](../Images/InceptionV3_predictions/588c82f0-dd69-403b-b821-56e9ddd52b0b.png)</br>

![alt text](../Images/InceptionV3_predictions/82f201cf-1b42-4746-9972-cadd52694cbd.png)</br>


![alt text](../Images/InceptionV3_predictions/d377c3b7-db8d-4ae9-8599-38e8f995c022.png)</br>

![alt text](../Images/InceptionV3_predictions/fdb31897-a278-4d40-ba96-19d3fe817c00.png)



### DenseNet121

When implementing the DenseNet121 model in code, we leverage its densely connected architecture to enhance our image classification tasks. By loading the pre-trained DenseNet121 model with weights from the ImageNet dataset, we benefit from its extensive knowledge.

**Reason for choosing:** Lightweight (33 MB)
, High accuracy , Moderate number of parameters (8M) , Efficient inference speed (CPU - ~45 ms, GPU - ~10 ms).

Visualization of Predicted Labels on test set :- </br>

![alt text](../Images/DenseNet121/46ff97c0-cad9-4916-ba31-565f7ff2ae0e.png)</br>

![alt text](../Images/DenseNet121/98cc9ef2-237f-4c40-953e-ecd31c0f4a2c.png)</br>

![alt text](../Images/DenseNet121/c242d566-fcc2-4ba7-ac0a-c860991d23e7.png)</br>

![alt text](../Images/DenseNet121/ef81aca5-1b84-4144-8e32-1fbe009cbfe9.png)






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


![alt text](../Images/image_path.png)



## 📈 Performance of the Models based on the Accuracy Scores

| Models      |       Accuracy Scores|
|------------ |------------|
|Xception  |99% ( Validation Accuracy: 0.9914)|
|InceptionV3  | 96% (Validation Accuracy:0.9569) |
|DenseNet121     | 98% (Validation Accuracy:0.9828) |
|ResNet50V2  | 99% (Validation Accuracy:0.9914) |
|DenseNet169    | 99% (Validation Accuracy: 0.9914) |


## 📢 Conclusion

**According to the accuracy scores it can be concluded that Xception , ResNet50V2 and DenseNet169 were able to perform good on this dataset.**

Even though all of  the models implemented above are giving above 90% accuracy which is great when it comes to image recognition.

## ✒️ Your Signature

Full name:-Aaradhya Singh                      
Github Id :- https://github.com/kyra-09  
Email ID :- aaradhyasinghgaur@gmail.com  
LinkdIn :- https://www.linkedin.com/in/aaradhya-singh-0b1927250/ </br>
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024