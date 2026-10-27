#Libraries für mathem. und zeitl. Funktionen
#Library für cvs Datien, um den "Sensor-Daten"  speichern zu können
#Libraries für einen Zeitstempel
import math
import time
import csv
from datetime import datetime, timezone

#Simulationsparameter definieren
#AVERAGE_TEMP -/+ AMPLITUDE
MACHINE_NAME = "Maschine-01"
AVERAGE_TEMP = 20
AMPLITUDE = 5
PERIOD = 20

#Zaehler, der die generierte Messungen "trackt"
sample = 0

# CSV Datei erstellen und öffnen
with open("../csv files/sensor_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "sample", "machine", "temperature"])

    #Simulationsschleife
    #Simultion: Generiert ein Zeitstempel -> berechnet den Temperatur -> drückt dies aus und speichert die MEssungen -> inkrementiert den Zaehler und wartet eine Sekunde
    while True:
        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        temperature = AVERAGE_TEMP + AMPLITUDE * math.sin(2 * math.pi * sample / PERIOD)

        print(f"{timestamp} | {MACHINE_NAME} | {temperature:.2f} °C", flush=True)

        writer.writerow([timestamp, sample, MACHINE_NAME, f"{temperature:.2f}"])
        file.flush()

        sample += 1
        time.sleep(1)