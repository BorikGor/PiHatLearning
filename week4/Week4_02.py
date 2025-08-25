import numpy as np
import cv2

#create a VideoCapture object that represents the camera:
cap = cv2.VideoCapture(0)   # 0 is the Vid0

#Display the captured frames one-by-one in an infinite loop
while(True):
    #Capture a frame:
    red, frame = cap.read()
    cv2.imshow('Webcam',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Clean-up when done
cap. release()
cv2.destroyAllWindows()