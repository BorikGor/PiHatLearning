# A program to record and analyse weather data
import time
import random
import math
import statistics

class Weather:
    def get_weather():
        # return a few random values in place of actual sensor data
        temp = int(random.uniform(8, 30))
        humidity = int(random.uniform(0, 100))
        pressure = int(random.uniform(950, 1050))
        time_ms = int(time.time_ns()/1000000)
        return (time_ms, temp, humidity, pressure)

class Log:
    # number of weather readings
    count_samples = 0

    # list of weather readings
    samples = []

    # add a new weather reading
    def add(self, reading):
        self.count_samples = 1 + self.count_samples
        self.samples.append(reading)

    # display sampled weather data
    def plot_samples(self, output_samples):
        print("Timestamp (ms) | Temp (°C) | Humidity (%) | Pressure (hPa)")
        for sample in output_samples:
            print(f"{sample[0]:<15}| {sample[1]:<10}| {sample[2]:<13}| {sample[3]}")

    # display stored weather data
    def plot(self):
        self.plot_samples(self.samples)

    # Calculate derivative information for sampled weather data

    # Extract all measurements of a certain variable from the samples
    def select_var(self, index, input_samples=None):
        if input_samples is None:
            input_samples = self.samples
        return [ sample[index] for sample in input_samples ]

    # Extract all measurements within a recent time period
    def select_recent(self, time_ms):
        return [sample for sample in self.samples if sample[0] >= time_ms]

    # Get the most recent sample based on the timestamps
    def most_recent(self):
        timestamps = self.select_var(0)
        max_index = timestamps.index(max(timestamps))
        return self.samples[max_index]

    # Calculate dew point for the last recent sample
    def dew_point(self):
        if not self.samples:
            return None
        # Dew point depends on temperature and humidity
        (_, temp, humidity, _) = self.most_recent()

        # Use Magnus formula
        a = 17.62
        b = 243.12
        gamma = (a * temp) / (b + temp) + math.log(humidity / 100.0)
        result = (b * gamma) / (a - gamma)
        return round(result, 1)

    # Calculate average values
    def average(self, samples):
        av_time = statistics.mean(self.select_var(0, samples))
        av_temp = statistics.mean(self.select_var(1, samples))
        av_humidity = statistics.mean(self.select_var(2, samples))
        av_pressure = statistics.mean(self.select_var(3, samples))
        av_sample = (av_time, av_temp, av_humidity, av_pressure);
        return [ av_sample ]

class WeatherApp:
    def menu(self):
        self.weather_log = Log()
        option = 0
        while option <= 4:
            print("1) Measure current weather")
            print("2) Show all measurements")
            print("3) Print dew point")
            print("4) Average over the last 10 seconds")
            print("5) Exit")
            option = int(input("> "))
            if 1 == option:
                reading = Weather.get_weather()
                print(reading)
                self.weather_log.add(reading)
            elif 2 == option:
                self.weather_log.plot()
            elif 3 == option:
                recent_dew_point = self.weather_log.dew_point()
                print("Dew point: ", recent_dew_point, " degree Celsius")
            elif 4 == option:
                now_ms = int(time.time_ns()/1000000)
                earliest_ms = now_ms - 10 * 1000
                recent_samples = self.weather_log.select_recent( earliest_ms )
                print("Samples from the past 10s:")
                self.weather_log.plot_samples(recent_samples)
                av_samples = self.weather_log.average(recent_samples)
                print("Average:")
                self.weather_log.plot_samples(av_samples)

app = WeatherApp()
app.menu()
print("*** End ***")
