<h1>James Webb Space Telescope Image Analysis</h1>

<h2>Goal</h2>

The Goal of this project is to apply various modules for image analysis. The data extracted from this image analysis can then be used for various regression and classification techniques.

<h2>Dataset</h2>
The dataset is obtained from the link, https://www.kaggle.com/datasets/goelyash/james-webb-telescope-images-original-size
<h2>What have I done</h2>
Method 1:

Coverted color images to greyscale images and then to binary images. Used methods like regionprops to extract data from given images and stored into a csv file for image processing.

Method 2:

Used opencv module and its properties to perform edge detection and to apply laplacian methods.

<h2>Libraries Used</h2>

imageio

matplotlib

numpy

opencv-python

pandas

Pillow

scikit-image

scipy

<h2>Data Visualization</h2> 

Binarized images:

![alt text](https://github.com/Rohith2202/DL-Simplified/blob/main/James%20Webb%20Space%20Telescope%20Image%20Analysis/Images/Binary_Image.jpg)

Image for data extraction:

![alt text](https://github.com/Rohith2202/DL-Simplified/blob/main/James%20Webb%20Space%20Telescope%20Image%20Analysis/Images/RegionProps.jpg)

Plotting the pixel values in histogram:

![alt text](https://github.com/Rohith2202/DL-Simplified/blob/main/James%20Webb%20Space%20Telescope%20Image%20Analysis/Images/Pixel_plot.jpg)

Vertical Edge detection:

![alt text](https://github.com/Rohith2202/DL-Simplified/blob/main/James%20Webb%20Space%20Telescope%20Image%20Analysis/Images/Vertical_Edge_Detection.jpg)

Laplacian Method:

![alt text](https://github.com/Rohith2202/DL-Simplified/blob/main/James%20Webb%20Space%20Telescope%20Image%20Analysis/Images/Laplacian%20Method.jpg)

Edge Detection (canny method):

![alt text](https://github.com/Rohith2202/DL-Simplified/blob/main/James%20Webb%20Space%20Telescope%20Image%20Analysis/Images/Edge%20Detection.jpg)

<h4>Steps to run the code:</h4>

Click on "Run" button to execute the code

Download data using the opendatasets module or download it directly from kaggle into the folder containing .ipynb file

Download the required modules and if there is an error while downloading opencv try:- pip install opencv-python

Install all the requirements from requirements.txt file

Change path ff the images are in a different folder

Can also provide "path" by using glob module and a for loop

Dataset for image classification and regression has already been found and uploaded into the data.csv file in dataset folder

<h2>Analysis and Conclusion</h2>

The dataset's photos are all first transformed to greyscale versions. This approach makes it simpler and requires less computing with the use of greyscale images. When colour photos are used for image analysis, extraneous information will be included therefore increasing the amount of training data necessary to attain acceptable accuracy and performance. So they are transformed into greyscale images.

Then, greyscale images are transformed into binary images using thresholding. We employ thresholding in the James Webb space telescope image analysis to separate items from a backdrop. Because we can distinguish between the many light sources, such as galaxies, stars, etc., and the dark background of space, this method in particular is highly helpful. Once we have the binary image, we can visually identify the different light sources in the dataset. Astronomers can use this as a preliminary observation technique. Combining area opening and area closing allows components with an area less than lambda to be eliminated, advancing image analysis.

The label method is then used to act as a container for the images and regionprops method is used to extract the properties of the image. With this method we can get data ['area','convex_area','bbox_area','major_axis_length','minor_axis_length','perimeter','equivalent_diameter','mean_intensity,'solidity','eccentricity'] for all the images.This is the data that can be used for image classification and regression techniques. All the data obtained from MIRI images, NIRCam images and Composite(both NIRCam and MIRI) is then stored into a single dataframe. The data from this dataframe can then be used for image classification for the new images obtained or we can use some AI and deep learning models to predict the images of nearby stars,galaxies.. etc. All the data is stored in the data.csv file of the dataset folder.

Laplacian provides an image's second derivative, which quantifies how quickly the first derivative is changing. This establishes whether a change in the values of adjacent pixels results from a continuous progression or an edge. In relation to the pixel grid, X sobel and Y sobel react most strongly to edges that run vertically and horizontally , Ksize is limited to 1, 3, 5, or 7. Greater k will result in fewer fake corners but more real ones will be missed. Conversely, smaller k will result in many more corners, many more of which will be false.

With visual analysis we can see the edges of the James Webb Space telescope images. We can use the data obtained to perform and implement various ML models.

Edges are detected near sources of light i.e. stars and other planetary objects so we can use the edge data to find out the relative positions of sources of light.

Laplacian derivative tells us about the intensity change. This is very helpful for image analysis and processing.



My linkedin: https://www.linkedin.com/in/m-rohith-3a4b8b237/ 

My github: https://github.com/Rohith2202
