import cv2
import numpy as np
import os
from datetime import datetime
from deepface import DeepFace

# Path to your images folder
path = 'imagesatted'
images = []
classNames = []

# List the files in the images folder
mylist = os.listdir(path)
print(mylist)

# Load images and extract class names
for cls in mylist:
    curImg = cv2.imread(os.path.join(path, cls))
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])
print(classNames)

# Function to find face encodings using DeepFace
def findEncodings(images):
    encodeList = []
    for img in images:
        try:
            encodings = DeepFace.represent(img, model_name='VGG-Face')
            if encodings:
                encodeList.append(encodings[0]["embedding"])
        except Exception as e:
            print(f"Error encoding image: {e}")
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
    if not success:
        break
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    try:
        # Detect faces in the current frame
        facesCurFrame = DeepFace.extract_faces(imgS, detector_backend='mtcnn', enforce_detection=False)
    except Exception as e:
        print(f"Detection error: {e}")
        continue

    for face in facesCurFrame:
        faceLoc = face["facial_area"]
        faceImg = face["face"]
        try:
            encodeFace = DeepFace.represent(faceImg, model_name='VGG-Face', enforce_detection=False)[0]["embedding"]
        except Exception as e:
            print(f"Representation error: {e}")
            continue

        distances = np.linalg.norm(np.array(encodeListKnown) - encodeFace, axis=1)
        matchIndex = np.argmin(distances)
        total_attempts += 1  # Increment total attempts
        if distances[matchIndex] < 0.6:  # Threshold for a valid recognition
            correct_recognitions += 1  # Increment correct recognitions
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc["y"], faceLoc["x"] + faceLoc["w"], faceLoc["y"] + faceLoc["h"], faceLoc["x"]
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)

            # Calculate accuracy and display it with the name
            accuracy = (correct_recognitions / total_attempts) * 100 if total_attempts > 0 else 0
            cv2.putText(img, f"{name} {accuracy:.2f}%", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
            print("Attendance marked for", name)
        else:
            print(f"No match found. Distances: {distances}")

    # Show live camera image
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Calculate and print accuracy
if total_attempts > 0:
    accuracy = (correct_recognitions / total_attempts) * 100
    print(f'Accuracy: {accuracy:.2f}%')
else:
    print('No face recognition attempts made.')
