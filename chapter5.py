import cv2
import numpy as np

img = cv2.imread("resource/cards.jpg")

width,height = 250,350
pts1 = np.float32([[111,222],[285,189],[155,482],[348,437]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #ukuran setelah di crop atau di scan
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) #src,M,dSize

cv2.imshow("image", img)
cv2.imshow("output/pts2",imgOutput)
cv2.waitKey(0)