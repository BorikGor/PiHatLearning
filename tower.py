import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(90)


with open('tower.conf', 'r') as file:
    lines = file.readlines()
    for line in lines:
        times = int(line[0])
        for cnt in range(0,times):
            print(line.strip()[2:])
    