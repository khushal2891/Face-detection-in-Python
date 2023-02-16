import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('profile.png') xxx[we don't want image , we want multiple frames]
# cap= cv2.VideoCapture(0)✔️✔️✔️
cap= cv2.VideoCapture(0)
# we can use this for a video cap= cv2.VideoCapture(0)
# zero is used for webcam

while True:
    _, img =cap.read()
    gray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1,4)


    for (x,y,w,h) in faces:
        cv2.rectangle (img , (x,y), (x+w, y+h),(255,0,0),2)

#  if we press escape from our keyboard the loop will be break automatically
    cv2.imshow('img',img)
    k= cv2.waitKey(30) & 0xff
    if k==27:
         break

cap.release()
