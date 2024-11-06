# Dataset for Signal Denoising Autoencoder

This dataset contains synthetic or real-world signals with added noise, used for training and testing a denoising autoencoder. It includes columns representing the original amplitude of the signal and the noisy version of the signal.

## Dataset Structure

The dataset file (`ex1.xlsx`) includes the following columns:
- **Amplitude**: The original, clean signal amplitude.
- **Amplitude_noise**: The amplitude of the signal after noise has been added.

The data is sequential and each entry represents one time step.

### Loading the Dataset
To load the dataset in Python, use the following code:

```bash
import pandas as pd

data = pd.read_excel('ex1.xlsx')
original_amplitude = data['Amplitude'].values
noised_amplitude = data['Amplitude_noise'].values
```

### Usage
This dataset is used to train and evaluate denoising models, which will learn to filter noise from signals, providing a cleaned signal that approximates the original.