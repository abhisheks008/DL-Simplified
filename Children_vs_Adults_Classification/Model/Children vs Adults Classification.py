from keras.models import load_model 
import cv2 
import numpy as np

np.set_printoptions(suppress=True)

model = load_model("D:\Open Source\DL-Simplified\Children_vs_Adults_Classification\Model\keras_model.h5", compile=False)

class_names = open("D:\Open Source\DL-Simplified\Children_vs_Adults_Classification\Model\labels.txt", "r").readlines()

camera = cv2.VideoCapture(0)

def Find_Chid_vs_Adult():
    ret, image = camera.read()
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    image = (image / 127.5) - 1

    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    keyboard_input = cv2.waitKey(1)

    

while True:
    Find_Chid_vs_Adult()
    
    if class_names=='Children':
        break
cv2.destroyAllWindows()