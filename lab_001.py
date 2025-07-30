import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(90)


name = input("What's your name? ")
print("Hello, "+name+" pie!")

