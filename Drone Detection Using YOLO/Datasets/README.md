# Drone Detection Dataset
The dataset used here is provided at https://www.kaggle.com/datasets/muki2003/yolo-drone-detection-dataset.

## About Dataset

Read-On Dataset for training yolo drone detection model contain 1012 training image and 347 validation images with annotations. The images are labelled using yolo-labelling and can be directly fed into YOLO architectures.

## How to label Images for Yolo models
We can use any ImageLabelling software or open website tools in order to produce labels for the image in the desired format. One good software available is Roboflow which can be imported as 
```
#follow the link below to get your download code from from Roboflow
!pip install -q roboflow
from roboflow import Roboflow
rf = Roboflow(model_format="yolov5", notebook="roboflow-yolov5")

```
After importing we can do the data labelling by generating an API key and uploading our dataset to their Image object detector and labeller. After that we can download the data as done below:
```
%cd /content/yolov5
#after following the link above, recieve python code with these fields filled in
#from roboflow import Roboflow
#rf = Roboflow(api_key="YOUR API KEY HERE")
#project = rf.workspace().project("YOUR PROJECT")
#dataset = project.version("YOUR VERSION").download("yolov5")

```
The Roboflow generates a Yaml file to work with dataset which can be viewed as::
```
# this is the YAML file Roboflow wrote for us that we're loading into this notebook with our data
%cat {dataset.location}/data.yaml
```
