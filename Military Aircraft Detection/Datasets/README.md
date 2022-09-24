# Military Aircraft Detection Dataset
The dataset used here is provided at https://www.kaggle.com/datasets/a2015003713/militaryaircraftdetectiondataset.

## About Dataset

The dataset consists of 12337 images that are divided into 40 categories of Aircrafts that 
are collected from Google Images. Since the author is not sure about the copyright of the images, there is no license to the images. So I would like to declare that the data I have used here is only used for purely research and academic(non-commercial) purpose. 
40 aircraft types 
(A10, A400M, AG600, AV8B, B1, B2, B52 Be200, C130, C17, C5, E2, EF2000, F117, F14, F15, F16, F18, F22, F35, F4, J20, JAS39, MQ9, Mig31, Mirage2000, RQ4, Rafale, SR71(may contain A12), Su34, Su57, Tornado, Tu160, Tu95(may contain Tu142), U2, US2, V22, Vulcan, XB70, YF23)

## Augumentations Used on the Dataset
The dataset consists of 12337 images that are divided into 40 categories of Aircrafts that 
variable sized so to pass through them into the model we need to do some special augumentations. So I took the following optimizations in order to decrease the computation time and increase the accuracy of the output.
- Converting the variable sized images into standard sizes of 224 X 224 so that they can be supplied to each next layer(ReSize)
- For images smaller than 224X224, I want randomcrop and padding(reflecting) enacbled as it can help increase the amount of data provided by low resolution images
- Then the images are converted into pytorch tensors
- Then the images are normalized using empirical values of mean and standard deviation.