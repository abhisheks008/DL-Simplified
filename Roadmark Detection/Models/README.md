# Road Mark Detection using UNet, Mask R-CNN, and DeepLab

This repository contains the implementation of various models for road mark detection, including UNet, Mask R-CNN, and DeepLab. The models are trained and evaluated on a Kaggle dataset containing images and labels for road marks.

## Baseline CNN Model

Initially, a baseline CNN model was built for the dataset. However, due to its limited performance and lack of potential for improvement, the use of this model is deemed invalid. Therefore, the focus has shifted to more advanced architectures such as UNet, Mask R-CNN, and DeepLab.

## UNet Model

### Dataset

The dataset consists of:
- 2167 images in the training set
- 417 images in the validation set
- 192 images in the test set

All images are resized to 640x640 pixels.

### Data Loading and Preprocessing

The images and their corresponding labels are loaded and preprocessed as follows:
- Images are read using OpenCV and normalized.
- Labels are parsed to extract coordinates and create binary masks for segmentation.

### Model Architecture

We used the UNet architecture, which is well-suited for image segmentation tasks. The model was implemented using the `segmentation-models` library.

### Training

Due to resource limitations, the model was trained for only 1 epoch with a batch size of 64 on Google Colab using TPUv2.

Here is the training code snippet:

      # Define the UNet model
      model = Unet(input_shape=(640, 640, 3), classes=1, activation='sigmoid')
      
      # Compile the model
      model.compile(optimizer='adam', loss=bce_jaccard_loss, metrics=[iou_score])
      
      # Train the model
      history = model.fit(
          train_images, train_labels,
          epochs=1,
          batch_size=64,
          validation_data=(valid_images, valid_labels)
      )


### Results

After training for 1 epoch, the model achieved the following results on the test set:
- **Test Loss:** 1.1267637014389038
- **Test IoU:** 0.029536180198192596

### Limitations

The current training was performed for only 1 epoch due to resource constraints. As a result, the model has not had sufficient time to learn effectively from the data, leading to high loss and low IoU.

### Future Work

Given more resources, the following improvements can be made:
- Increase Number of Epochs
- Adjust Batch Size
- Implement Data Augmentation
- Hyperparameter Tuning

Here is an example of how you might continue training the model with more epochs and additional callbacks for better training management:

      from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
      
      # Callbacks for better training management
      callbacks = [
          EarlyStopping(monitor='val_loss', patience=5, verbose=1, restore_best_weights=True),
          ModelCheckpoint('unet_model.h5', monitor='val_loss', save_best_only=True, verbose=1),
          ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
      ]
      
      # Continue training the model
      history = model.fit(
          train_images, train_labels,
          epochs=50,  # Increase number of epochs
          batch_size=64,  # You can experiment with larger batch sizes if using TPU
          validation_data=(valid_images, valid_labels),
          callbacks=callbacks
      )
      
      # Evaluate the model on the test set
      test_loss, test_iou = model.evaluate(test_images, test_labels)
      print(f'Test Loss: {test_loss}')
      print(f'Test IoU: {test_iou}')


## Mask R-CNN and DeepLab

Templates for the Mask R-CNN and DeepLab models have been added to this repository. Due to version conflicts and importing errors, developing these models was not possible at this time. However, if these errors are resolved in the future, feel free to use the templates included in the repository and modify them accordingly.

## Conclusion

The UNet model shows promising potential for road mark detection. With adequate training resources and further optimization, the model can achieve significantly better performance. Contributions and suggestions for improvements are welcome!

For future development, feel free to utilize and modify the Mask R-CNN and DeepLab templates provided in this repository.
