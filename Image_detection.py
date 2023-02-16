# First of all install open cv using (pip install opencv-python)
import cv2

# we will use haarcascade for detecting faces 
# open cv has many classfiers for faces , smiles , eyes etc 
# Today we will use face classifier

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('profile.png')

# this method works only on gray scale That's why we have to convert our image into gray scale
 
gray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1,4)

# we have to draw rectangle on the faces & 2 is the thickness of the rectangle here 

for (x,y,w,h) in faces:
    cv2.rectangle (img , (x,y), (x+w, y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey()