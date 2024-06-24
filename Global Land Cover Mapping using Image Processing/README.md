# Land Cover Classification

## 📊 Analyzing Dataset

I analyzed the [data set](https://www.kaggle.com/datasets/aletbm/global-land-cover-mapping-openearthmap).
The dataset contains .tif images (geospatial satellite images) and the labels are in colour-coded format.
There are 3 directories under in the data - `test`, `train`, and `val` (stands for validation)
- Training set: Used to train the model.
- Validation set: Used to evaluate the model during training and tune hyperparameters.
- Test set: Used to evaluate the model's performance after training is complete.

**This is an image present in the dataset under the directory images/train**

![Screenshot from 2024-05-18 19-19-43](https://github.com/abhisheks008/DL-Simplified/assets/146760434/82b95f82-e6b5-4265-89d6-e97c12b849dd)

**Each image has 3 layers (RGB), so below are the layers of the above image:**

Red Channel
![Screenshot from 2024-05-18 19-20-01](https://github.com/abhisheks008/DL-Simplified/assets/146760434/ec853ed6-b71c-4bbe-93ee-58ecce692b45)

Green Channel
![Screenshot from 2024-05-18 19-20-09](https://github.com/abhisheks008/DL-Simplified/assets/146760434/6e521154-e053-455d-9846-b7e324a8ec1e)

Blue Channel
![Screenshot from 2024-05-18 19-20-16](https://github.com/abhisheks008/DL-Simplified/assets/146760434/77b834e0-ea67-4a78-9917-144f9f9f39df)

**There is a corresponding label/train which has 1 layer with coloured label**

Colour(Hex)  | Class|
-------------|----------|
#800000	     |	Bareland |
#00FF24	     |	Rangeland |
#949494	     |	Developed space |
#FFFFFF	     |	Road |
#226126	     |	Tree |
#0045FF	     |	Water |
#4BB549	     |	Agriculture land |
#DE1F07	     |	Building |

![Screenshot from 2024-05-18 19-20-38](https://github.com/abhisheks008/DL-Simplified/assets/146760434/f87a5c3e-2ad7-495d-8472-aee35c3e30e8)

## 🧵 Clustering (using DBScan)

Label displaying class 2 (Rangeland)
![Screenshot from 2024-05-31 10-43-17](https://github.com/abhisheks008/DL-Simplified/assets/146760434/cd5a808e-760d-465d-877e-a85fe76979e8)

Clusters drawn on the label using DBScan
![Screenshot from 2024-05-31 10-44-34](https://github.com/abhisheks008/DL-Simplified/assets/146760434/096187d0-1fcb-489c-9161-d28ca9d8d6c1)

Drawing bounding boxes around clusters
![Screenshot from 2024-06-01 11-00-27](https://github.com/abhisheks008/DL-Simplified/assets/146760434/a9867f79-698b-48ef-8751-cf118fb138a5)

So, the `clustering.py` file draws clusters for each class and makes bounding boxes around them. The coordinates of the boxes are used to generate labels and these labels are converted into YOLO format for training.
The YOLO format labels are then converted into Pascal VOC format for RetinaNet training.

## 🚀 MODELS USED

 1.  **YOLOv5(You Only Look Once, version 5):** This model is chosen for land cover classification due to its high accuracy and efficiency. Designed for real-time classification, it is ideal for applications requiring quick and precise results. YOLOv5's CNN architecture effectively learns and identifies spatial patterns, ensuring robust classification of various land cover types. Its end-to-end learning approach simplifies the classification pipeline, enhancing performance and reliability.

 2. **RetinaNet:** RetinaNet is chosen for land cover classification due to its high accuracy and robustness. It is designed for real-time classification, making it ideal for applications requiring precise results. RetinaNet's Focal Loss function effectively handles class imbalance, ensuring accurate classification of diverse land cover types. Its deep learning architecture captures intricate spatial patterns, enhancing performance and reliability.
 
 3. **VGG16:** VGG16 is chosen for landcover detection due to its pre-trained architecture on ImageNet, deep layers for learning intricate patterns, availability in frameworks like TensorFlow, and suitability for transfer learning, enabling effective model training even with limited data.

## 🧮  Exploratory Data Analysis Results

#### YOLOv5 Model:

![yolo_f1_curve](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/yolo_F1_curve.png)

![yolo_confusion_matrix](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/yolo_confusion_matrix.png)

![yolo_labels](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/yolo_labels.jpg)

![yolo_results](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/yolo_results.png)

#### RetinaNet Model:

![retinanet_epoch_loss](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/retinanet_epoch_loss.png)

![retinanet_epoch_mAP](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/retinanet_epoch_mAP.png)

![retinanet_regression_loss](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/retinanet_regression_loss.png)

## 📈 Performance of the Models based on the Accuracy Scores
The evaluation metrics I used to assess the models were epoch loss

| Model      | Epoch Loss |
|------------|----------|
| YOLOv5    | 0.020     |
| RetinaNet    | 7.188 |
| VGG16   |    -     |

## 📢 Conclusion
Based on the results we can draw the following conclusions:
1. **YOLOv5:** The YOLOv5 model had an epoch loss of 0.020. This loss was lower compared to RetinaNet, hence it outperformed the RetinaNet model. I could use my GPU to train this model as it ised 3.07GB out of the 4GB memory my system has. I was able to train with 5000 epochs on my terminal and 100 epochs in jupyter notebook.

2. **RetinaNet:** I was successfully able to train YOLO using my GPU. However, that was not the case with RetinaNet. My GPU ran out of memory so I had to train this model using CPU.It could train to a maximum of 10 epochs using CPU. This had an epoch loss of 7.188. This was higher than the YOLOv5 model.  

3. **VGG16:** I initially attempted to use VGG as one of my models. However, later in the process, I realized that VGG was ideal for object detection and not classification. Therefore, this model would work properly only if there was 1 class. But, in my case, I had 9 classes (including 'Null' as a class), so I could not continue using this model.
