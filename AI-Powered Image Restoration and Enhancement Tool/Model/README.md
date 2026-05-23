# AI-Powered Image Restoration and Enhancement Tool

## Overview
This project implements an AI-powered pipeline for image restoration and enhancement using 4 deep learning models.

## Models Used
- **DnCNN** - Image Denoising
- **SRCNN** - Super Resolution  
- **U-Net** - Image Colorization
- **ESRGAN** - Enhanced Super Resolution (4x)

## Dataset
- **BSD300** (Berkeley Segmentation Dataset)
- URL: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/
- 300 natural images (200 train / 100 test)

## Metrics
- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)
- MSE (Mean Squared Error)

## Requirements
- PyTorch
- OpenCV
- scikit-image
- matplotlib
- pandas

## How to Run
Open the notebook in Google Colab and run all cells sequentially.
