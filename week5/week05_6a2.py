from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(0)
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

print(sense.humidity)