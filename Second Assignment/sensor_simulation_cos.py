# Libraries
import math
import time
import csv
import os
import requests
from datetime import datetime, timezone

# Simulationsparameter
MACHINE_NAME = "Maschine-02"

AVERAGE_TEMP = 20
AMPLITUDE = 5
PERIOD = 20

# REST Server Adresse
REST_URL = os.getenv(
    "REST_URL",
    "http://dss-rest:5000"
)

# Zaehler fuer generierte Messungen
sample = 0

# CSV Datei erstellen und oeffnen
with open("sensor_data_cos.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "sample", "machine", "temperature"])

    # Simulationsschleife
    while True:

        # 1. Zeitstempel generieren
        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

        # 2. Temperatur mit Cosinusfunktion berechnen
        temperature = AVERAGE_TEMP + AMPLITUDE * math.cos(
            2 * math.pi * sample / PERIOD
        )

        # 3. Messdaten fuer REST API vorbereiten
        measurement = {
            "timestamp": timestamp,
            "sample": sample,
            "machine": MACHINE_NAME,
            "temperature": round(temperature, 2)
        }

        # 5. Messung in CSV Datei speichern
        writer.writerow([
            timestamp,
            sample,
            MACHINE_NAME,
            f"{temperature:.2f}"
        ])
        file.flush()

        # 6. HTTP POST: Messung an REST Server senden
        try:
            response = requests.post(
                f"{REST_URL}/measurements",
                json=measurement,
                timeout=3
            )

        except requests.exceptions.RequestException as error:
            print(f"POST failed: {error}")

        # 8. Zaehler erhoehen und eine Sekunde warten
        sample += 1
        time.sleep(1)
