# Polyp Segmentation in Endoscopy Images using UNet, ResUNet, and DeepLabV3+ 🏥🔬

This project focuses on the automated segmentation of polyps in endoscopy images using three state-of-the-art deep learning architectures: UNet, ResUNet, and DeepLabV3+. By accurately identifying and delineating polyps, this work aims to assist medical professionals in early detection and prevention of colorectal cancer.

## What is a Polyp? 🔎

Polyps are abnormal tissue growths that arise from mucous membranes, commonly found in organs such as the colon, stomach, and intestines. While many polyps are benign, some can develop into cancer, making early detection and removal crucial for preventing colorectal cancer and other serious conditions.

## Importance of the Subject 💡

Early detection and accurate segmentation of polyps during endoscopy are vital for:
- Preventing colorectal cancer
- Improving patient outcomes
- Reducing the risk of complications

Automated polyp segmentation aids gastroenterologists in identifying and removing polyps efficiently.

## Methods 🛠️

This project utilizes three different architectures for polyp segmentation:
- **UNet**: A convolutional network designed for biomedical image segmentation with an encoder-decoder structure and skip connections.
- **ResUNet**: An extension of UNet with residual blocks for improved feature extraction and segmentation accuracy.
- **DeepLabV3+**: A deep convolutional network that uses atrous spatial pyramid pooling and an encoder-decoder structure for precise segmentation.

## Dataset 📊

The dataset consists of endoscopy images and their corresponding ground truth images, which indicate the presence and location of polyps.

![image](https://github.com/Kaushal-11/HealthLearning/assets/121329391/b9ae85f3-ca1a-4e86-8907-a99db4799245)

### Dataset Details
- **Source**: [CVC-ClinicDB](https://polyp.grand-challenge.org/CVCClinicDB/)
- **Number of Images**: 612
- **Image Format**: .tif 
- **Mask Format**: .tif

## Model Architectures 🏗️

### UNet
- Encoder-decoder structure with skip connections
- Precise localization and segmentation
- Accurate delineation of polyp boundaries

### ResUNet
- Enhanced with residual blocks for better feature extraction
- Improved performance over traditional UNet
- Retains encoder-decoder structure with skip connections

### DeepLabV3+
- Utilizes atrous spatial pyramid pooling for multi-scale feature extraction
- Encoder-decoder structure for detailed segmentation
- Effective for complex segmentation tasks

## Training and Evaluation 📈

### Preprocessing
- Resizing images to a fixed size (256x256)
- Normalizing pixel values (0-255 to 0-1 range)

### Metrics
- Accuracy, recall, and precision
- Logging training progress and metrics to a CSV file

### Thresholding
- Applying a threshold (0.5) to convert probabilities to binary masks

### Evaluation
- Calculating metrics like Accuracy, F1 Score, Jaccard Index (IoU), Recall, Precision

### Visualization
- Visualizing results: Original image | Ground truth mask | Predicted mask

## Results 📊

Detailed results and visualizations are provided for each model, showcasing their performance in polyp segmentation.

### UNet
- **Graph of Training and Validation Loss, Accuracy**:
  ![Training and Validation Loss, Accuracy](https://github.com/Kaushal-11/DL-Simplified/assets/121329391/f7d74bbb-9937-4271-a180-20ff1829902b)
- **Result**:
  ![Result](https://github.com/Kaushal-11/DL-Simplified/assets/121329391/f08c695e-86d1-4867-a9c9-fe92001f4e14)

### ResUNet
- **Graph of Training and Validation Loss, Accuracy**:
  ![Training and Validation Loss, Accuracy](https://github.com/Kaushal-11/DL-Simplified/assets/121329391/6b2fe67d-2222-4dad-ba6d-2326c031250e)
- **Result**:
  ![Result](https://github.com/Kaushal-11/DL-Simplified/assets/121329391/4f61c7d6-e10f-45b3-9c13-c414636ec1d2)

### DeepLabV3+
- **Graph of Training and Validation Loss, Accuracy**:
  ![Training and Validation Loss, Accuracy](https://github.com/Kaushal-11/DL-Simplified/assets/121329391/8288a12a-e16a-45c5-8569-6d3decebe27f)
- **Result**:
  ![Result](https://github.com/Kaushal-11/DL-Simplified/assets/121329391/289c9cfe-15be-444e-8c94-e6c43fc1fdb6)

## Model Performance📊

### U-Net
- **Accuracy:** 0.94052
- **F1 Score:** 0.55769
- **Jaccard Index:** 0.44812
- **Recall:** 0.60501
- **Precision:** 0.61600

### ResUNet
- **Accuracy:** 0.95242
- **F1 Score:** 0.64726
- **Jaccard Index:** 0.53020
- **Recall:** 0.63822
- **Precision:** 0.75802

### DeepLabV3+
- **Accuracy:** 0.94905
- **F1 Score:** 0.58536
- **Jaccard Index:** 0.47407
- **Recall:** 0.52060
- **Precision:** 0.78002

## Conclusion 🎗️

Based on the evaluation metrics, the **ResUNet** model demonstrates the best overall performance for medical image segmentation tasks. The reasons for selecting ResUNet as the best model is as follows,

ResUNet combines the advantages of U-Net with residual connections, which enhance its capability to learn complex features and prevent vanishing gradient issues. This makes ResUNet a robust and efficient choice for high-accuracy medical image segmentation tasks.

