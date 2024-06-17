# 🖼️ Image De-Photobombing Using Deep Learning

This project focuses on removing photobombed elements from images using various techniques, including OpenCV, U-Net, and DeepFillv2 (Gated CNNs). By comparing different methods based on loss metrics, we aim to identify the most effective approach for de-photobombing.

## 📑 Table of Contents

- 🛠️ Installation
- 🚀 Usage
- 📊 Visualizations
- 🧠 Model
- 📈 Results
- 🔍 Conclusions

## 🛠️ Installation

To set up the environment, ensure you have the necessary libraries installed. You can find the required libraries in the `requirements.txt` file. Install them using the following command:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

All the code is provided in the 'ImageDePhotobombing.py' file. Simply run the script to perform de-photobombing using the different methods.

## 📊 Visualizations

This project includes several visualizations to understand and compare the de-photobombing results better:
## 📊 Visualizations

### Original Image vs De-Photobombed Image Using OpenCV
![OpenCV_based](https://github.com/hiteshhhh007/DL-Simplified/assets/115102401/02cee995-c84c-4e09-85f5-fb01d0d865f7)


### Original Image vs De-Photobombed Image Using U-Net
![unet-2](https://github.com/hiteshhhh007/DL-Simplified/assets/115102401/ef96dd50-6825-4982-90b4-d52e0dffe3cf)


### Original Image vs De-Photobombed Image Using DeepFillv2
![Screenshot 2024-05-23 003611](https://github.com/hiteshhhh007/DL-Simplified/assets/115102401/c4072064-dab0-4c20-b2ba-cfc00632bb7a)



## 🧠 Model

Different deep learning models and techniques were used to remove photobombed elements from images, then the best one was chosen based on the loss metrics.

1. **OpenCV Technique:**
   - Uses basic image processing techniques to segment and remove photobombed elements.
   - Utilizes binary masks to identify and cut off unwanted parts from the main image.

2. **U-Net:**
   - **Architecture:** Encoder-Decoder architecture with skip connections to preserve fine details.
   - **Compilation:** Adam optimizer, mean squared error loss function.
   - **Layers:**
     - Input layer with shape (256, 256, 3)
     - Encoder blocks with filters [64, 128, 256, 512]
     - Bottleneck layer with 1024 filters
     - Decoder blocks with filters [512, 256, 128, 64]
     - Output layer with 3 channels and sigmoid activation

3. **DeepFillv2 (Gated CNNs):**
   - **Architecture:** Uses gated convolutions to handle irregular mask shapes and produce high-quality inpainting results.
   - **Compilation:** Adam optimizer, mean squared error loss function.

## 📈 Results

| Technique   | Loss   |
|-------------|--------|
| OpenCV      | 0.0451 |
| U-Net       | 0.0079 |
| DeepFillv2  | 0.0042 |

## 🔍 Conclusions

As the results show, based on the lowest loss value, the DeepFillv2 (Gated CNNs) method is the best technique for de-photobombing.


Overall, DeepFillv2 outperforms other methods by achieving the lowest loss, making it the most effective approach for de-photobombing. 🚀
