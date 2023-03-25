import cv2
import numpy as np
("package imported")

img = cv2.imread("resource/Lenna.png")
kernel = np.ones((5,5),np.uint8)

imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggrey,(7,7),0)
imgcanny = cv2.Canny(img,200,200)
imgdialation = cv2.dilate(imgcanny,kernel,iterations=1)
imgroded = cv2.erode(imgdialation,kernel,iterations=1)

cv2.imshow ("grey image", imggrey)
cv2.imshow ("blur image", imgblur)
cv2.imshow ("canny image", imgcanny)
cv2.imshow ("dialation image", imgdialation)
cv2.imshow ("roded image", imgroded)

cv2.waitKey(0)

