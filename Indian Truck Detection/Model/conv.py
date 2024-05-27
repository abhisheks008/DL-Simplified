# A Python script to change the size of images and save them inside a new directory
# The script contains two functions:
# 1. To  change the names of current images to standard number labels.
# 2. To convert the images of random sizes to a fixed size 200X200 resolution.
# This makes the further process of training the model easy as dimensions of each image
# are the same


# Import all the necessary modules
import cv2
import glob
import os


# Source folder location of images
sourceFolder = "D://ML DL AI DSBDA//Indian Trucks Detection//Truck Images"

# Create a separate directory to store processed images
os.mkdir('Processed Images')


def changeNames(path: str) -> None:
    'Change the naming conventions of images:'
    k = 0
    location = os.chdir(path)
    for old_file_name in os.listdir(location):
        new_file_name = '{}.jpg'.format(k)
        os.rename(old_file_name, new_file_name)
        k += 1


def changeDimensions(width: int, height: int) -> None:
    'Change the random dimensions of all images to a fixed resolution and then insert into a new folder'
    i = 0
    for img in glob.glob(sourceFolder + '//*.jpg'):
        image = cv2.imread(img)
        imageResized = cv2.resize(image, (width, height))

        # cv2.imshow('frame', image)
        cv2.imwrite(
            "D://ML DL AI DSBDA//Indian Trucks Detection//Processed Images//000{}.jpg".format(i), imageResized)
        cv2.waitKey(0)
        i += 1

        # if i == 2:
        #     break

    cv2.destroyAllWindows()


def main():
    path = 'D:\\ML DL AI DSBDA\\Indian Trucks Detection\\Truck Images'
    changeNames(path)
    changeDimensions(200, 200)


if __name__ == '__main__':
    main()
