import cv2.cv2 as cv2
image=cv2.imread('Images/myimage3.jpg')

# print(image.shape) #show width, height, chanel
image=cv2.resize(image,(800,600)) #resize the image

image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert color to grayscale
# cv2.destroyAllWindows()
faceDetector=cv2.CascadeClassifier('Files/frontalFaceDetector.xml')#load frontal face detecting algorithm
fdetection=faceDetector.detectMultiScale(image_gray,scaleFactor=1.11,minNeighbors=10) #detect faces #scaleFactor is used to adjust with image size
# print(detection)#print face location in x and y axis and face size in width and height
eyeDetector=cv2.CascadeClassifier('Files/eyeDetector.xml')
edetection=eyeDetector.detectMultiScale(image_gray,scaleFactor=1.05,minNeighbors=10,maxSize=(40,40))

for(x,y,w,h) in fdetection:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),3) #create a rectangle in detected images takes perameter
    # (image,starting x and y value,ending x and y value, rectangle color, rectangle thikness)

# for (x,y,w,h) in edetection:
#     cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("image",image) #display the image
cv2.waitKey(5000) #wait time in window