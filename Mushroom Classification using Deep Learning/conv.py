import os
import cv2

def changeDimensions(dirPath : str, width : int, height : int) -> None:
    # Iterate through each folder
    for folder_name in os.listdir(dirPath):
        folder_path = os.path.join(dirPath, folder_name)
        
        if os.path.isdir(folder_path):
            print(f"Resizing images in folder: {folder_name}")
            
            # Iterate through each image file in the folder
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                
                # Load the image
                image = cv2.imread(file_path)
                
                # Resize the image while maintaining the aspect ratio
                resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
                
                # Save the resized image back to the same folder
                cv2.imwrite(file_path, resized_image)
                
            print("Images resized and saved successfully.")


image_dir = 'D://ML DL AI DSBDA//Mushroom Classification using Deep Learning//archive//Mushrooms//'
changeDimensions(image_dir, 256, 256)