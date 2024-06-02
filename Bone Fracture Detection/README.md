## **Bone Fracture Detection Using Object Detection Algorithms**

### 🎯 **`Goal`**
---
The Goal of the project is to detect Bone fractures in a given X-ray image using state-of-the-art models which are pretrained over huge datasets

### 🧵 **`Dataset`**
---
I have used Bone Fracture Detection dataset of Kaggle

### 🧾 **`Description`** 
---
This Code base implements two object detection models that are used to localize fractures by drawing boxes around them and classify them into appropriate types (as given in the dataset description). These models have the potential to do human level tasks , when trained over large dataset with proper tuning of the parameters.


### 🧮 **`What have I done`**

We used two powerful models for spotting objects: YOLOv8 by Ultralytics and Faster-RCNN by Facebook's Detectron. Each has its own way of handling data and training.

#### **Choosing Models and Getting Data Ready**

- **YOLOv8 (Ultralytics):**
  - It's fast and accurate for spotting objects.
  - The data we had was already in a good format for this model, so we didn't need to do much to it before using it.

- **Faster-RCNN (Facebook's Detectron):**
  - This one is great for detailed object spotting.
  - We had to make sure our data matched up with the annotations required by the model. Detectron helps with this by automatically organizing the annotations.

#### **Getting Data Ready and Training**

- We got our data set up and tweaked it to fit each model's needs.
- YOLOv8 needed less tweaking since our data was already in a good format.
- For Faster-RCNN, we had to make sure the data and annotations were aligned properly, but Detectron helped with this part.

#### **Training and Checking Performance**

- We adjusted settings like how fast the model learns, how many times it looks at the data (epochs), and how much data it looks at each time (batch size).
- Detectron made it easy to see how well our models were doing by automatically checking their performance and storing the best versions.

#### **Sharing the Models**

- Once our models were trained, we saved them in a way that makes them easy to share and use in other places, like pickle files.

By tailoring our approach to each model's requirements and using helpful tools like Detectron, we made the most of YOLOv8 and Faster-RCNN for spotting objects accurately and efficiently.
### 🚀 **`Models Implemented`**
 ---
I have used two different models 
- YOLOv8 Model
- Faster-RCNN pretrained over ResnetXt 


### 📢 **`Conclusion`**
---
In conclusion, our journey in leveraging object detection models, YOLOv8 and Faster-RCNN, has been marked by thorough research and rigorous testing. By aligning data processing with model requirements and optimizing parameters, we achieved efficient and accurate results. Moving forward, exploring diverse hyperparameter tuning strategies and integrating real-time datasets could enhance performance and robustness.

### ✒️  **`Author`**
---
`Bingumalla Likith |
GSSoC 24 Contributor|
Issue Number #457`

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/bingumalla-likith-2633392b9)  [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/binguliki)