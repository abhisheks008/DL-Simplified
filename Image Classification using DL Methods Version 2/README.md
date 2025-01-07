## **Image Classification using Convolutional Neural Networks**

### 🎯 **Goal**

To implement and compare various convolutional neural network (CNN) architectures for image classification tasks using the CIFAR-10 and MNIST datasets, analyzing their efficiency and accuracy.

### 🧵 **Dataset**

- **CIFAR-10 Dataset:** [Link to CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- **MNIST Dataset:** [Link to MNIST Dataset](http://yann.lecun.com/exdb/mnist/)

### 🧾 **Description**

This project involves the implementation of different CNN models to classify images from the CIFAR-10 and MNIST datasets accurately. The models range from simple architectures suitable for educational purposes to complex networks designed for high accuracy on larger, more complex datasets.

### 🧮 **What I had done!**

1. **Dataset Preparation:**
   - Loaded and preprocessed the CIFAR-10 and MNIST datasets (normalization, resizing, etc.).
2. **Model Implementation:**
   - Implemented several CNN architectures (LeNet-5, MobileNet, ResNet50, Simple CNN, VGG16).
3. **Training and Validation:**
   - Trained each model on the training datasets.
   - Validated the models on the validation datasets.
4. **Performance Evaluation:**
   - Evaluated model performance using accuracy, precision, recall, and F1-score.

### 🚀 **Models Implemented**

1. **LeNet5_Model**
   - Chosen for its simplicity and historical significance in CNN development, particularly for digit recognition tasks such as MNIST.
2. **MobileNet_Model**
   - Selected for its efficiency in mobile and embedded applications, utilizing depthwise separable convolutions, tested on both CIFAR-10 and MNIST.
3. **ResNet50_Model**
   - Implemented for its deep architecture and residual connections, solving the vanishing gradient problem, evaluated on CIFAR-10.
4. **Simple_CNN_Model**
   - Used as a basic model to understand CNN architecture and its implementation, tested on both CIFAR-10 and MNIST.
5. **VGG16_Model**
   - Included for its deep architecture with small 3x3 convolutions and proven performance on complex datasets like CIFAR-10.

### 📚 **Libraries Needed**

- TensorFlow/Keras
- PyTorch
- NumPy
- Pandas
- Matplotlib
- scikit-learn

### 📈 **Performance of the Models based on the Accuracy Scores**

- **LeNet5_Model:** 
  - CIFAR-10: Accuracy - `0.5802000000%`
  - MNIST: Accuracy - `0.9862000000%`
- **MobileNet_Model:** 
  - CIFAR-10: Accuracy - `0.5521000000%`
  - MNIST: Accuracy - `0.9843000000%`
- **ResNet50_Model:** 
  - CIFAR-10: Accuracy - `0.3908000000%`
  - MNIST: Accuracy - `0.9789000000%`
- **Simple_CNN_Model:** 
  - CIFAR-10: Accuracy - `0.6947000000%`
  - MNIST: Accuracy - `0.9929000000%`
- **VGG16_Model:** 
  - CIFAR-10: Accuracy - `0.7196000000%`
  - MNIST: Accuracy - `0.9919000000%`

### 📢 **Conclusion**

From the results obtained, it is evident that different CNN architectures perform variably on the CIFAR-10 and MNIST datasets due to their unique design and complexity. Here are the key observations and conclusions derived from this project:

1. **Simple_CNN_Model**:
   - Achieved the highest accuracy on the MNIST dataset (99.29%), making it the most suitable for this specific task.
   - Also performed well on the CIFAR-10 dataset (69.47%), showcasing its robustness and versatility.

2. **VGG16_Model**:
   - Attained the highest accuracy on the CIFAR-10 dataset (71.96%), indicating its effectiveness for more complex image classification tasks.
   - Also showed strong performance on the MNIST dataset (99.19%).

3. **LeNet5_Model**:
   - Performed exceptionally well on the MNIST dataset (98.62%) due to its design tailored for digit recognition.
   - However, it was less effective on the CIFAR-10 dataset (58.02%), which is expected given its simpler architecture.

4. **MobileNet_Model**:
   - Showed decent performance on both CIFAR-10 (55.21%) and MNIST (98.43%), highlighting its efficiency and suitability for mobile applications despite slightly lower accuracy.

5. **ResNet50_Model**:
   - Surprisingly, had the lowest accuracy on the CIFAR-10 dataset (39.08%) among all models tested, possibly due to overfitting or insufficient training epochs.
   - Achieved a good accuracy on the MNIST dataset (97.89%), but it was outperformed by simpler models in this context.

In conclusion, the **Simple_CNN_Model** and **VGG16_Model** stood out as the best performers for MNIST and CIFAR-10 respectively. The **Simple_CNN_Model** is highly recommended for simpler tasks like digit recognition, while the **VGG16_Model** is better suited for more complex image classification tasks. Despite the lower accuracy, **MobileNet_Model** offers a good balance between performance and computational efficiency, making it ideal for deployment in resource-constrained environments. The results also highlight the importance of selecting the appropriate architecture based on the specific dataset and task at hand.

### ✒️ **Your Signature**

**Utsav Singhal**  
[LinkedIn](https://www.linkedin.com/in/utsavsinghal2604/) | [GitHub](https://github.com/UTSAVS26) | [Email](mailto:utsavsinghal26@gmail.com)
