'''
This program will be training in Object-orienting programming.
Part 2: Weather log:
'''
class clear():

    def screen():
        from os import system
        system("clear||cls")

class calibrated:
    def temperature(temp):
        import os
        cpu_temp = os.popen("vcgencmd measure_temp").readline()
        print(cpu_temp)
        cpu_temp = float(cpu_temp.replace("temp=", "").replace("'C\n", ""))
        correction_factor = 0.75  # Примерное значение
        return(temp - ((cpu_temp - temp) / correction_factor))

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
        # temperatures = [sample[1] for sample in self.samples]
        # import matplotlib.pyplot as plt
        # fig = plt.figure()
        # ax = fig.subplots()
        # ax.plot([range(self.countSamples-1)],temperatures)
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
