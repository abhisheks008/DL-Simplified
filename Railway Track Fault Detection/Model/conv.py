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
defective = "D://ML DL AI DSBDA//Railway Track Fault Detection//archive//images//Defective"
nonDefective = "D://ML DL AI DSBDA//Railway Track Fault Detection//archive//images//Non Defective"
# Create a separate directory to store processed images



def changeNames(path: str) -> None:
    'Change the naming conventions of images:'
    k = 0
    location = os.chdir(path)
    for old_file_name in os.listdir(location):
        new_file_name = '{}.jpg'.format(k)
        os.rename(old_file_name, new_file_name)
        k += 1


def changeDimensionsForDefectiveImages(width: int, height: int) -> None:
    'Change the random dimensions of all images to a fixed resolution and then insert into a new folder'
    i = 0
    for img in glob.glob(defective + '//*.jpg'):
        image = cv2.imread(img)
        imageResized = cv2.resize(image, (width, height))

        # cv2.imshow('frame', image)
        
        cv2.imwrite(
            "D://ML DL AI DSBDA//Railway Track Fault Detection//Processed Images//Defective//000{}.jpg".format(i), imageResized)
        cv2.waitKey(0)
        i += 1

        # if i == 2:
        #     break

    cv2.destroyAllWindows()

def changeDimensionsForNonDefectiveImages(width: int, height: int) -> None:
    'Change the random dimensions of all images to a fixed resolution and then insert into a new folder'
    i = 0
    for img in glob.glob(nonDefective + '//*.jpg'):
        image = cv2.imread(img)
        imageResized = cv2.resize(image, (width, height))

        # cv2.imshow('frame', image)
        cv2.imwrite(
            "D://ML DL AI DSBDA//Railway Track Fault Detection//Processed Images//Non Defective//000{}.jpg".format(i), imageResized)
        cv2.waitKey(0)
        i += 1

        # if i == 2:
        #     break

    cv2.destroyAllWindows()


def main():
    defectiveImagePath = 'D://ML DL AI DSBDA//Railway Track Fault Detection//archive//Images//Defective'
    nonDefectivePath = 'D://ML DL AI DSBDA//Railway Track Fault Detection//archive//Images//Non Defective'
    changeNames(defectiveImagePath)
    changeNames(nonDefectivePath)
    changeDimensionsForDefectiveImages(256, 256)
    changeDimensionsForNonDefectiveImages(256, 256)


if __name__ == '__main__':
    main()
