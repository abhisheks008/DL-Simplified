# Glass-Bangle-Defect-Dectection-Dataset

The dataset used here is provided at https://www.kaggle.com/datasets/almique/glass-bangle-defect-detection-classification.

## About Dataset

Since one of the most crucial aspects of bangle manufacturing process is to make sure bangles come out round and without defects. We have compiled a dataset which consists of human-labeled images collected from one of the bangle factories. The dataset consist total of 1080 images consisting broken, defected and good bangle images.

## Augumentations Used on the Dataset

The data images(about 1080 in number) were especially large (3000X3000 pixels). So I took the following optimizations in order to decrease the computation time and increase the accuracy of the output.
- Random Horizontal flip
- Resizing the images to (224 X 224) using Resize function in Pytorch Data Trasforms
- Normalized the data images using empirical values of mean and standard deviation.
- Finally all images were converted into batches and loaded into the pytorch model

For more imformation, visit https://pytorch.org/tutorials/beginner/basics/data_tutorial.html