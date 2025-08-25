import numpy as np
import cv2

#create a VideoCapture object that represents the camera:
cap = cv2.VideoCapture(0)   # 0 is the Vid0

red, frame = cap.read()

cv2.imshow("Color image", frame)
cv2.waitKey( 0 )
# cv2.destroyAllWindows()


greyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.imshow("Greyscale image", greyFrame)
cv2.waitKey( 0 )
# cv2.destroyAllWindows()


ret, binaryFrame = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
cv2.imshow("Black and White image", binaryFrame)
cv2.waitKey( 0 )
cv2.destroyAllWindows()

while(True):
    #Capture a frame:
    red, frame = cap.read()
    ret, binaryFrame = cv2.threshold(frame,48,255,cv2.THRESH_BINARY)
    cv2.imshow('Webcam',binaryFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


while(True):
    #Capture a frame:
    red, frame = cap.read()
    greyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # arrFrame = np.array(greyFrame, dtype='uint8')
    binaryFrame = cv2.adaptiveThreshold(
        greyFrame,255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        21, 4
        )
    contours, _ = cv2.findContours(
        binaryFrame,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    # contourFrame = np.zeros_like(frame)
    contourFrame = np.full_like(frame,255)
    cv2.drawContours(contourFrame, contours, -1, (255, 127, 127), 1)

    cv2.imshow('Webcam',contourFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Clean-up when done
cap. release()
cv2.destroyAllWindows()
