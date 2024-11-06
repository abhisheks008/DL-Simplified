## 📊 Synthetic Dataset Used

In this model, a synthetic dataset consisting of 1,000 images was generated, each with a resolution of 28x28 pixels and three color channels (RGB). The images were created using random noise, simulating artistic patterns. This dataset serves as a foundation for training the GAN, allowing for the evaluation of its ability to produce diverse and visually appealing art-like images. 

### Visualization of the Synthetic Dataset

Below is a sample of the generated synthetic images:

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic dataset
def generate_synthetic_data(num_samples, img_shape):
    return np.random.rand(num_samples, *img_shape)

# Generate and display sample images
synthetic_data = generate_synthetic_data(1000, (28, 28, 3))

# Plotting the synthetic images
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(synthetic_data[i])
    plt.axis('off')
plt.show()
```
## 📊 Dataset Characteristics

The synthetic dataset consists of 1,000 RGB images, each measuring 28x28 pixels. The images are generated using random noise, resulting in diverse and unique artistic patterns. This randomness contributes to the dataset's variability, making it suitable for training Generative Adversarial Networks (GANs) to create visually appealing outputs.

### Data Preprocessing

Before feeding the data into the GAN, several preprocessing steps were performed:

1. **Normalization**: The pixel values were scaled to a range between 0 and 1 to facilitate better training convergence.
2. **Reshaping**: Images were reshaped to ensure they meet the input requirements of the GAN model.
3. **Data Augmentation**: While not applied here, techniques such as rotation, flipping, and scaling could be incorporated to enhance the dataset's diversity.

These preprocessing steps help improve the GAN's performance and stability during training.
