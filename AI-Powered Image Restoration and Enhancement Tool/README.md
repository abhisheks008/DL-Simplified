# AI-Powered Image Restoration and Enhancement Tool

## 🎯 Aim
To build an AI-powered pipeline that restores and enhances degraded images using deep learning models.

## 📌 Description
This project implements 4 deep learning models for image restoration:
- **DnCNN** — Image Denoising
- **SRCNN** — Super Resolution
- **U-Net** — Image Colorization
- **ESRGAN** — Enhanced Super Resolution (4x)

## 📊 Dataset
- **BSD300** (Berkeley Segmentation Dataset)
- 300 natural images (200 train / 100 test)
- URL: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/

## 🧠 Models Used
| Model | Task | Metric |
|-------|------|--------|
| DnCNN | Image Denoising | PSNR, SSIM |
| SRCNN | Super Resolution | PSNR, SSIM |
| U-Net | Colorization | Visual Quality |
| ESRGAN | Enhanced SR (4x) | PSNR, SSIM |

## 🚀 How to Run
Open the notebook in Google Colab and run all cells sequentially.

## 📁 Project Structure
AI-Powered Image Restoration and Enhancement Tool/
├── Dataset/
│   └── README.md
├── Images/
│   └── README.md
├── Model/
│   ├── AI_Powered_Image_Restoration_and_Enhancement_Tool.ipynb
│   └── README.md
├── README.md
└── requirements.txt

## ✍️ Author
**Goli Jyothish**
GitHub: https://github.com/GoliJyothish
