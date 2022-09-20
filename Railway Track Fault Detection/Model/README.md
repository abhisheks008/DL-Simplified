### **Railway Track Fault Detection**

**Goal** 🎯 : 
The main objective of this project is to detect the fault in railway track using Image classification.

**DATASET** ℹ️ : 
[https://www.kaggle.com/datasets/gpiosenka/railway-track-fault-detection-resized-224-x-224](url)

**DESCRIPTION**: 
As we heard many a times about the Train accidents due to **Track Derailments** in Newspapers, News Channels and Articles. Track Derailments contributes about **7.3 percent** of total train accidents in India. Railway Track Maintainence is an Crucial Part of Safety of People Lives. I have made a project which can predict whether the railway track is defective or not using Deep Learning. 
The project consists of an image dataset of Railway Track in **Train**, **Test** and **Validation** data in two Labels/categories named **Defective** and **Non Defective**. It also consists of a **.CSV** file containing the information regarding number of labels in **Train**, **Test** and **Validation** data. It comprises a CNN Model which can predict whether the input image of Railway Track is Defective or Not.

**WHAT I HAD DONE** : 

1. Firstly, I had imported the necessary libraries and packages required for the project.
2. I looked into the distribution of the labels in Train, Test and Validation Data, used **`.seaborn`** and **`matplotlib.pyplot.`** libraries for plotting and data visualization.
3. Extracting the labels from the dataset.
4. Build a User-defined function for preparation of dataset. 
5. Plotted 15 Images from both labels ***Defective*** and ***Non Defective***.
6. Started the set of train, test and validation data using the user-defined function and made a generator for  the data using `ImageDataGenerator.`
7. Started Building a CNN model using `Sequential.`, grasped the summary of the parameters in the model. Then, I compiled the model taking **Adam** for optimization, **BinaryCrossentropy** as our loss function and    selected **Accuracy** as our metrics.
8. Now, I trained the model with `fit_generator.` library used a `Earlycallback.` to reduce the chance of Overfitting.
9. It's time for the evaluation of the model and for this I used `.evaluate` in `Keras` Library.
10. Predicted the model against the Test Data and store the outputs as a dataframe. Did some analysis on the predictions obtained.
11. Saved the model using `.save` in `keras.models`.
12. Again, Build an Xception model and followed the steps **7-11** on it and got an remarkable accuracy of **`100 %`** which is better than that got with CNN model.

**LIBRARIES NEEDED**:

1. **Numpy**

![image](https://user-images.githubusercontent.com/102639355/189530650-ffbb7c60-eaad-4986-9719-6a8d6ec8e278.png)

2. **Pandas**

![image](https://user-images.githubusercontent.com/102639355/189530697-feadc763-3449-46e9-90a4-446535ab703d.png)

3. **Seaborn**

![image](https://user-images.githubusercontent.com/102639355/190845538-1e81593e-7e98-440e-b6ca-3105aaeffbc3.png)

4. **Matplotlib**

![image](https://user-images.githubusercontent.com/102639355/189531053-d86db639-e5e8-4922-b6ce-9434b7e1f7bd.png)

5. **Tensorflow**

![image](https://user-images.githubusercontent.com/102639355/189531167-71884461-87de-42a0-80c3-131a08c2b9f9.png)


**CONCLUSION**:
After observing the model, it can be inferred that the CNN model incurred **loss (Binary Crossentropy)** of **0.70** with an **accuracy** of around **0.502** (approx.) whereas when an **`Xception`** was used, it got an accuracy of **`100 %`** which is extremely good on this dataset (small in size). Atlast, the model is effectively classifying the Rail Tracks as Defective or Not. 

**Contributed By** : 😄 
**ANKIT PANDEY** 
You can Connect with me at :
LinkedIn : [LinkedIn Profile](www.linkedin.com/in/ankit-pandey-2003ap)
Twitter : [Twitter Handle](https://twitter.com/thecoolpandey)