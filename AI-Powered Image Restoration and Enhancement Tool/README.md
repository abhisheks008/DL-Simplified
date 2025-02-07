# AI-Powered Image Restoration and Enhancement Tool

## Project Description
This project aims to develop an **AI-Powered Image Restoration Tool** that revitalizes low-quality historical photos by upscaling, denoising, and adding realistic color. Using advanced deep learning techniques, it transforms degraded images into vibrant, high-quality visuals while preserving their historical context. This tool is perfect for heritage conservation, family archiving, and historical documentation.

## Tech Stack
- **Programming Language**: Python
- **Libraries**:
  - OpenCV: For image processing tasks
  - Pillow: For handling image files
  - PyTorch: For implementing deep learning models
  - torchvision: For image transformations and model utilities
- **Models**:
  - SRCNN (Super-Resolution Convolutional Neural Network): For image upscaling
  - DnCNN: For image denoising
  - Pre-trained colorization models (e.g., U-Net): For adding color to grayscale images


## Methodology

- **Advanced Image Processing Techniques**: Utilizes state-of-the-art methods like Non-Local Means denoising and deep learning models for image super-resolution, denoising, and colorization.
- **Super-Resolution**: Enhances image clarity and resolution using models like SRCNN, providing high-resolution outputs from low-quality images.
- **Denoising**: Removes unwanted noise with Non-Local Means or advanced denoising networks, preserving image details and texture.
- **Colorization**: Adds vibrant colors to grayscale images through deep learning techniques, making them visually appealing and realistic.
- **User-Friendly and Robust**: Includes comprehensive error handling, ensuring smooth processing and clear feedback for image handling issues.
- **Before-and-After Comparison**: Stacks input and output images for easy visualization of restoration and enhancement effects.

This project is ideal for applications in digital media restoration, enhancing low-quality images, and creating compelling visual content from historical or degraded images.
