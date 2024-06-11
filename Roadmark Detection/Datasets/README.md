<h1> About the Dataset </h1>

Kaggle link: https://www.kaggle.com/datasets/pkdarabi/road-mark-detection






<h3> Overview </h3>


In recent years, advancements in computer vision and deep learning have revolutionized the field of object detection, enabling a wide range of applications in various domains. One crucial application is road safety, where accurate and efficient object detection plays a vital role in preventing accidents and improving traffic management. To address the challenges unique to this domain, researchers and developers have created specialized datasets tailored specifically for road-related object detection tasks. Among these datasets, the ROAD MARK Dataset is a comprehensive and valuable resource for training and evaluating object detection models.

The ROAD MARK Dataset is a curated collection of annotated images and videos focusing on detecting and classifying road markings and related objects. It encompasses a diverse range of scenarios encountered on roads, including highways, urban streets, and rural areas, making it highly representative of real-world conditions. The dataset includes various types of road markings, such as lane lines, arrows, pedestrian crossings, speed limit signs, and other relevant objects like traffic lights and barriers.

This dataset contains 2892 samples, which are correctly divided into three parts: Train, Valid, and Test.

<h3> Dataset Structure </h3>


The dataset is organized as follows:

    Train: Contains the training images.
    Valid: Contains the validation images.
    Test: Contains the test images.

<h3> Data Configuration File </h3>


The dataset includes a data.yaml file for training models. Below is the content of the file:

yaml

train: ../train/images
val: ../valid/images
test: ../test/images

nc: 13
names: ['BUS LANE', 'Jeltaya razmetka', 'Liniya 1', 'Liniya 2', 'Perehod', 'Romb', 'SLOW', 'Strelka vlevo', 'Strelka vpered', 'Strelka vpered - vlevo', 'Strelka vpered - vpravo', 'Strelka vpravo', 'Velosiped']

<h5> Annotations </h5>


    nc: Number of classes (13)
    names: List of class names

<h3> License </h3>


The dataset is available under the CC BY 4.0 license.
Roboflow Integration

The dataset is hosted on Roboflow and can be accessed using the following details:

    Workspace: lr-tdx
    Project: road-mark
    Version: 3
    URL: Roboflow ROAD MARK Dataset

<h3> Usage </h3>


To use this dataset for training your object detection models:

    Download the dataset from the provided URL.
    Configure your training pipeline using the data.yaml file.
    Ensure your model reads the training, validation, and test images from the specified directories.
