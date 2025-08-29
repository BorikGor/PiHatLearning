'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This program is an enhanced program of the week 4 lab that uses openCV to #
# get a video stream form a USB camera, but uses a CSI RPi camera instead.  #
# As it turns out the CSI camera is not as easy to access from a Python     #
# script and needs a workaround. The workaround is openninf a stream to a   #
# local port and getting the data from there, using OpenCV.                 #
#                                                                           #
# I've got a feeling, that using a C program would be easier.               #
#                                                                           #
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import subprocess
import time
import numpy as np
import cv2

# Create a strem subprocess to stream the video from the CSI camera to port 5800:

stream_process = subprocess.Popen([
    "rpicam-vid",
    "-t", "0",                     # Endless stream
    "--codec", "mjpeg",            # Format MJPEG
    "--inline",                    # Inbuilding JPEG
    "-o", "udp://127.0.0.1:5800"   # Stream to local port
])

# Give 2 seconds for the camera to start streaming:
print("Waiting for 2 seconds for the camera to come online")
time.sleep(2)
print("Done waiting for camera to come online.")

#create a VideoCapture object that represents the camera:
# cap = cv2.VideoCapture(0)   # 0 is the Vid0
cap = cv2.VideoCapture("udp://127.0.0.1:5800?overrun_nonfatal=1",cv2.CAP_FFMPEG)
print("Created the cap object, which gets the video from localHost:5800")

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
    if not ret or frame is None:
        print("Skipping frame\n")
        continue
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

# Stop the streaming from the CSI camera to the local port:
stream_process.terminate()
