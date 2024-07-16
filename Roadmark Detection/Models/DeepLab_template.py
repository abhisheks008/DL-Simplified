#!pip install tensorflow
#!pip install segmentation-models

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from segmentation_models import DeepLabV3
from segmentation_models.losses import bce_jaccard_loss
from segmentation_models.metrics import iou_score

# Define paths
train_images_path = '/path_to_train_images'
train_labels_path = '/path_to_train_labels'
valid_images_path = '/path_to_valid_images'
valid_labels_path = '/path_to_valid_labels'
test_images_path = '/path_to_test_images'
test_labels_path = '/path_to_test_labels'

# Example function to load images and labels
def load_data(image_path, label_path):
    images = []
    labels = []
    for img_file in sorted(os.listdir(image_path)):
        img = plt.imread(os.path.join(image_path, img_file))
        images.append(img)
    for label_file in sorted(os.listdir(label_path)):
        label = plt.imread(os.path.join(label_path, label_file))
        labels.append(label)
    return np.array(images), np.array(labels)

train_images, train_labels = load_data(train_images_path, train_labels_path)
valid_images, valid_labels = load_data(valid_images_path, valid_labels_path)
test_images, test_labels = load_data(test_images_path, test_labels_path)

# Define the model
model = DeepLabV3(input_shape=(640, 640, 3), classes=1, activation='sigmoid')

# Compile the model
model.compile(optimizer='adam', loss=bce_jaccard_loss, metrics=[iou_score])

# Evaluate on the test set
test_loss, test_iou = model.evaluate(test_images, test_labels)
print(f'Test Loss: {test_loss}')
print(f'Test IoU: {test_iou}')

def visualize_predictions(images, labels, predictions, num_samples=5):
    for i in range(num_samples):
        plt.figure(figsize=(15, 5))
        plt.subplot(1, 3, 1)
        plt.imshow(images[i])
        plt.title('Image')
        plt.subplot(1, 3, 2)
        plt.imshow(labels[i].squeeze(), cmap='gray')
        plt.title('Ground Truth')
        plt.subplot(1, 3, 3)
        plt.imshow(predictions[i].squeeze(), cmap='gray')
        plt.title('Prediction')
        plt.show()

predictions = model.predict(test_images)
visualize_predictions(test_images, test_labels, predictions)
