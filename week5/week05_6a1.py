from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)

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

while True:
    temp = sense.temp
    pixels = [R if i < temp else B for i in range(64)]
    sense.set_pixels(pixels)