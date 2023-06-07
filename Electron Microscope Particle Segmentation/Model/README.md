# Electron Microscopy Particle Segmentation

## PROJECT TITLE

Electron Microscopy Particle Segmentation

## GOAL

The main goal of this project is to develop a segmentation model that can accurately identify and segment particles in electron microscopy images. The purpose of the project is to explore the performance of different deep learning models in this specific segmentation task.

## DATASET

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/datasets/batuhanyil/electron-microscopy-particle-segmentation). The dataset consists of a collection of electron microscopy images along with corresponding ground truth masks for particle segmentation.

## DESCRIPTION

This project aims to build a segmentation model that can accurately detect and segment particles in electron microscopy images. By leveraging deep learning models and image processing techniques, the project seeks to achieve precise and reliable segmentation results.

## WHAT I HAD DONE

1. Data collection: Gathered a diverse dataset of electron microscopy images along with corresponding ground truth masks.
2. Data preprocessing: Performed necessary preprocessing steps such as resizing, normalization, and augmentation.
3. Model selection: Chose popular deep learning models, including U-Net, DeepLabv3+, Mask R-CNN, and FCN, for the segmentation task.
4. Model training: Trained each model using the labeled dataset and appropriate training configurations.
5. Model evaluation: Evaluated the trained models on a separate validation dataset to measure their segmentation performance.
6. Comparative analysis: Compared the IoU (Intersection over Union) and Dice coefficient scores of each model to determine the best-performing model.

## MODELS USED

1. DeepLabv3+
2. UNet

The choice of these model was based on its proven performance in image segmentation tasks and its architectural complexities. This allowed for a comprehensive analysis of different model types.

## LIBRARIES NEEDED

The following libraries are required to run this project:

- PyTorch
- pandas
- numpy
- matplotlib
- scikit-learn

## VISUALIZATION

![Segmentation Comparison](Images/output.png)

## EVALUATION METRICS

The evaluation metrics I used to assess the performance of the segmentation models is:

- Intersection over Union (IoU)

## RESULTS

The segmentation results obtained for selected model on the validation dataset is as follows:

- DeepLabv3+: IoU=0.8972
- UNet: IoU=0.2954

## CONCLUSION

The DeepLabv3+ model achieved a significantly higher IoU score of 0.8972 on the validation dataset, indicating superior performance in accurately segmenting the biomedical images compared to the UNet model, which achieved an IoU score of 0.2954.
