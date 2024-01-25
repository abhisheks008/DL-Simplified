I have fetched the Human Detection Dataset from, https://www.kaggle.com/datasets/vinayakshanawad/weedcrop-image-dataset/data, for building and developing this Project. You guys can check out the dataset from the given link.

### Data Description

It includes 2822 images.
Weed are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:

Auto-orientation of pixel data (with EXIF-orientation stripping)
The following augmentation was applied to create 3 versions of each source image:

Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise
Random shear of between -15° to +15° horizontally and -15° to +15° vertically
Random brigthness adjustment of between -25 and +25 percent
Classes
Crop, Weed
