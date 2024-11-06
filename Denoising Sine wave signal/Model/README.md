# Sine Wave Signal Denoising

## Project Overview

This project demonstrates how to denoise a noisy signal using deep learning models, primarily through a Convolutional Autoencoder, LSTM Autoencoder, and an enhanced Conv1D Autoencoder. Each model is designed to take a noisy signal as input and reconstruct the original (denoised) signal. After denoising, the Savitzky-Golay filter is applied to further smooth the output.

### Methodology

1. **Preprocessing**: 
   - The signal is normalized using `MinMaxScaler`.
   - Both noisy and original signals are reshaped into sliding windows for training.
   
2. **Model Architectures**:
   - **Conv1D Autoencoder**: A Convolutional Autoencoder built to map noisy signals to clean ones, using convolutional and pooling layers for feature extraction and dimensionality reduction.
   - **LSTM Autoencoder**: A recurrent model utilizing LSTM layers to capture temporal dependencies, effective for time-series data.
   - **Enhanced Conv1D Autoencoder**: An improved version of the Conv1D Autoencoder with deeper layers for better feature extraction and reconstruction capabilities.

3. **Postprocessing**:
   - The Savitzky-Golay filter is applied to the output to further reduce residual noise.

4. **Visualization**:
   - The original, noisy, and denoised signals are plotted for a comprehensive visual comparison.

### Dependencies

- Python 3.x
- `pandas`
- `numpy`
- `scikit-learn`
- `tensorflow`
- `scipy`
- `matplotlib`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/signal denoising autoencoder.git
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Prepare your dataset in an Excel file (`ex1.xlsx`) with two columns: `Amplitude` and `Amplitude_noise`.
   
2. Run the denoising script:
   ```bash
   python denoise_signal.py
   ```

3. The script will train the autoencoders on the noisy signal, output the denoised signals, and plot them alongside the original and noisy signals.

### Model Details

#### Conv1D Autoencoder

The model architecture:
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

#### LSTM Autoencoder

The LSTM Autoencoder captures sequential dependencies, which is particularly effective for time-series data. This model consists of:
- A stack of LSTM layers for encoding the sequence.
- An intermediate dense layer for feature extraction.
- LSTM layers for decoding the signal back to its denoised form.

The model is effective for denoising tasks with complex temporal dependencies and uses `Mean Squared Error (MSE)` as the loss function.

#### Enhanced Conv1D Autoencoder

An advanced convolutional model that expands upon the basic Conv1D Autoencoder:
- Deeper architecture with additional convolutional layers for enhanced feature extraction.
- Additional UpSampling and convolutional layers for improved reconstruction capabilities.
- MaxPooling and UpSampling for dimensionality adjustments and noise removal, offering better denoising for high-frequency noise.

### Results

After training each model, the denoised signals are plotted and visually compared with the original and noisy signals. Each model significantly reduces noise, preserving the main structure of the original signal.

### Comparison of Model Performance

- **Conv1D Autoencoder**: Ideal for signals with moderate noise levels; balances simplicity and accuracy.
- **LSTM Autoencoder**: Better suited for sequential data, capturing dependencies over longer periods.
- **Enhanced Conv1D Autoencoder**: Offers the best denoising performance among the models due to its deeper architecture and robust feature extraction capabilities.

### Conclusion

This project demonstrates how deep learning models, particularly convolutional and recurrent autoencoders, can be used for signal denoising. Further improvements can be made by experimenting with model architectures, window sizes, and smoothing techniques to enhance the denoising process.

