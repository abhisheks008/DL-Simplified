# Rick and Morty Character Image Detection #462

## Objective
Testing various pre-trained such as **VGG16** , **MobileNetV2** and **InceptionV3** models to train , validate and finally predict the **Rick and Morty Image detection dataset** .

**Done By -**              
Full name:- AaradhyaSingh                      
Github Id :- https://github.com/kyra-09  
Email ID :- aaradhyasinghgaur@gmail.com  
Participant Role :- Contributor / GSSOC (Girl Script Summer of Code ) - 2024

## Approach For This Project

Trained the dataset on various models , each of their summary is as follows :-

### InceptionV3
When implementing the InceptionV3 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionV3 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. To fine-tune the model for our specific dataset, we freeze the layers to preserve the learned representations.With its exceptional performance on image classification, InceptionV3 serves as an excellent choice for deep learning practitioners seeking accurate and efficient models.


### VGG16
I will utilize the VGG16 (Visual Geometry Group) architecture, which have deeper and complex structures. These models are renowned for their exceptional performance on various image recognition tasks. By leveraging the pre-trained weights of VGG, I can benefit from the learned features and fine-tune the network for image segmentation on the Rick na Morty Image Detection dataset.   
(I trained the VGG16 model using a dataset of 1000 images due to CPU constraints and validated its performance on a smaller set of 50 images.)


### MobileNetV2
Utilizing transfer learning with the MobileNetV2 model allows us to leverage pre-trained weights, drastically reducing the training time needed for image classification tasks. This strategy is especially beneficial when working with limited training data, as we can capitalize on the comprehensive representations learned by the base model from a vast dataset such as ImageNet.

## Accuracy Result
| Model  | Accuracy |
|--------|----------|
| InceptionV3 |  97 | 
| VGG16       |  88 | 
| MobileNetV2 |  97 | 

## Conclusion

**InceptionV3 and MobileNetV2 works better with highest accuracy. (considering I only used few image dataset for VGG16 and all for the above two.)**
