import time
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

L = R
ya = [
    B,B,L,L,L,L,L,B,
    B,L,B,B,B,B,L,B,
    B,L,B,B,B,B,L,B,
    B,B,L,L,L,L,L,B,
    B,B,B,B,L,B,L,B,
    B,B,B,L,B,B,L,B,
    B,B,L,B,B,B,L,B,
    B,L,B,B,B,B,L,B,
]
#sense.set_pixels(ya)


def generate_gamma_table(clear_value):
    """
    Generate a 32-element gamma table for the Sense HAT based on ambient light level.
    - When clear_value = 256, returns gamma_def.
    - When clear_value = 0, returns [0,...,0,1].
    - Smooth interpolation in between using a power curve.
    """

    # Clamp clear_value to [0, 256]
    clear_value = max(0, min(256, clear_value))

    # Normalize brightness to [0, 1]
    brightness = clear_value / 256.0

    # Use a smooth interpolation curve (cubic easing)
    # This curve keeps values non-zero even at low brightness
    scale = brightness ** 0.7  # less aggressive than square or higher powers

    # Generate gamma table
    gamma_scaled = []
    for i, val in enumerate(gamma_def):
        if brightness == 0.0:
            gamma_scaled.append(1 if i == 31 else 0)
        else:
            scaled_val = int(round(val * scale))
            gamma_scaled.append(max(0, min(31, scaled_val)))

    return gamma_scaled

# Base gamma definition
gamma_def = [0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 21, 23, 25, 27, 29, 31]
gamma_dim = gamma_def

# Screen test:
#colors = [W, Z, R, G, B, o, g, p, c, m, y, b, s, N]
colors = [Z, N, R, o, y, s, G, g, c, b, B, m, p, W]

# Loop through and display each color
for TestColor in colors:
    sense.clear(TestColor)
    time.sleep(0.3)

print(sense.color.gain)
sense.color.gain = 16
# print("Gamma settings:")
# print(sense.gamma)

while True:
    time.sleep(2 * sense.colour.integration_time)
    red, green, blue, clear = sense.colour.colour # readings scaled to 0-256
#    print(f"R: {red}, G: {green}, B: {blue}, C: {clear}")
#    dimmer = 1+round(30*(1-(clear/256)))
    gamma_dim = generate_gamma_table(clear)
#    print(str(gamma_dim) +' '+ str(clear))
    sense.gamma = gamma_dim

    humidity = round(sense.get_humidity(),1)
    hum_txt = str(humidity)
    temperature_s = round(sense.get_temperature(),0)
    temperature_h = round(sense.get_temperature_from_humidity(),0)
    temperature_p = round(sense.get_temperature_from_pressure(),0)
    tmp_txt = str(temperature_s)
    # sense.show_message(f"Humidity: " + hum_txt + "% ",text_colour=p)
    # sense.show_message(f"Temp= " + tmp_txt + "C ",text_colour=s)
    sense.show_message(f"{temperature_s}")
    #time.sleep(2)