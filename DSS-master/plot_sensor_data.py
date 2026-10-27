import csv
import matplotlib.pyplot as plt

samples = []
temperatures = []

with open("csv files/sensor_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        samples.append(int(row["sample"]))
        temperatures.append(float(row["temperature"]))

plt.plot(samples, temperatures, marker="o")
plt.xlabel("Sample")
plt.ylabel("Temperature (°C)")
plt.title("Sine Wave")
plt.grid(True)
plt.show()