### **Cyclone Detection**

**Goal** 🎯 : 
The main objective of this project is to detect the intensity of cyclones happening all around the world using satellite image data.

**DATASET** ℹ️ : 
[https://www.kaggle.com/datasets/sshubam/insat3d-infrared-raw-cyclone-images-20132021](url)

**DESCRIPTION**: 
The project consists of an image dataset of cyclones 🌀 containing infrared and raw satellite images from INSAT-3D. It also consists of a **.CSV** file containing the intensity of the cyclones. It comprises a model built using the Inception_v3 model.

**WHAT I HAD DONE** : 

1. Firstly, I had seen the composition of the dataset and came to know it consists of a **.csv** file and **IR** and **raw** satellite images. 
2. Imported the necessary libraries and modules to perform data visualization and build the model.
3. Plotted the 25 Images from the Infrared and Raw Images Dataset using `matplotlib.pyplot.`.Also, the conclusion image is derived from each image (present in the dataset).
4. Build a function to load the images using the `load_img.` function and store it in a list in form of `np.ndarray.`.
5. I created the training dataset using the `ImageDataGenerator.` and `flow_from_directory.` functions.
6. **Model Building**: After creating the training dataset, I build the model using Inception_v3 (Pre Trained model) from `tensorflow.keras.applications.inception_v3.`. Then, I evaluated my model by `.evaluate().` and got a loss of 1.3165.
7. Finally, I saved the model using `save_model.` from the **Keras** **`models.`** module.

**LIBRARIES NEEDED**:

1. **Numpy**
![image](https://user-images.githubusercontent.com/102639355/189530650-ffbb7c60-eaad-4986-9719-6a8d6ec8e278.png)

2. **Pandas**
![image](https://user-images.githubusercontent.com/102639355/189530697-feadc763-3449-46e9-90a4-446535ab703d.png)

3. **Matplotlib**
![image](https://user-images.githubusercontent.com/102639355/189531053-d86db639-e5e8-4922-b6ce-9434b7e1f7bd.png)

4. **Tensorflow**
![image](https://user-images.githubusercontent.com/102639355/189531167-71884461-87de-42a0-80c3-131a08c2b9f9.png)

**CONCLUSION**:
After observing the model, it can be inferred that the model incurred loss (Mean Absolute Error) of around 1.3165 on the training data which is considerably good. At last, model is successfully detecting the intensity of a cyclone from images.

**Contributed By** : 
****ANKIT PANDEY**
You can Connect with me at :
LinkedIn : [www.linkedin.com/in/ankit-pandey-2003ap](url)
Twitter : [https://twitter.com/thecoolpandey](url)