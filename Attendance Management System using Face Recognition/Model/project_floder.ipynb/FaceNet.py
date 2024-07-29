import numpy as np
import cv2
import os
from datetime import datetime
from tensorflow.keras.models import load_model
from mtcnn import MTCNN
from numpy import asarray, expand_dims

# Load the pre-trained FaceNet model
model = load_model('facenet_keras.h5')

# Function to preprocess the face for FaceNet model
def preprocess_face(face):
    face = cv2.resize(face, (160, 160))
    face = face.astype('float32')
    mean, std = face.mean(), face.std()
    face = (face - mean) / std
    face = expand_dims(face, axis=0)
    return face

# Function to get the face embedding using FaceNet
def get_embedding(model, face):
    face = preprocess_face(face)
    embedding = model.predict(face)
    return embedding[0]

# Path to your images folder
path = 'imagesatted'
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)
for cls in mylist:
    curImg = cv2.imread(os.path.join(path, cls))
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])
print(classNames)

# Initialize MTCNN face detector
detector = MTCNN()

# Function to find face encodings for all images in the folder
def findEncodings(images):
    encodeList = []
    for img in images:
        results = detector.detect_faces(img)
        if results:
            x1, y1, width, height = results[0]['box']
            x2, y2 = x1 + width, y1 + height
            face = img[y1:y2, x1:x2]
            encode = get_embedding(model, face)
            encodeList.append(encode)
    return encodeList

# Function to mark attendance
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

# Find encodings for known faces
encodeListKnown = findEncodings(images)
print('Encoding complete')

# Initialize webcam
cap = cv2.VideoCapture(0)

total_attempts = 0
correct_recognitions = 0

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Failed to capture image from camera.")
        continue

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = detector.detect_faces(imgS)
    encodesCurFrame = []

    for result in facesCurFrame:
        x1, y1, width, height = result['box']
        x2, y2 = x1 + width, y1 + height
        face = imgS[y1:y2, x1:x2]
        encode = get_embedding(model, face)
        encodesCurFrame.append((encode, (x1, y1, x2, y2)))

    for encodeFace, faceLoc in encodesCurFrame:
        total_attempts += 1
        distances = np.linalg.norm(np.array(encodeListKnown) - encodeFace, axis=1)
        matchIndex = np.argmin(distances)
        if distances[matchIndex] < 0.6:  # Threshold for a valid recognition
            correct_recognitions += 1
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)

            # Calculate accuracy and display it with the name
            accuracy = (correct_recognitions / total_attempts) * 100 if total_attempts > 0 else 0
            cv2.putText(img, f"{name} {accuracy:.2f}%", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
            print("Attendance marked for", name)

    # Show live camera image
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Calculate and print final accuracy
if total_attempts > 0:
    accuracy = (correct_recognitions / total_attempts) * 100
    print(f'Final Accuracy: {accuracy:.2f}%')
else:
    print('No face recognition attempts made.')
