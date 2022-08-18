James Webb Space Telescope Image analysis

Click on "Run" button to execute the code

Download data using the opendatasets module or download it directly from kaggle into the folder containing .ipynb file

Download the required modules and if there is an error while downloading opencv try:- pip install opencv-python

Change path if the images are in a different folder

Currently images are in the image folder which hasn't been uploaded so path has to be changed

Can also provide "path" by using glob module and a for loop

Analysis

The dataset's photos are all first transformed to greyscale versions. This approach makes it simpler and requires less computing with the use of greyscale images. When colour photos are used for image analysis, extraneous information will be included therefore increasing the amount of training data necessary to attain acceptable accuracy and performance. So they are transformed into greyscale images.

Then, greyscale images are transformed into binary images using thresholding. We employ thresholding in the James Webb space telescope image analysis to separate items from a backdrop. Because we can distinguish between the many light sources, such as galaxies, stars, etc., and the dark background of space, this method in particular is highly helpful. Once we have the binary image, we can visually identify the different light sources in the dataset. Astronomers can use this as a preliminary observation technique. Combining area opening and area closing allows components with an area less than lambda to be eliminated, advancing image analysis.

The label method is then used to act as a container for the images and regionprops method is used to extract the properties of the image. With this method we can get data ['area','convex_area','bbox_area','major_axis_length','minor_axis_length','perimeter','equivalent_diameter','mean_intensity,'solidity','eccentricity'] for all the images.This is the data that can be used for image classification and regression techniques. All the data obtained from MIRI images, NIRCam images and Composite(both NIRCam and MIRI) is then stored into a single dataframe. The data from this dataframe can then be used for image classification for the new images obtained or we can use some AI and deep learning models to predict the images of nearby stars,galaxies.. etc. All the data is stored in the data.csv file of the dataset folder.

Laplacian provides an image's second derivative, which quantifies how quickly the first derivative is changing. This establishes whether a change in the values of adjacent pixels results from a continuous progression or an edge. In relation to the pixel grid, X sobel and Y sobel react most strongly to edges that run vertically and horizontally , Ksize is limited to 1, 3, 5, or 7. Greater k will result in fewer fake corners but more real ones will be missed. Conversely, smaller k will result in many more corners, many more of which will be false.

With visual analysis we can see the edges of the James Webb Space telescope images. We can use the data obtained to perform and implement various ML models.

Dataset can be used for multiple ML models like regression,classification or reinforcement learning.

Analysis:

Edges are mainly present near the source of light i.e. near stars or all light emitting objects

The laplacian derivative showing the 2nd derivative describes the stress of the space field.

Copyright 2022 Rohith

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

My linkedin profile: https://www.linkedin.com/in/m-rohith-3a4b8b237/

My github profile: https://github.com/Rohith2202

