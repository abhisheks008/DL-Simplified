#!/usr/bin/env python
# coding: utf-8

# # Note: This notebook is prepared in Google collab

# # Loading Basic Libraries

# In[1]:


import os
import cv2
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt


# In[2]:


# Creaking dataset folder  to download the dataset
mkdir dataset


# In[3]:


# changing current directory path
cd dataset


# In[5]:


# Downloading the dataset
get_ipython().system('kaggle datasets download -d nirmalsankalana/crop-pest-and-disease-detection')


# In[6]:


# Unzipping the dataset
get_ipython().system('unzip \\*.zip')


# In[ ]:


# Navigating back to content directory
cd '../'


# # Some predifined functions

# In[7]:


import matplotlib.pyplot as plt

def plot_graph(history):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))  # Create a figure with 1 row and 2 columns

    # Plot training & validation accuracy values
    ax[0].plot(history.history['accuracy'])
    ax[0].plot(history.history['val_accuracy'])
    ax[0].set_title('Model accuracy')
    ax[0].set_ylabel('Accuracy')
    ax[0].set_xlabel('Epoch')
    ax[0].legend(['Train', 'Validation'], loc='upper left')

    # Plot training & validation loss values
    ax[1].plot(history.history['loss'])
    ax[1].plot(history.history['val_loss'])
    ax[1].set_title('Model loss')
    ax[1].set_ylabel('Loss')
    ax[1].set_xlabel('Epoch')
    ax[1].legend(['Train', 'Validation'], loc='upper left')

    plt.tight_layout()
    plt.show()


# # Data Cleaning and filter valid image data

# The given dataset contains some invalid images. The below code filters the dataset.

# In[54]:


import os
import random
import shutil

# Set the source directory
src_dir = 'dataset'

# Set the destination directories
train_dir = 'train'
test_dir = 'test'
val_dir = 'val'

# Set the split ratios
train_ratio = 0.7
test_ratio = 0.2
val_ratio = 0.1

# Create the destination directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Get a list of all subdirectories in the source directory
subdirs = [d for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

for subdir in subdirs:
    subdir_path = os.path.join(src_dir, subdir)
    image_files = [f for f in os.listdir(subdir_path) if f.endswith('.jpg') or f.endswith('.png')]

    print(f"Found {len(image_files)} image files in {subdir_path}")

    # If no image files found in the subdirectory, skip it
    if not image_files:
        print(f"No image files found in {subdir_path}. Skipping...")
        continue

    # Shuffle the list of image files
    random.shuffle(image_files)

    # Calculate the number of images for each set
    num_images = len(image_files)
    num_train = int(num_images * train_ratio)
    num_test = int(num_images * test_ratio)
    num_val = num_images - num_train - num_test

    # Create subdirectories for train, test, and val sets
    train_subdir = os.path.join(train_dir, subdir)
    test_subdir = os.path.join(test_dir, subdir)
    val_subdir = os.path.join(val_dir, subdir)

    os.makedirs(train_subdir, exist_ok=True)
    os.makedirs(test_subdir, exist_ok=True)
    os.makedirs(val_subdir, exist_ok=True)

    # Copy the images to their respective sets
    train_files = image_files[:num_train]
    test_files = image_files[num_train:num_train+num_test]
    val_files = image_files[num_train+num_test:]

    for file in train_files:
        src_path = os.path.join(subdir_path, file)
        dst_path = os.path.join(train_subdir, file)
        shutil.copy(src_path, dst_path)

    for file in test_files:
        src_path = os.path.join(subdir_path, file)
        dst_path = os.path.join(test_subdir, file)
        shutil.copy(src_path, dst_path)

    for file in val_files:
        src_path = os.path.join(subdir_path, file)
        dst_path = os.path.join(val_subdir, file)
        shutil.copy(src_path, dst_path)

    print(f"Copied {num_train} images to {train_subdir}")
    print(f"Copied {num_test} images to {test_subdir}")
    print(f"Copied {num_val} images to {val_subdir}")


# In[10]:


# Function to check if an image is valid using OpenCV
def is_image_valid(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return False
        return True
    except:
        return False

# Function to filter out corrupted images
def filter_and_save_valid_images(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if is_image_valid(file_path):
                relative_path = os.path.relpath(file_path, source_dir)
                target_path = os.path.join(target_dir, relative_path)
                target_subdir = os.path.dirname(target_path)
                if not os.path.exists(target_subdir):
                    os.makedirs(target_subdir)
                cv2.imwrite(target_path, cv2.imread(file_path))

# Specify the source and target directories
train_source_dir = 'train'
train_target_dir = 'filtered_train'
val_source_dir = 'val'
val_target_dir = 'filtered_val'
test_source_dir = 'test'
test_target_dir = 'filtered_test'

# Filter and save valid images
filter_and_save_valid_images(train_source_dir, train_target_dir)
filter_and_save_valid_images(val_source_dir, val_target_dir)
filter_and_save_valid_images(test_source_dir, test_target_dir)


# # Loading the dataset

# In[11]:


# Function to load and preprocess the dataset
def load_and_preprocess_dataset(directory, image_size=(150, 150), batch_size=32):
    dataset = tf.keras.utils.image_dataset_from_directory(
        directory=directory,
        labels='inferred',
        label_mode='categorical',
        batch_size=batch_size,
        image_size=image_size)

    class_names = dataset.class_names

    # Define a preprocessing function to scale the images
    def preprocess(image, label):
        # Rescale the image pixel values from [0, 255] to [0, 1]
        image = tf.cast(image, tf.float32) / 255.0
        return image, label

    # Apply the preprocessing function to the dataset
    dataset = dataset.map(preprocess, num_parallel_calls=tf.data.AUTOTUNE)
    return dataset, class_names

# Load the datasets
train_ds, train_class_names = load_and_preprocess_dataset(train_target_dir)
val_ds, val_class_names = load_and_preprocess_dataset(val_target_dir)

# Ensure the class names are consistent
assert train_class_names == val_class_names, "Class names in training and validation datasets do not match."

# Prefetching to improve performance
train_ds = train_ds.prefetch(buffer_size=tf.data.AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=tf.data.AUTOTUNE)


# In[12]:


test_ds, test_class_names = load_and_preprocess_dataset(test_target_dir)
test_ds = test_ds.prefetch(buffer_size=tf.data.AUTOTUNE)


# # ANN model

# In[ ]:


import tensorflow as tf
from tensorflow.keras import layers, models
ann_model = models.Sequential([
    layers.Flatten(input_shape=(150,150,3)),         # Input layer flattens the image
    layers.Dense(512, activation='relu'),            # Hidden layer with 512 units and ReLU activation
    layers.Dense(256, activation='relu'),            # Hidden layer with 256 units and ReLU activation
    layers.Dense(22, activation='softmax')  # Output layer with softmax activation for classification
])

# Compile the model
ann_model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

ann_model.summary()


# In[ ]:


ann_history= ann_model.fit(train_ds,validation_data=val_ds,epochs=10)


# In[ ]:


plot_graph(ann_history)


# # Basic CNN model

# In[ ]:


from keras.optimizers import Adam


# In[ ]:


import tensorflow as tf
from tensorflow.keras import layers, models

# Define the CNN model with batch normalization
cnn_model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(1024, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.75),
    layers.Dense(22, activation='softmax')
])


# Compile the model
cnn_model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

# Display the model summary
cnn_model.summary()


# In[ ]:


cnn_history = cnn_model.fit(
    train_ds,
    validation_data=val_ds,

    epochs=10  # Adjust the number of epochs based on your requirements
)



# In[ ]:


plot_graph(cnn_history)


# # Resnet(Basic)
# 

# In[13]:


import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D , Dropout
from tensorflow.keras.optimizers import Adam


# In[14]:


base_model = ResNet50(weights='imagenet', include_top=False)

for layer in base_model.layers[-10:]:
    layer.trainable = True

# Add new top layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(22, activation='softmax')(x)

res_model = Model(inputs=base_model.input, outputs=predictions)


# Re-compile the model
res_model.compile(optimizer=Adam(learning_rate=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# In[15]:


resnet_history= res_model.fit(train_ds,validation_data=val_ds,epochs=10)


# In[41]:


plot_graph(resnet_history)


# # ResNet(Perfect) with Data Augumentaion and Regularizations

# In[25]:


# Data augmentaion
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

train_generator = datagen.flow_from_directory(
    'filtered_train',
    target_size=(150,150),
    batch_size=32,
    class_mode='categorical'
)

val_generator = datagen.flow_from_directory(
    'filtered_val',
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)


# In[27]:


from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping


# In[31]:


# Load the base model
base_model = ResNet50(weights='imagenet', include_top=False)

# Make the last 10 layers trainable
for layer in base_model.layers[-10:]:
    layer.trainable = True

# Add new top layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.5)(x)  # Adding dropout for regularization
x = Dense(1024, activation='relu', kernel_regularizer=l2(0.01))(x)
x = Dropout(0.5)(x)  # Adding another dropout layer for regularization
predictions = Dense(22, activation='softmax', kernel_regularizer=l2(0.01))(x)

res_model_perfect = Model(inputs=base_model.input, outputs=predictions)

# Re-compile the model
res_model_perfect.compile(optimizer=Adam(learning_rate=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model
res_model_perfect_history = res_model_perfect.fit(train_generator, epochs=5, validation_data=val_generator, callbacks=[early_stopping])


# In[33]:


res_model_perfect_history1 = res_model_perfect.fit(train_generator, initial_epoch=5,epochs=10, validation_data=val_generator, callbacks=[early_stopping])


# # VGG16 Model

# In[19]:


from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# In[20]:


# Load the base model
base_model = VGG16(weights='imagenet', include_top=False)

# Make more layers trainable
for layer in base_model.layers[-10:]:
    layer.trainable = True

# Add new top layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(22, activation='softmax')(x)

# Create the final model
vgg_model = Model(inputs=base_model.input, outputs=predictions)

vgg_model.compile(optimizer=Adam(learning_rate=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

vgg_model.summary()



# In[21]:


vgg_history= vgg_model.fit(train_ds,epochs=10,validation_data=val_ds)


# In[24]:


plot_graph(vgg_history)


# # Model Evaluation and Best model Testing

# In[ ]:


loss_ann, accuracy_ann = ann_model.evaluate(test_ds)
print(f"ANN Test accuracy: {accuracy_ann * 100:.2f}%")


# In[ ]:


loss_cnn, accuracy_cnn = cnn_model.evaluate(test_ds)
print(f"CNN Test accuracy: {accuracy_cnn * 100:.2f}%")


# In[17]:


loss_res, accuracy_res = res_model.evaluate(test_ds)
print(f"ResNet Test accuracy: {accuracy_res * 100:.2f}%")



# In[37]:


loss_vgg16, accuracy_vgg16 = vgg_model.evaluate(test_ds)
print(f"VGG16 Test accuracy: {accuracy_vgg16 * 100:.2f}%")


# In[56]:


# Preparing test data for Renset Perfect model
test_generator = datagen.flow_from_directory(
    'filtered_test',
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical'
)


# In[55]:


loss_res_model_perfect, accuracy_res_model_perfect = res_model_perfect.evaluate(test_generator)
print(f"ResNet(Perfect) Test accuracy: {accuracy_res_model_perfect * 100:.2f}%")


# # Tabulating the Model and it's Accuracy

#                             |   Model Name    | Accuracy (%) |
#                             |-----------------|--------------|
#                             | ANN             | 38.98        |
#                             | CNN             | 69.92        |
#                             | VGG16           | 83.03        |
#                             | ResNet          | 85.62        |
#                             | ResNet(Perfect) | 84.58        |

# - The ResNet(Perfect) model is chosen as the optimal model due to its balance of high accuracy and reduced overfitting, making it the best candidate for deployment. While the standard ResNet model achieved the highest accuracy, its overfitting issues could compromise its performance on new, unseen data. Therefore, for practical applications where generalization is crucial, the ResNet(Perfect) model is the preferred choice
# 

# In[ ]:




