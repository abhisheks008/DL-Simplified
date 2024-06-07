### Original source: [Identify the dance form - Kaggle](https://www.kaggle.com/datasets/singhuday/identifythedanceform)

### Alternate source (used in notebooks): [Download link - GCP Bucket](https://storage.googleapis.com/dance-forms-dataset/dance_forms.zip)

* Test set in original dataset has no associated labels. We have discarded it.
* Train set in original dataset has 364 images belonging to 8 classes.  
A custom test set is created by picking 8 images for each class, resulting in 64 images.  
The new distribution is: Train - 300, Test - 64. 
