# Libraries
from threading import Lock
from flask import Flask, jsonify, request

# Flask Anwendung erstellen
app = Flask(__name__)

# Liste zum Speichern der Sensormessungen
measurements = []

# Lock fuer den sicheren Zugriff auf die Messdaten
lock = Lock()

# Erforderliche Felder einer Messung
REQUIRED_FIELDS = [
    "timestamp",
    "sample",
    "machine",
    "temperature"
]


# 1. GET: Pruefen, ob der Server erreichbar ist
@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


# 2. POST: Messdaten von den Sensoren empfangen
@app.post("/measurements")
def add_measurement():

    # JSON-Daten aus der HTTP-Anfrage lesen
    data = request.get_json(silent=True)

    # Pruefen, ob gueltige JSON-Daten vorhanden sind
    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid JSON data"
        }), 400

    # Pruefen, ob alle erforderlichen Felder vorhanden sind
    missing = [
        field for field in REQUIRED_FIELDS
        if field not in data
    ]

    if missing:
        return jsonify({
            "error": "Missing fields",
            "fields": missing
        }), 400

    # Datentypen pruefen
    if not isinstance(data["machine"], str) or not data["machine"]:
        return jsonify({"error": "Invalid machine"}), 400

    if not isinstance(data["timestamp"], str):
        return jsonify({"error": "Invalid timestamp"}), 400

    if type(data["sample"]) is not int:
        return jsonify({"error": "Invalid sample"}), 400

    if type(data["temperature"]) not in (int, float):
        return jsonify({"error": "Invalid temperature"}), 400

    # Messung sicher speichern
    with lock:
        measurements.append(data)

    return jsonify({
        "message": "Measurement stored successfully",
        "measurement": data
    }), 201


# 3. GET: Gespeicherte Messdaten abrufen
@app.get("/measurements")
def get_measurements():

    # Optional nach einer Maschine filtern
    machine = request.args.get("machine")

    with lock:
        result = [
            measurement
            for measurement in measurements
            if not machine or measurement["machine"] == machine
        ]

    return jsonify(result), 200


# 4. GET: Letzte Messung einer Maschine abrufen
@app.get("/measurements/latest")
def get_latest_measurement():

    # Maschinenname aus URL auslesen
    machine = request.args.get("machine")

    if not machine:
        return jsonify({
            "error": "Machine parameter required"
        }), 400

    # Neueste Messung dieser Maschine suchen
    with lock:
        for measurement in reversed(measurements):
            if measurement["machine"] == machine:
                return jsonify(measurement), 200

    return jsonify({
        "error": "No measurements found"
    }), 404


# 5. REST Server starten
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
