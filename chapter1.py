import cv2
("package imported")

image capture
img = cv2.imread("resource/Lenna.png")
cv2.imshow("output", img)
cv2.waitKey(0)

#video capture
cap = cv2.VideoCapture("resource/motor.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("video", img)
   if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

#video capture
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set (10,100) #kecerahan webcam 100
while True:
   success, img = cap.read()
    cv2.imshow("video", img)
   if cv2.waitKey(1) & 0xFF ==ord('q'):
        break