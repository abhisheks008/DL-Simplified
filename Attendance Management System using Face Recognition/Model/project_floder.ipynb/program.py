import face_recognition
import cv2
import numpy as np
imgElon= face_recognition.load_image_file('imagebasic/elonmuk1.jpg')
imgElon=cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgTest= face_recognition.load_image_file('imagesatted/elonmuk1.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

#step2 find faces and their encodings
faceLoc=face_recognition.face_locations(imgElon)[0]  #0-single image
encodeElon=face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)


faceLocTests=face_recognition.face_locations(imgTest)[0]  #0-single image
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTests[3],faceLocTests[0]),(faceLocTests[1],faceLocTests[2]),(255,0,255),2)



#step3 comparing faces and finding faces

results= face_recognition.compare_faces([encodeElon],encodeTest)


#to find best match
faceDis=face_recognition.face_distance([encodeElon],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {faceDis[0],2}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)
