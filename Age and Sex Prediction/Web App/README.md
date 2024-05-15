## Web Application for Age and Sex Prediction using Flask

### Goal 🎯
The main goal is to develop a user-friendly web application that predicts age and gender from human images using deep learning models. This application will allow users to upload images and receive predictions.

### Model used for the Web App 🧮
The backend of this web application utilizes Convolutional Neural Networks (CNNs) for age and gender prediction. It has been trained on [UTKFace Dataset](https://www.kaggle.com/datasets/jangedoo/utkface-new) dataset that contains over 20000 facial images for 30 epochs.

Key Details:
* **Model Architecture:** It utilizes Convolutional Neural Network.
* **Data Processing**: Input images are converted to Grayscale images, resized to 128x128 pixels, and normalized.
* **Frameworks and Libraries**: The model is implemented using TensorFlow and Keras for deep learning tasks, and OpenCV for image processing.
* **Model Training**: The model uses categorical cross-entropy loss and Mean Average Error for gender and age respectively and the Adam optimizer. And sigmoid and ReLU activation functions are used for gender and age respectively. It has been trained for 30 epochs.
* **Deployment**: The model is deployed using Flask, providing a web application to interact with the deep learning model efficiently.
This setup enhances user interface allowing real-time predictions.


### Video Demonstration 🎥

[!()](https://github.com/theiturhs/DL-Simplified/assets/96874023/03bdb810-4b52-4606-9bc4-1384fcecb595)

### Signature ✒️
**Shruti Shrivastava**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shrutikshrivastava/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shrutishrivastava22ss@gmail.com)
[![Carrd](https://img.shields.io/badge/carrd-000000?style=for-the-badge&logo=carrd&logoColor=white)](https://theiturhs.carrd.co/)
[![Kaggle](https://img.shields.io/badge/kaggle-0077B5?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/theiturhs)
[![GitHub](https://img.shields.io/badge/github-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/theiturhs)
