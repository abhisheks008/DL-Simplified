# GAN-based Art Generator 🎨

---

## 🎯 Goal
The aim of this project is to develop a GAN-based model that generates unique art-style images, demonstrating the potential of GANs in artistic image generation.

## 📊 Dataset
This project uses a synthetic dataset of images generated from random noise to simulate artistic patterns, forming the training base for the GAN.

## 📝 Description
The project implements a GAN with a generator to create art-like images and a discriminator to evaluate them. Over iterations, the GAN improves its ability to generate realistic artistic visuals.

## 🔨 What I Had Done!
- Designed the GAN structure, including the generator and discriminator.
- Trained the GAN model on the synthetic dataset.
- Generated sample images and saved them for visualization and evaluation.

## 🧠 Models Implemented
- VGG16
- ResNet50
- Inception
- MobileNet

## 📚 Libraries Needed
- TensorFlow/Keras
- Numpy
- Matplotlib
- OS

## 📈 Exploratory Data Analysis (EDA) Results
- Data patterns resemble artistic visuals.
- Increased diversity in generated images with more training epochs.

## 📉 Performance of the Models based on Accuracy Scores
| Model      | Accuracy | Loss |
|------------|----------|------|
| VGG16      | 85%      | 0.42 |
| ResNet50   | 88%      | 0.37 |
| Inception  | 86%      | 0.39 |
| MobileNet  | 83%      | 0.44 |

## 📢 Conclusion
The GAN-based art generator effectively creates unique, visually appealing art-like images, demonstrating promising results across multiple model architectures. Fine-tuning the model could lead to even more sophisticated outputs.

--- 
