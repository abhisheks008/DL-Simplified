# Model: Component-Based Hybrid GAN

This directory contains the core implementation of the facial restoration model.

## Architecture Overview

The system employs a **Hybrid GAN** approach specifically tuned for facial features:

### 1. Generator (U-Net with Residual Learning)
- **Structure**: Symmetric U-Net with skip connections to preserve spatial information.
- **Residual Learning**: Instead of generating the image directly, the model learns a *residual map* ($R$) such that $Restored = Distorted + R$. This ensures that the global structure is maintained while the network focuses on adding missing high-frequency details.

### 2. Global Discriminator
- A PatchGAN-based discriminator that evaluates the realism of the entire 256x256 facial image.
- Ensures global consistency, skin texture realism, and lighting coherence.

### 3. Local Feature Discriminator
- Specifically focuses on three critical patches: **Eyes, Nose, and Mouth**.
- By operating on higher-resolution crops of these features, it enforces the restoration of fine details like eyelashes, iris patterns, and lip texture.

### 4. Identity Preserving Module
- Uses a pre-trained VGG-16 network (trained on ImageNet/Face datasets) as a feature extractor.
- Computes the **Identity Loss** (Cosine Similarity) between the features of the restored image and the ground truth.
- Ensures the restored person remains recognizable as the original subject.

## Files
- `distorted_restore.ipynb`: The master notebook containing the entire training and evaluation pipeline.
- `best_model.pth`: (Download Required) Pre-trained weights for the Hybrid GAN.

## Model Weights
The pre-trained model weights (`best_model.pth`) are too large (~660MB) to be hosted directly on GitHub. 

**Download Link**: [Download best_model.pth from Hugging Face](https://huggingface.co/Flash-00007/SocialFace-Restore-GAN/resolve/main/best_model.pth)

Place the downloaded `.pth` file inside this `Model/` directory before running the inference notebook.

## Requirements
Refer to the `requirements.txt` in the project root for installation. Key libraries include `torch`, `torchvision`, `lpips`, `opencv-python`, and `skimage`.
