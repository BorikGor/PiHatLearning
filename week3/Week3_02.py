'''
 This program will be training in Object-orienting programming.
 Part 2: Weather log:

The program displays a menu to the user:
    1) Measure current Weather
    2) Plot log
    3) Clear log
    4) Exit
 and acts according to the chosen menu item.
If chosen 1, the program reads the following data from the 
 Raspberry Pi SenseHat sensor and displays it onscreen as a list:
    Temperature: 17.4
    Humidity:    31.4
    Pressure:    1018.3
    Timestamp:   1754539143765.0
 The data is then stored in a local list variable.
If chosen 2, the program prints out the logged data in raw format:
    [Indx] ([timestamp in milliseconds], [temperature], [humidity], [pressure])
If chosen 3, the logged data is cleared.
if chosen 4, the program exits.
-----------------------------------------------------------------------------
Classes created for this program:
clear:
    Allows for a simple screen clearing by using the screen() method.
    usage example:
        clear.screen()

calibrated:
    Uses the single method temperature(). Allows for simple calibration of
    the temperature reading from the onboard SenseHat temperature sensor.
    usage example:
        print("calibrated.temperature(48.3)")

weather:
    Uses the single method getWeather(), reading the sensors, calling the
    calibrated.temperature() method to get the true value of the ambient
    temperature.
    Prints out the received data in a short list.

log:
    Defines two local variables:
    self.countSamples - integer, that count the amount of samples registered
    self.samples      - list of the values of sensors read by the 
                        weather.getWeather() method
    Holds the following methods:
        add()
        Calls the weather.getWeather() method and appends the received data
        to the local samples variable.
        increments the countSamples variable by 1 each time it's called.

        clear()
        clears the data from both local variables.

        plot()
        Uses the matplotlib library to plot all the currently logged
        temperature values on a plot.
        Note: this only works if the user is connected to the Raspberry Pi
        via a remote session and sees the Linux GUI. Otherwise the plot is
        not shown.
        After plotting the data, this method also prints out the "raw" data
        and waits for user to press Enter.

weatherApp:



'''
class clear():

    def screen():
        from os import system
        system("clear||cls")

class calibrated:
    def temperature(temp):
        '''
        Receives a value from the calling function, that should be the reading
        of the SenseHat onboard temperature sensor.
        Reads the CPU/Board temperature of the Pi.
        Calculates the "true" value of ambient temperature.
        Returns the resulting value to the calling function.

        Note: The value of the Correction Factor was chosen forcebly after a
        few local tests and may need to change according to Pi's environment
        and the temperature of the system (dynamic correctlion)
        '''
        import os
        print("CPU")
        cpu_temp = os.popen("vcgencmd measure_temp").readline()
        # print(cpu_temp)
        cpu_temp = float(cpu_temp.replace("temp=", "").replace("'C\n", ""))
        correction_factor = 0.75                               # Correction factor chosen iteratively.
        return(temp - ((cpu_temp - temp) / correction_factor)) # Returns the "fixed" temperature value, accounting for the board temperature.

class weather:
    def getWeather(self):
        import time
        from sense_hat import SenseHat
        sense = SenseHat()
        # input("Measuring!\r\nPress Enter to continue.")
        clear.screen()
        temperature = round(calibrated.temperature(sense.get_temperature()),1)
        humidity = round(sense.get_humidity(),1)
        pressure = round(sense.get_pressure(),1)
        timestamp = round(time.time() * 1000,0)
        input(\
              f"Temperature: "+str(temperature)+"\r\n"\
              "Humidity:    "+str(humidity)+"\r\n"\
              "Pressure:    "+str(pressure)+"\r\n"\
              "Timestamp:   "+str(timestamp)+"\r\n"\
              "Press Enter to continue.")
        return(timestamp,temperature,humidity,pressure)

class log:
    
    def __init__(self):
        self.countSamples = 0
        self.samples = []

    def add(self):
        clear.screen()
        # input("Logging.\r\nPress Enter to continue.")
        self.samples.append(weather.getWeather(self))
        self.countSamples+=1
        # print("New weather reading appended.")

    def clear(self):
        clear.screen()
        # input("Clearing Log. \r\nPress Enter to continue.")
        self.samples = []
        self.countSamples = 0
        input("Log Cleared.\r\nPress Enter to continue.")

    def plot(self):
        temperatures = [sample[1] for sample in self.samples]
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.subplots()
        print("The plot will only be seen in the RDP session to the Pi.")
        ax.plot(list(range(0,(self.countSamples))),temperatures)
        plt.show()
        plt.close()

        clear.screen()
        # print("Printing current list of sensor reading:")
        for smp, sample in enumerate(self.samples):
            print(f"{smp+1} {sample}")
        
        input("Log printed!\r\nPress Enter to continue.")

class weatherApp:

    def __init__(self):
        self.weatherLog = log()

    def menu(self):
        while(True):
            user_input = "wut"
            clear.screen()
            user_input = input("" \
                "Hello there!\r\n" \
                "Choose an option and press Enter:\r\n" \
                " 1) Measure current Weather\r\n" \
                " 2) Plot log\r\n" \
                " 3) Clear log\r\n" \
                " 4) Exit\r\n ")
            
            if user_input.isdigit():
                # input(f"Commencing option "+str(user_input)+"!\r\nPress Enter to continue.")
                if user_input == "4": break
                elif user_input == "1":
                    self.weatherLog.add()

                elif user_input == "2":
                    self.weatherLog.plot()

                elif user_input == "3":
                    self.weatherLog.clear()

                elif user_input == "0":
                    # input("Exiting. \r\nPress Enter to continue.")
                    print("+++ OUT OF CHEESE ERROR!!! +++")
                    break
                else:
                    input("Please enter a digit corresponding to the menu item you want me to do.")
            elif user_input in "Hello!hello!":
                input("Why, gutten tag to you too!\n\rWhat a gentelmen you are!\r\nPress Enter to continue.")
            else:
                input("Please enter just the digit of the menu.\r\nPress Enter to continue.")

Catrina = weatherApp()
Catrina.menu()
