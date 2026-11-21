# Libraries 
import math                                                     # Mathematik-Funktionen
import time                                                     # Zeit-Funktionen
import csv                                                      # CSV-Funktionen; Read/ Write CSV Datein (Common-Separated-Values; Zum Speichern der Daten in Reiehn und Spalten; Erste Reihe besteht aus 'Headers', die mit Kommata getrennt sind; Weitere Reihen bestehen aus Daten , die zum zegehörigen Header eingeordnet sind)
import os                                                       # OS-Funktionen; Zugriff auf Umgebungsvariablen
import requests                                                 # HTTP-Funktionen; HTTP-Requests an REST-Server senden und empfangen
from datetime import datetime, timezone                         # Zeitstempel-Funktionen; Zeitstempel im ISO-Format generieren

# Hier handelt es sich um die Namen der Maschinen, die die Messungen generieren. Diese Namen werden in den Messungen gespeichert und können später zur Identifikation der Maschine verwendet werden.

MACHINE_NAME = "Maschine-01"

# Sinusfunktion Parameter zum Generieren der Temperaturwerte
AVERAGE_TEMP = 20
AMPLITUDE = 5
PERIOD = 20

# REST Server Adresse
REST_URL = os.getenv(
    "REST_URL",
    "http://dss-rest:5000"
)

# Zähler für generierte Messungen
sample = 0

# CSV Datei in einem Format erstellen und öffnen
with open("sensor_data_sin.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Header in die CSV Datei schreiben (CSV-Daten Format)
    writer.writerow(["timestamp", "sample", "machine", "temperature"])

    # Simulationsschleife
    # Ziele: Erstellt die Simulationsdaten , speichert sie in einer CSV-Datei, sendet sie an den REST-Server, wartet eine Sekunde.
    while True:

        # 1. Zeitstempel generieren
        timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

        # 2. Temperatur mit Sinusfunktion berechnen
        temperature = AVERAGE_TEMP + AMPLITUDE * math.sin(
            2 * math.pi * sample / PERIOD
        )

        # 3. Messdaten für REST API vorbereiten
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

            response.raise_for_status()

        except requests.exceptions.RequestException as error:
            print(f"POST failed: {error}")

        # 8. Zähler erhöhen und eine Sekunde warten
        sample += 1
        time.sleep(1)
