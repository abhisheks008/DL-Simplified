### Chocolate Classification using DL

## 🎯 Goal
The objective is to categorize the chocolate depicted in the image as either **dark** chocolate or **white** chocolate.

## 🧵 DATASET
Here is the link to the dataset utilized in this project👇:<br>
https://www.kaggle.com/datasets/siddharthmandgi/chocolate-classification

## 🧾 DESCRIPTION
This project is designed to discern the subtle differences between white chocolate and dark chocolate within images. It has undergone training utilizing a comprehensive dataset consisting of various images depicting both white chocolate and dark chocolate, enabling it to accurately classify chocolate types in unseen images with precision and reliability.

## 🧮 WHAT I HAD DONE
1. **Data collection:** Initially, data was collected from the provided dataset link to ensure a diverse range of samples for analysis.<br>
2. **Data preprocessing:** Images underwent preprocessing to standardize dimensions, ensuring uniformity across the dataset. Labels were checked for appropriate extensions and then Label Encoded from categorical to numerical counterparts.<br>
3. **Model selection:** Traditional CNNs were combined with advanced architectures such as VGG16 and ResNet50 to capitalize on their effectiveness in image detection. CNN with Attention was also implemented by adding probability distribution into the training process.<br>
4. **Comparative analysis:** Models were evaluated based on accuracy scores, facilitating a nuanced understanding of their performance for informed decision-making.

## 🚀 **Models Implemented**
The following models have been incorporated in developing this project:
1. **CNN**<br>
2. **VGG16**<br>
3. **ResNet50**<br>
4. **CNN with Attention**

## 📚 LIBRARIES NEEDED
The following libraries are necessary to execute this project:
1. numpy==1.24.3
2. pandas==1.5.0
3. matplotlib==3.6.0
4. tensorflow==2.6.0

## 🖼️ VISUALIZATION

### CNN
<img src="https://github.com/abhisheks008/DL-Simplified/blob/main/Chocolate%20Classification%20using%20DL/Images/acc_cnn.jpg" alt="Image1" >

### RESNET50
<img src="https://github.com/abhisheks008/DL-Simplified/blob/main/Chocolate%20Classification%20using%20DL/Images/acc_resnet50.jpg" alt="Image2">

### VGG16
<img src="https://github.com/abhisheks008/DL-Simplified/blob/main/Chocolate%20Classification%20using%20DL/Images/acc_vgg16.jpg" alt="Image3" >

### CNN with Attention
<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_chocolate_detect/Chocolate%20Classification%20using%20DL/Images/acc_CNN-Attention.png" alt="Image4" >

## 📋 EVALUATION METRICS
The evaluation metrics that have been used to assess the models are:
- Accuracy<br> 
- Loss

## 📈 **Performance of the Models based on the Accuracy Scores**
Results on dataset is as follows:
| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.861     | 0.218   |
| VGG16    | 0.722     | 1.341    |
| ResNet50    | 0.917     | 0.251    |
| CNN (Attention)    | 0.97     | 0.388    |

## 📢CONCLUSION
1. The CNN model achieved a higher accuracy **(0.861)** and relatively low loss **(0.218)**, demonstrating *strong performance* in distinguishing between images of dark and white chocolate.
2. VGG16 exhibited lower accuracy **(0.722)** compared to CNN, indicating it *might not* be the most suitable model for this particular chocolate detection task. Nonetheless, it still showed predictive capability.
3. ResNet50 demonstrated a higher accuracy **(0.917)** among the models, highlighting its *effectiveness* in differentiating between dark and white chocolate images. Furthermore, it displayed a low loss value **(0.251)**, indicating *robust convergence* during training.
4. The CNN model with Attention mechanism achieved the highest accuracy **(0.97)** and relatively low loss **(0.388)**, demonstrating *strong performance* and indicated *robust convergence* in distinguishing between images of dark and white chocolate.

## Your Signature
README enhanced by: Mahi Singh [https://github.com/mahi13singh2004]
Model and README enhanced by: Arihant Bhandari [https://github.com/Arihant-Bhandari]