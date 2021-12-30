import cv2.cv2 as cv2

faceDetector=cv2.CascadeClassifier('Files/frontalFaceDetector.xml')
videoCapture=cv2.VideoCapture(0)

while True:
    ret,frame=videoCapture.read()

    imageGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detection=faceDetector.detectMultiScale(imageGray,scaleFactor=1.09,minNeighbors=5,minSize=(100,100))

    for (x,y,w,h) in detection:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Video",frame)

    if (cv2.waitKey(1)&0xFF==ord('q')):
        break

videoCapture.release()
cv2.destroyAllWindows()