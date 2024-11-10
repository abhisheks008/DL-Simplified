import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys


def plot_images(images, nrows = None, ncols = None, figsize = None, ax = None, 
                axis_style = 'on', bgr2rgb = True):
    '''
    Plots a given list of images and returns axes.Axes object
    
    Parameters
    -----------
    images: list
            A list of images to plot
            
    nrows: int
           Number of rows to arrange images into
    
    ncols: int
           Number of columns to arrange images into
    
    figsize: tuple
             Plot size (width, height) in inches
           
    ax: axes.Axes object
        The axis to plot the images on, new axis will be created if None
        
    axis_style: str
                'off' if axis are not to be displayed
    '''
    N = len(images)
    if not isinstance(images, (list, np.ndarray)):
        raise AttributeError("The images parameter should be a list of images, "
                             "if you want to plot a single image, pass it as a "
                             "list of single image")

    # Setting nrows and ncols as per parameter input
    if nrows is None:
        if ncols is None:
            nrows = N
            ncols = 1
        else:
            nrows = int(np.ceil(N / ncols))
    else:
        if ncols is None:
            ncols = int(np.ceil(N / nrows))
    
    if ax is None:
        _, ax = plt.subplots(nrows, ncols, figsize = figsize)
    
    if len(images) == 1:
        if bgr2rgb == True:
            images[0] = cv2.cvtColor(images[0], cv2.COLOR_BGR2RGB)
    
        ax.imshow(images[0])
        ax.axis(axis_style)
        
        return ax
    
    else:
        for i in range(nrows):
            for j in range(ncols):
                if (i * ncols + j) < N:
                    img = images[i * ncols + j]
                    
                    if bgr2rgb == True:
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    
                    # For this condition, ax is a 2d array else a 1d array
                    if nrows >1 and ncols > 1: 
                        ax[i][j].imshow(img)
                    
                    else:
                        ax[i + j].imshow(img)
                
                if nrows > 1 and ncols > 1:
                    ax[i][j].axis(axis_style)
                else:
                    ax[i + j].axis(axis_style)
        
        return ax


def drawProgressBar(current, total, string = '', barLen = 20):
    '''
    Draws a progress bar, something like [====>    ] 20%
    
    Parameters
    ------------
    current: int/float
             Current progress
    
    total: int/float
           The total from which the current progress is made
             
    string: str
            Additional details to write along with progress
    
    barLen: int
            Length of progress bar
    '''
    percent = current/total
    arrow = ">"
    if percent == 1:
        arrow = ""
    # Carriage return, returns to the begining of line to owerwrite
    sys.stdout.write("\r")
    sys.stdout.write("Progress: [{:<{}}] {}/{}".format("=" * int(barLen * percent) + arrow, 
                                                         barLen, current, total) + string)
    sys.stdout.flush()