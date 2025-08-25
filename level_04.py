import math
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_imu_config(True, True, False)  # Enabling accelerometer only

# Setup the main color values:
W = [255,255,255]             # White
Z = [0,0,0]                   # Black
R = [255,0,0]                 # Red
G = [0,255,0]                 # Green
B = [0,0,255]                 # Blue
o = [255,127,0]               # Orange
g = [0, 255, 127]             # Light Green
p = [127,0,255]               # Purple

def get_bubble_position(acc_x, acc_y):
    # # Normalizing accelerations values
    # pitch = max(min(pitch, 90), -90)
    # roll = max(min(roll, 90), -90)

    # Converting into coordinates 0..7
    x = int(round(7 * (acc_x / 1)))
    y = int(round(7 * (acc_y / 1)))

    return x, y

def draw_bubble(x, y):
    pixels = [Z for _ in range(64)]
    index = y * 8 + x
    color = R if x in [0,7] or y in [0,7] else B
    pixels[index] = color
    sense.set_pixels(pixels)

# Main Loop
try:
    while True:
        acceleration = sense.get_accelerometer_raw()

        x, y = get_bubble_position(acceleration["x"],acceleration["y"])
        print(x,y)
        draw_bubble(x, y)

        time.sleep(0.1)
except KeyboardInterrupt:
    sense.clear()
