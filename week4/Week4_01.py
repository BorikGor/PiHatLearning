import numpy as np
import cv2

img = cv2.imread("./ScreenS.png")

cv2.imshow("Here's my flat!", img)
cv2.imflip

cv2.waitKey( 0 )
cv2.destroyAllWindows()