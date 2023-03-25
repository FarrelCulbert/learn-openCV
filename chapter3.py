import cv2
import numpy as np

img = cv2.imread("resource/Lenna.png")
print(img.shape) #(height,width)

imgresize=cv2.resize(img,(300,300)) #(width,height)
imagecropped = img[200:300,300:500] #(height,width)

cv2.imshow("image", img)
cv2.imshow("image resize",imgresize)
cv2.imshow("image cropped",imagecropped)

cv2.waitKey(0)
