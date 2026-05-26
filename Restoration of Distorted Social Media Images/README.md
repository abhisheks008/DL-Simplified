## **Restoration of Distorted Social Media Images (Facial Features Only)**

### 🎯 **Goal**

The primary objective of this project is to restore high-fidelity facial features (eyes, nose, mouth) in images degraded by social media platform processing, motion blur, and sensor noise. It aims to achieve perceptual realism while strictly preserving the subject's unique identity.

### 🧵 **Dataset**

The project utilizes high-quality facial datasets to generate paired training data via synthetic distortion:
- **Faces Dataset (Small)**: A sample dataset used for demonstration, automatically downloaded via `kagglehub`. [Link](https://www.kaggle.com/datasets/tommykamaz/faces-dataset-small)

### 🧾 **Description**

Images on social media often suffer from quality degradation due to aggressive lossy compression, low-resolution sensors, and environmental factors like motion blur. This project implements a **Component-Based Hybrid GAN** architecture to restore sharp facial features. Unlike standard global restoration models, this system leverages specialized discriminators for local facial components and an identity-consistency module to ensure the output remains recognizable as the original subject.

### 🧮 **What I had done!**

- **Synthetic Distortion Pipeline**: Developed a module to apply randomized JPEG compression, Gaussian blur, and additive noise to clean images, creating paired training data on-the-fly.
- **Hybrid GAN Implementation**: Architected a 4-model system using PyTorch, featuring a deep U-Net generator and multi-scale discriminators.
- **Residual Enhancement**: Configured the generator to learn a correction map (residual) added to the input image, preserving structural integrity while recovering high-frequency details.
- **Perceptual and Identity Loss Integration**: Integrated VGG-based feature matching and identity-consistency losses to optimize for human-perceived quality rather than just pixel-wise accuracy.
- **Evaluation Framework**: Built a validation pipeline using PSNR, SSIM, and LPIPS metrics to quantify restoration performance.

### 🚀 **Models Implemented**

- **Generator (U-Net)**: A symmetric encoder-decoder with skip connections. Chosen to preserve spatial details from the input while the residual learning approach ensures stable training for restoration tasks.
- **Global Discriminator (PatchGAN)**: Evaluates the realism of the full 256x256 image. Chosen for its ability to model local textures across the entire facial surface.
- **Local Feature Discriminator**: A specialized network focusing on high-detail regions (eyes, nose, mouth). Chosen to enforce fine-grained realism in the most perceptually critical facial areas.
- **Identity Preserver**: A frozen VGG-16 backbone used as a feature extractor. Chosen to calculate identity-consistency loss, ensuring the restored face matches the ground truth in high-level feature space.

### 📚 **Libraries Needed**

- `torch` & `torchvision` (Model implementation and training)
- `opencv-python` (Image processing and synthetic distortion)
- `numpy` (Mathematical operations)
- `scikit-image` (Metric calculation)
- `lpips` (Learned Perceptual Image Patch Similarity metric)
- `kagglehub` (Automated dataset acquisition)
- `matplotlib` (Visualization of results and curves)
- `tqdm` (Training progress monitoring)

### 📊 **Exploratory Data Analysis Results**

Initial analysis involves monitoring the distribution of synthetic distortions across facial patches. Training performance is tracked through:
- **Loss Curves**: Monitoring the adversarial balance between the generator and dual discriminators.
- **Metric Tracking**: Real-time evaluation of PSNR, SSIM, and LPIPS during the training process.
- **Qualitative Inspection**: Generation of image grids comparing distorted inputs, restored outputs, and ground truth targets (saved in the `Images/` directory).

### 📈 **Performance of the Models based on the Accuracy Scores**

The restoration quality is quantified using standard perceptual metrics:
- **PSNR (Peak Signal-to-Noise Ratio)**: Target > 28dB for high-fidelity reconstruction.
- **SSIM (Structural Similarity Index)**: Target > 0.85 for structural preservation.
- **LPIPS (Learned Perceptual Similarity)**: Target < 0.15 for high human-perceived realism.

*The Component-Based Hybrid GAN consistently outperforms basic U-Net models by achieving lower LPIPS scores, indicating superior texture recovery in critical facial regions.*

### 📢 **Conclusion**

The Component-Based Hybrid GAN effectively addresses the limitations of global image restoration by prioritizing perceptually critical facial features. The integration of local discriminators and identity-preserving losses ensures that the restoration is not only sharp but also identity-consistent. Based on the LPIPS and SSIM scores, the hybrid architecture is the optimal choice for social media image restoration where human perception is the primary evaluation criterion.

### ✒️ **Your Signature**

Gurijala Dheeraj Reddy
[GitHub/dheeraj00001](https://github.com/dheeraj00001)
