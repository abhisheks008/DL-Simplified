import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime
import tkinter as tk
from PIL import ImageTk, Image

def button():
    path= 'imagesatted'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
        curImg=cv2.imread(f'{path}/{cls}')
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])
    print(classNames)
    def findEncodings(images):
        encodeList =[]
        for img in images:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode=face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    def markAttendence(name):
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            print(myDataList)
            nameList=[]
            for line in myDataList:
                entry= line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString=now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

    encodeListKnown = findEncodings(images)
    print('Encoding complete')
    cap=cv2.VideoCapture(0)
    total_attempts = 0
    correct_recognitions = 0
    while True:
        success, img=cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
        facesCurFrame =face_recognition.face_locations(imgS)#TOP < BOTTOM< LEFT < RIGHT
        encodesCurFrame=face_recognition.face_encodings(imgS,facesCurFrame)
        #print(encodesCurFrame)
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            #print(encodeFace)
            total_attempts += 1
            print(faceLoc)
            matches= face_recognition.compare_faces(encodeListKnown,encodeFace)
            print(matches)
            faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex=np.argmin(faceDis)
            if matches[matchIndex]:
                correct_recognitions += 1
                name= classNames[matchIndex].upper()
                accuracy = (correct_recognitions / total_attempts) * 100  # Calculate accuracy

                y1,x2,y2,x1=faceLoc
                y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4

                print(name)
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,f'{name} ({accuracy:.2f}%)',(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2) #2- thickness
                markAttendence(name)
                print("Attendance marked for", name)


        #shows live camera image
        cv2.imshow('Webcam',img)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Create the main application window
root = tk.Tk()
root.title("Attendance System")

# Create a button for marking attendance
def hide_window():
 root.destroy()
root.protocol("WM_DELETE_WINDOW", hide_window) # Hide window when close button is clicked
root.maxsize(width=800, height=600)
root.title("Face Recognition System")
root.geometry("800x600")
image = Image.open("imagebasic/bg.jpg") # Replace "path_to_image_file.jpg" with the actual path to your
#image file
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()),)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
l = tk.Label(root, text='Welcome Face Recognition System', font="Calibri 18 bold", bg='#CAEBF0')
l.place(x=250, y=100)
mark_button = tk.Button(root, text="Mark Attendance", command=button)
mark_button.pack(pady=20)
mark_button.place(x=350,y=250)

# Run the Tkinter event loop
root.mainloop()
