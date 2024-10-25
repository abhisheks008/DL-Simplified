# Sine Wave Signal Denoising using Convolutional Autoencoder

## Project Overview

This project demonstrates how to denoise a signal using a Convolutional Autoencoder. We take a noisy signal as input and use a deep learning model to reconstruct the original (denoised) signal. The denoised signal is further smoothed using the Savitzky-Golay filter to improve its quality.

### Dataset

The dataset used consists of two columns:
- `Amplitude`: Original signal amplitude (ground truth)
- `Amplitude_noise`: Noisy version of the original amplitude
