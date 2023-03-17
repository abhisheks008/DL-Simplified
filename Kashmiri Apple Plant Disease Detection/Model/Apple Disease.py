from keras.models import load_model  
from PIL import Image, ImageOps  
import numpy as np


np.set_printoptions(suppress=True)


model = load_model("D:\Open Source\DL-Simplified\Kashmiri Apple Plant Disease Detection\Model\keras_model.h5", compile=False)

class_names = open("D:\Open Source\DL-Simplified\Kashmiri Apple Plant Disease Detection\Model\labels.txt", "r").readlines()


data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
path =(r"D:\Open Source\DL-Simplified\Kashmiri Apple Plant Disease Detection\Model\Blotch.jpeg")

image = Image.open(path).convert("RGB")

size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

image_array = np.asarray(image)

normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

data[0] = normalized_image_array


prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)