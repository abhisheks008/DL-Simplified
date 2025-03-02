# 🎯 Goal
The main goal of the project is to successfully calssify various types of pokemons from the 7000 pokemon images. 

# 🖼️ Dataset
The datset that I have used for the project is taken from the Kaggle website (https://www.kaggle.com/datasets/lantian773030/pokemonclassification/data).Well kaggle is a famous website known for organizing many data science competition and for delivering dataset.

# 🧾 Description
To train my deep learing model I have choose a pre-trainned model which is RESNET-18 to classify pokemon images correctly. RESNET-18 is a famous pre-trainned model which was trainned on large image datasets it was made to solve vanishing gradient problem, well it has 18 layers including convolutional layers and fully connected layers.

# 🧮 What I Had Done
1. ### Data Preprocessing ###
    * I have resized the image into (224, 224) size to match the input size.
    * I have normalized the pixel values in range 0 to 1.
    * I have also randomly rotated the image of about 10 degress and also performed random horizontal flip.

2. ### Model Architecture ###
    * To classify the images I have choose only the RESNET-18 model it has total of 18 layers including convlution layers and fully connected layers it  was trainned on imagenet dataset.

3. ### Model Training ###
    * I have trainned the model over 151 different classes of pokemons.
    * I have evaluate the model on testing dataset to visualize the performance.

4. ### Save the model ###
    * I have saved the models as a pytorch file to reuse it for further classification tasks.

# 📚 Libraries Needed
1. Pytorch.
2. Numpy.
3. Matplotlib.

# Visualization
1.  Pokemon images before normalization. 
    ![](https://github.com/DeXtAr47-oss/DL-Simplified/blob/7ae57bdb8033a7e830809802bad51e94e965d9ec/Pokemon%20classification%20using%20DL/images/Screenshot%20from%202025-02-04%2003-24-18.png)

3. Pokemon images after normalization.
   ![](https://github.com/DeXtAr47-oss/DL-Simplified/blob/7ae57bdb8033a7e830809802bad51e94e965d9ec/Pokemon%20classification%20using%20DL/images/Screenshot%20from%202025-02-04%2003-24-53.png)

4. Accuracy and loss graph.
  ![](https://github.com/DeXtAr47-oss/DL-Simplified/blob/7ae57bdb8033a7e830809802bad51e94e965d9ec/Pokemon%20classification%20using%20DL/images/Screenshot%20from%202025-02-04%2003-25-07.png)
 
# 📈 Model Performance based on Accuracy Scores

| Model    | Accuracy | Loss   |
|----------|----------|--------|
| RESNET-18| 82.62    | 0.7078 |

# 📢 Conclusion And Result
The image classification project  demonstrates effective learning and categorization across 151 classes. The model achieve promising accuracy on both training and testing sets, showcasing the potential for various image processing applications. This project will aid others to use this technology to classifiy pokemon images for their purposes.
    
