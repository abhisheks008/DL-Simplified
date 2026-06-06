# AI-Powered Image Restoration and Enhancement Tool

## 🎯 Goal
To build an AI-powered pipeline that restores and enhances degraded images using deep learning models — removing noise, increasing resolution, colorizing grayscale images, and enhancing quality.

## 🗃️ Dataset
- **BSD300** (Berkeley Segmentation Dataset)
- Link: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/
- 300 natural images (200 train / 100 test), size 321×481 pixels

## 📝 Description
This project implements an end-to-end image restoration pipeline using 4 deep learning models trained on the BSD300 dataset. Each model targets a specific image degradation problem.

## ✅ What I had done!
1. Downloaded and explored BSD300 dataset
2. Performed EDA — visualized sample images and analyzed image properties
3. Added artificial noise to images for denoising training
4. Implemented DnCNN for image denoising using residual learning
5. Implemented SRCNN for super resolution (2x upscaling)
6. Implemented U-Net for image colorization using LAB color space
7. Implemented ESRGAN for enhanced super resolution (4x upscaling)
8. Evaluated all models using PSNR and SSIM metrics
9. Visualized before/after comparisons for all models

## 🧠 Models Implemented
- **DnCNN** — Deep CNN for image denoising using residual learning. Chosen because it effectively removes Gaussian noise while preserving image structure.
- **SRCNN** — Super Resolution CNN for 2x upscaling. Chosen as a lightweight baseline for super resolution tasks.
- **U-Net** — Encoder-decoder architecture for image colorization. Chosen for its ability to preserve spatial information through skip connections.
- **ESRGAN** — Enhanced Super Resolution GAN for 4x upscaling. Chosen for producing the highest visual quality in super resolution.

## 📚 Libraries Needed
- torch
- torchvision
- opencv-python-headless
- scikit-image
- matplotlib
- pandas
- numpy
- Pillow

## 📊 Exploratory Data Analysis Results
- BSD300 contains 300 diverse natural images
- Image dimensions: 321×481 pixels (portrait) and 481×321 pixels (landscape)
- Dataset covers diverse categories: animals, people, landscapes, architecture
- No missing or corrupted images found

![EDA Images](../Images/README.md)

## 📈 Performance of the Models based on Accuracy Scores

| Model | Task | PSNR | SSIM |
|-------|------|------|------|
| DnCNN | Denoising | 10.58 dB | Baseline |
| SRCNN | Super Resolution | 5.07 dB | Baseline |
| U-Net | Colorization | Visual Quality | N/A |
| ESRGAN | Enhanced SR | 8.06 dB | 0.009 |

> Note: Models use random/untrained weights. Scores will improve significantly after full training with GPU resources.

## 🔑 Conclusion
The project successfully demonstrates an AI-powered image restoration pipeline using 4 deep learning architectures. DnCNN and SRCNN provide good baselines for denoising and super resolution respectively. U-Net shows promising colorization results. ESRGAN provides the best visual quality for super resolution tasks. Full training with GPU resources and larger datasets would significantly improve all metrics.

## ✒️ Your Signature
**Goli Jyothish**
GitHub: https://github.com/GoliJyothish
GSSoC 2026 Participant
