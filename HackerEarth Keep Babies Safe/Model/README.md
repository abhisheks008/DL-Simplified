# KEEP BABIES SAFE MODEL

**GOAL**

Develop a model to classify products into consumer products and toys and Extract and tag brand names of these products from each image. In case no brand names are mentioned, tag it as ‘Unnamed’.

*NOTE* : We can cluster visually similar images (image clustering) together using deep learning and clustering. 

**DATASET**

https://www.kaggle.com/datasets/kunalgupta2616/hackerearth-dl-challenge-keep-babies-safe

**CONTENT**

Data for the case is available in CSV format having 1131 rows and 3 columns.
It also has an images folder containing 1131 images of different products.

**STEPS TAKEN**

All the required libraries and packages were imported and then the required dataset for the project was loaded. 

Basic *EDA* was carried out.

The code uses Resnet50, a pre-trained  CNN, for feature extraction, we remove its topmost/head or the final layer of neurons used for prediction of classes, we then feed our image to the CNN and get a feature vector as an output, which essentially is a flattened array of all the feature maps learned by our CNN at the second last layer of Resnet50. This output vector can be fed into any clustering algorithm ( kmeans(n_cluster = 2) or agglomerative clustering) which classifies our images into the desired number of classes.

Model building was then implemented using different algorithms. Two different OCR libraries were used.

**MODELS USED**

The classification models used are:

1. *PyTesseract*
2. *Keras-OCR*
3. *Agglomerative Clustering*

**THEORY**

Optical Character Recognition (OCR) is the process that converts an image of text into a machine-readable text format. An OCR program extracts and repurposes data from scanned documents, camera images and image-only pdfs. OCR software singles out letters on the image, puts them into words and then puts the words into sentences, thus enabling access to and editing of the original content.

![ocr_flow](https://user-images.githubusercontent.com/86421205/187048138-8663068a-d334-4622-83db-b961cd906e4f.png)

**AGGLOMERATIVE CLUSTERING**

Agglomerative Clustering is a type of *Hierarchical Method* of Clustering which creates a tree-like structure through decomposition. It uses distance between the nearest/farthest points in neighbouring clusters for refinement.

Agglomerative Clustering uses a *bottom-up approach*. It starts with each object forming its own cluster and then iteratively merges the clusters according to their similarity hence forming Large Clusters. It terminates either when all the clusters merge into a single cluster or if a certain clustering threshold is imposed. 

![aglo](https://user-images.githubusercontent.com/86421205/187048328-01fa6042-d37a-40e5-b1cf-157516531bac.jpg)


**LIBRARIES REQUIRED**

* Pandas - for data analysis
* Numpy - for data analysis
* matplotlib - for data visualization
* seaborn - for data visualization
* scikit-learn - for data analysis

**VISUALIZATION**

### Dataset Head snapshot
![Head](https://user-images.githubusercontent.com/86421205/187048338-c7faaf98-e52b-4fb7-b430-ae2958920b29.png)

### Samples
![Sample](https://user-images.githubusercontent.com/86421205/187048354-e883481f-827a-44f7-9afb-5b1d7d0ee986.png)

### RESULT
![tesseract_result](https://user-images.githubusercontent.com/86421205/187048377-240db53f-6736-4a3f-90b6-e0caf5efac34.png)

### EVALUATION OF ACCURACY

*CER* calculation is based on the concept of Levenshtein distance, where we count the minimum number of character-level operations required to transform the ground truth text (aka reference text) into the OCR output.
![image](https://user-images.githubusercontent.com/86421205/187367635-04fe26d9-3ee6-4dcc-bc41-106945ecf1d7.png)

* S = Number of Substitutions
* D = Number of Deletions
* I = Number of Insertions
* N = Number of characters in reference text (aka ground truth)

*Word Error Rate (WER)* might be more applicable if it involves the transcription of paragraphs and sentences of words with meaning (e.g., pages of books, newspapers).

WER operates at the word level instead. It represents the number of word substitutions, deletions, or insertions needed to transform one sentence into another.

WER is generally well-correlated with CER (provided error rates are not excessively high), although the absolute WER value is expected to be higher than the CER value.
![image](https://user-images.githubusercontent.com/86421205/187367946-64620e60-0a11-46e8-994f-880bb8719649.png)

*TESSERACT OCR ACCURACY*
![image](https://user-images.githubusercontent.com/86421205/187368323-84df1c54-9c1b-4f5b-9c8c-a8cdbb5a21ed.png)

![image](https://user-images.githubusercontent.com/86421205/187368447-67bc6929-cd76-4083-b2a1-7bfda7ba74e8.png)

*Keras-OCR*

![image](https://user-images.githubusercontent.com/86421205/187368593-17ce07fc-5a2b-4d18-8104-3d37d8b2da93.png)

**CONCLUSION**

Tesseract OCR has an upper-hand over the keras-ocr mostly for high-resolution images. 

After comparing the CER and WER accuracies of Tesseract OCR and Keras-OCR, we can conclude that for this case Pytesseract will be a better fit as it has a *lower CER and WER* as compared to Keras-OCR, hence *better accuracy*.

# Prajwal Uday

Connect with me on Linkedin: https://www.linkedin.com/in/prajwal-uday-1b9678229/

Check out my Github profile: https://github.com/prajwal-144
