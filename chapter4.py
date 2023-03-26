import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:] = 255,0,0 #(height,width) sama kayak cropped

cv2.line(img,(200,0),(200,200),(250,0,0),2) #img,pt1,pt2(img.shape[1],img.shape[0]),color,thinkness,lineType,shift
cv2.rectangle(img,(0,0),(100,100),(0,100,20),2) #img,pt1,pt2,color,thickness,lineType,shift
cv2.circle(img,(300,350),40,(0,0,100),cv2.FILLED) #img,center,radius,color,thickness,lineType,shift
cv2.putText(img,"OpenCV",(250,200),5,2,(100,250,20)) #img,text,org,fontface(0-7),fontscale,color,thickness,linetype,BottomLeftOrigin

cv2.imshow("image", img)
cv2.waitKey(0)