import cv2.cv2 as cv2
# import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread('Images/messi.jpg')
image=cv2.resize(image,(800,500))

imageBlob=cv2.dnn.blobFromImage(image=image,scalefactor=1.0/255,size=(image.shape[1],image.shape[0]))
# print(imageBlob.shape)

network=cv2.dnn.readNetFromCaffe('Files/pose_deploy_linevec_faster_4_stages.prototxt','Files/pose_iter_160000.caffemodel')
# print(network.getLayerNames())
network.setInput(imageBlob)
output=network.forward()

positionWidth=output.shape[3]
positionHeight=output.shape[2]
threshold=0.1
points=[]
for i in range(15):
    confidenceMap=output[0,i,:,:]

    _,confidence,_,point=cv2.minMaxLoc(confidenceMap)

    x=int((image.shape[1]*point[0])/positionWidth)
    y=int((image.shape[0]*point[1])/positionHeight)

    if confidence>threshold:
        cv2.circle(image,(x,y),5,(0,255,0),thickness=-1)
        cv2.putText(image,'{}'.format(i),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))
        points.append((x,y))
    else:
        points.append(None)


pointConnecton=[[0,1],[1,2],[2,3],[3,4],[1,5],[5,6],[6,7],[1,14],[14,8],[8,9],[9,10],[14,11],[11,12],[12,13]]

# plt.figure(figsize=(14,10))
# plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

for connection in pointConnecton:
    partA=connection[0]
    partB=connection[1]

    if points[partA] and points[partB]:
        cv2.line(image,points[partA],points[partB],(255,255,0),thickness=4)

cv2.imshow('image',image)
cv2.waitKey(5000)
