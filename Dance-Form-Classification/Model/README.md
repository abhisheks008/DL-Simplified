**PROJECT TITLE**: Dance Form Classification

**GOAL**: Multi-class classification of Indian dance forms.

**DATASET**: [Identify the dance form - Kaggle](https://www.kaggle.com/datasets/singhuday/identifythedanceform)

**DESCRIPTION**:

We have 364 images belonging to 8 Indian dance forms which are all classical in nature, such as Kathakali, Odissi, etc.  
Our aim is to use these limited amount of images to train a deep learning model which can classify them accurately.

**TASKS PERFORMED**:

1. Data exploration and creation of a custom test set using images sampled from the original dataset.  
Final distribution of images: Train - 300, Test - 64 (8 images each for 8 classes)  
2. Trained CNN model from scratch, trying different configurations for number of layers and hidden units.  
3. Added augmentations such as rotation and horizontal flip to data pipeline to artificially increase data size, which  
resulted in significant improvement in performance. Not much improvement after tuning hyperparameters due to limited data.  
4. Used transfer learning techniques to overcome lack of data. Tried five pretrained models as feature-extraction networks  
with a custom classification head. Included the augmentations in data pipeline. Boosted performance further.  
5. Fine-tuned DenseNet201 (best of the 5 feature-extractors) further in two stages. First by unfreezing a few layers and  
training with our images. Then unfreezing the entire network and training with a small learning rate.  
Showed quantitative and qualitative improvements at each stage. Finally, we have a model with more than a 100% improvement  
over our initial CNN model.

**MODELS USED**:

1. Convolution Neural Network ( + Data Augmentations)
2. Transfer-learning Feature-extraction: Xception, ResNet50v2, DenseNet121, Resnet152v2, DenseNet201
3. Transfer-learning Fine-tuning: DenseNet201  

(All Keras implementations)

**LIBRARIES NEEDED**:

1. Numpy
2. Pandas
3. Matplotlib
4. Scikit-learn
5. Keras
6. Tensorflow

**VISUALIZATION**

1. [CNN from scratch + Data augmentations](../Images/01-cnn_from_scratch/) ([Notebook 01](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/blob/dance-form-clf/Dance-Form-Classification/Model/01_cnn_from_scratch.ipynb))
2. [Transfer-learning Feature-extraction](../Images/02-transfer_learning_feature_extraction) ([Notebook 02](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/blob/dance-form-clf/Dance-Form-Classification/Model/02_transfer_learning_feature_extraction.ipynb))
3. [Transfer-learning Fine-tuning](../Images/03-transfer_learning_fine_tuning) ([Notebook 03](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/blob/dance-form-clf/Dance-Form-Classification/Model/02_transfer_learning_fine_tuning.ipynb)) 

**ACCURACIES**:

| **Model configuration**             |    Validation set   |     Test set       |
|:-----------------------------------:|:-------------------:|:--------------:|
| **CNN + Original images**           | 0.33                | 0.41           |
| **CNN + Data Augmentation**         | 0.45                | 0.61           |
| **Xception feature-extractor**      | 0.62                | 0.66           |
| **ResNet50v2 feature-extractor**    | 0.53                | 0.70           |
| **DenseNet121 feature-extractor**   | 0.65                | 0.67           |
| **ResNet152v2 feature-extractor**   | 0.52                | 0.73           |
| **DenseNet201 feature-extractor**   | 0.68                | 0.73           |
| **DenseNet201 fine-tuning Stage-1** | 0.62                | 0.70           |
| **DenseNet201 fine-tuning Stage-2** | 0.72                | 0.75           |
| **DenseNet201 fine-tuning Stage-3** | **0.77**            | **0.83**       |

**CONCLUSION**:

We used a very small number of images to train a deep learning model to classify eight Indian dance forms.  
While conventional deep learning did not give impressive results, we were able to leverage transfer-learning  
techniques to improve performance significantly. Our final model showed stable results with an accuracy of  
**0.77 on the validation set and 0.83 on the test set (more than a 100% increase over our initial baseline)**.

**AUTHOR**:
Siddhant Tiwari  
([Github](https://www.github.com/stiwari-ds) - [Kaggle](https://www.kaggle.com/stiwarids) - [LinkedIn](https://www.linkedin.com/in/stiwari-ds/))
