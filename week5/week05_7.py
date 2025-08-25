import math
import numpy as np
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.set_imu_config(False,True,False) #Gyro only

# Setup the main color values:
W = [255,255,255]             # White
Z = [0,0,0]                   # Black
R = [255,0,0]                 # Red
G = [0,255,0]                 # Green
B = [0,0,255]                 # Blue
o = [255,127,0]               # Orange
g = [0, 255, 127]             # Light Green
p = [127,0,255]               # Purple

c = [255 - ind for ind in R]  # Cyan
m = [255 - ind for ind in G]  # Magenta
y = [255 - ind for ind in B]  # Yellow
b = [255 - ind for ind in o]  # Light Blue
N = [255 - ind for ind in g]  # Pink
s = [255 - ind for ind in p]  # Salad Green

arrow = [
    [Z,Z,Z,R,R,Z,Z,Z],
    [Z,Z,R,R,R,R,Z,Z],
    [Z,R,R,R,R,R,R,Z],
    [R,R,Z,R,R,Z,R,R],
    [Z,Z,Z,B,B,Z,Z,Z],
    [Z,Z,Z,B,B,Z,Z,Z],
    [Z,Z,Z,B,B,Z,Z,Z],
    [Z,Z,Z,B,B,Z,Z,Z],
]

def rotate_image(image, angle):
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    
    cx, cy = 3.5, 3.5

    rotated = [[Z for _ in range(8)] for _ in range(8)]
    for y in range(8):
        for x in range(8):
            dx = x-cx
            dy = y-cy
            src_x =  cos_a*dx + sin_a*dy + cx
            src_y = -sin_a*dx + cos_a*dy + cy

            src_x_round = int(round(src_x))
            src_y_round = int(round(src_y))

            if 0 <= src_x_round < 8 and 0 <= src_y_round < 8:
                rotated[y][x] = image[src_y_round][src_x_round]
    
    rotated_flat = [pixel for row in rotated for pixel in row]
    return rotated_flat

while True:
    try:
        orientation = sense.get_orientation_radians()
        # angle = math.atan2(orientation["pitch"],orientation["roll"])
        angle = -orientation["yaw"]
        print(angle)
        arrowTrue = rotate_image(arrow,angle)
        sense.set_pixels(arrowTrue)
        time.sleep(0.5)
    except KeyboardInterrupt: 
        break

sense.clear()