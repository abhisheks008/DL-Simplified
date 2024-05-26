## **PROJECT TITLE**

### 🎯 **Goal**

 - To create models that can be used to classify Land based on use

### 🧵 **Dataset**

 - https://www.kaggle.com/datasets/apollo2506/landuse-scene-classification/data

### 🧾 **Description**

 - Land Use Classification is a project aimed at categorizing various types of land use in a given geographical area using remote sensing data and advanced machine learning techniques.
 - This project is crucial for urban planning, environmental monitoring, agriculture management, and resource allocation.
 - By accurately classifying land use, stakeholders can make informed decisions regarding sustainable development, conservation efforts, and policy-making.

### 🧮 **What I had done!**

 - I imported 4 pretrained models and changed the final layer to a classification layer and did the training.

### 🚀 **Models Implemented**

 - ResNet101V2
 - ResNet50V2
 - MobileNetV3Large
 - MobileNetV3Small

### 📚 **Libraries Needed**

- pandas
- Pillow
- numpy
- tensorflow
- matplotlib

### 📊 **Exploratory Data Analysis Results**

The dataset includes the following labels:

- airplane
- tenniscourt
- river
- denseresidential
- parkinglot
- storagetanks
- overpass
- sparseresidential
- mediumresidential
- intersection
- baseballdiamond
- runway
- chaparral
- freeway
- beach
- buildings
- harbor
- mobilehomepark
- forest
- golfcourse
- agricultural

#### Dataset Summary

#### Folder: train
- **Total images**: 7350
- **Images per label**: 350 each

#### Folder: test
- **Total images**: 1050
- **Images per label**: 50 each

#### Folder: validation
- **Total images**: 2100
- **Images per label**: 100 each

### 📈 **Performance of the Models based on the Accuracy Scores**

| Rank | Model            | Test Accuracy | Train Accuracy | Validation Accuracy |
|------|------------------|---------------|----------------|---------------------|
| 1    | MobileNetV3Large | 98.38%        | 99.99%         | 99.43%              |
| 2    | ResNet50v2       | 98.19%        | 98.69%         | 97.71%              |
| 3    | MobileNetV3Small | 98.29%        | 99.70%         | 98.38%              |
| 4    | ResNet101v2      | 95.90%        | 99.39%         | 95.81%             


### 📢 **Conclusion**

- **MobileNetV3Large** is the best performer with a test accuracy of 98.38%, showing excellent generalization and overall performance.
- **ResNet50v2** ranks second with 98.19% test accuracy, maintaining a good balance between training and validation accuracies.
- **MobileNetV3Small** follows closely with a 98.29% test accuracy but shows slight overfitting.
- **ResNet101v2** has the lowest test accuracy at 95.90%, indicating overfitting.

#### Recommendation

**MobileNetV3Large** is recommended for its superior accuracy and performance. For efficiency with slightly lower accuracy, **MobileNetV3Small** is a good alternative.

### Social Media

Connect with me on [LinkedIn](https://www.linkedin.com/in/adhithyanvp)

