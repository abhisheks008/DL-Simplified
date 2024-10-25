# Sine Wave Signal Denoising using Convolutional Autoencoder

## Project Overview

This project demonstrates how to denoise a signal using a Convolutional Autoencoder. We take a noisy signal as input and use a deep learning model to reconstruct the original (denoised) signal. The denoised signal is further smoothed using the Savitzky-Golay filter to improve its quality.

### Methodology

1. **Preprocessing**: 
   - The signal is normalized using MinMaxScaler.
   - The noisy and original signals are reshaped into sliding windows for training the autoencoder.
   
2. **Model Architecture**:
   - A 1D Convolutional Autoencoder is built to learn the mapping between noisy and original signals.
   - The model consists of convolutional layers for feature extraction and max pooling for dimensionality reduction. It uses UpSampling to reconstruct the denoised signal.
   
3. **Postprocessing**:
   - After obtaining the denoised signal from the autoencoder, the Savitzky-Golay filter is applied to further smooth the output.

4. **Visualization**:
   - The original, noisy, and denoised signals are plotted for visual comparison.

### Dependencies

- Python 3.x
- pandas
- numpy
- scikit-learn
- tensorflow
- scipy
- matplotlib

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/signal-denoising-autoencoder.git
   ```
   
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Prepare your dataset in an Excel file (`ex1.xlsx`) with two columns: `Amplitude` and `Amplitude_noise`.

2. Run the denoising script:
   ```
   python denoise_signal.py
   ```

3. The script will train the autoencoder on the noisy signal and output the denoised signal, which will be plotted alongside the original and noisy signals.

### Model Summary

The model architecture of the Convolutional Autoencoder:
```
Layer (type)                    Output Shape         Param #
=================================================================
input_signal (InputLayer)        [(None, 4500, 1)]    0
_________________________________________________________________
conv1d (Conv1D)                  (None, 4500, 16)     64
_________________________________________________________________
max_pooling1d (MaxPooling1D)     (None, 2250, 16)     0
_________________________________________________________________
conv1d_1 (Conv1D)                (None, 2250, 8)      392
_________________________________________________________________
max_pooling1d_1 (MaxPooling1D)   (None, 1125, 8)      0
_________________________________________________________________
conv1d_2 (Conv1D)                (None, 1125, 8)      200
_________________________________________________________________
up_sampling1d (UpSampling1D)     (None, 2250, 8)      0
_________________________________________________________________
conv1d_3 (Conv1D)                (None, 2250, 16)     400
_________________________________________________________________
up_sampling1d_1 (UpSampling1D)   (None, 4500, 16)     0
_________________________________________________________________
conv1d_4 (Conv1D)                (None, 4500, 1)      49
=================================================================
Total params: 1,105
Trainable params: 1,105
Non-trainable params: 0
```

### Results

After training the autoencoder, the denoised signal is plotted and visually compared with the original signal and the noisy input. The model significantly reduces noise while preserving the main structure of the original signal.

### Conclusion

This project shows how a deep learning model (Convolutional Autoencoder) can be used for signal denoising. Further improvements can be made by experimenting with different window sizes, model architectures, and postprocessing techniques.
