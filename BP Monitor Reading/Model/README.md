<h3>BP Monitor Reading</h3>
<p><h4>## Aim: Create a DL model, which will monitor the reading given in the images and identify them.<h4></p>

<p><h4>## Approach</h4>
We implemented three different models to identify the readings:<br>
1.Custom CNN<br>
2.ResNet50 (Transfer Learning)<br>
3.RNN with CNN features</p>

<p><h4>## Exploratory Data Analysis (EDA)</h4>
The dataset consists of images of BP monitor readings. We performed EDA to understand the data distribution and characteristics.<br>
Each image is annotated with bounding boxes indicating the reading areas.</p>

<h4>## Models</h4>

<h4>## 1.Custom CNN</h4>
<p>
Architecture: 3 convolutional layers, 2 dense layers.<br>
Training: 20 epochs, Adam optimizer, Mean Squared Error loss.<br>
Performance: Training accuracy: 0.80, Validation accuracy: 0.84.</p>

<h4>## 2.ResNet50 <br></h4>
<p>Architecture : Pre-trained ResNet50 with custom top layers.
Training: 20 epochs, Adam optimizer, Mean Squared Error loss.<br>
Performance: Training accuracy: 0.91, Validation accuracy: 0.84.</p>

<h4>## 3.CNN with RNN</h4>
<p>
Architecture: Convolutional layers followed by LSTM layers.<br>
Training: 20 epochs, Adam optimizer, Mean Squared Error loss.<br>
Performance: Training accuracy: 0.82, Validation accuracy: 0.78.</p>

<h4>## Results</h4>

Based on the training and validation accuracies of the models:<br>
<p>
1.The Custom CNN model achieved a final training accuracy of 78.12% and a validation accuracy of 84.38%.<br>
2.The ResNet50 model achieved a final training accuracy of 90.62% and a validation accuracy of 84.38%.<br>
3.The RNN with CNN features model achieved a final training accuracy of 82.03% and a validation accuracy of 78.12%.
</p>
<h4>## Key Observations</h4>
<p>
1.Model Performance: The ResNet50 model performed the best overall, achieving the highest training accuracy among the three models. However, both the Custom CNN and ResNet50 models achieved the same validation accuracy, indicating similar generalization performance on unseen data.
</p>
<p>2.Complexity vs. Performance: The ResNet50 model, being a deeper and more complex architecture, achieved higher training accuracy compared to the Custom CNN and RNN with CNN features models. This suggests that the additional complexity of the ResNet50 architecture can capture more intricate patterns in the data, leading to improved performance.
</p> 
<p>3.Training vs. Validation: All models achieved higher training accuracies compared to validation accuracies, indicating some degree of overfitting. Regularization techniques such as dropout or weight decay could be explored to mitigate overfitting and potentially improve validation performance.
</p>
<p>4.Computational Efficiency: While the ResNet50 model achieved the highest accuracy, it also requires significantly more computational resources due to its deeper architecture and larger number of parameters. The Custom CNN model, being simpler, may offer a good balance between performance and computational efficiency for certain applications.
</p>
<p>In summary, while the ResNet50 model demonstrated superior performance in terms of training accuracy, both the Custom CNN and ResNet50 models showed comparable validation accuracies. The choice between these models would depend on factors such as computational resources, performance requirements, and the specific characteristics of the dataset and task at hand.
</p>
