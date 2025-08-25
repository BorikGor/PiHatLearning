from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(0)

e = (0,0,0)
w = (255,255,255)

# Setup the main color values:
# W = [255,255,255]             # White
# Z = [0,0,0]                   # Black
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

sense.clear()
while True:
    for event in sense.stick.get_events():
        # Check the jpystick was pressed
        if event.action == 'pressed':
            # Check which direction
            if event.direction == 'up':
                sense.show_letter("U")
            elif event.direction == 'down':
                sense.show_letter("D")
            elif event.direction == 'left':
                sense.show_letter("L")
            elif event.direction == 'right':
                sense.show_letter("R")
            elif event.direction == 'middle':
                sense.show_letter("M")
            # wait a while and then clear the screen
            sleep(0.5)
            sense.clear()
