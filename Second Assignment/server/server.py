# Libraries
from flask import Flask, jsonify, request

# Flask Anwendung erstellen
app = Flask(__name__)

# Letzte Messung pro Maschine, z. B. {"Maschine-01": {...}, "Maschine-02": {...}}
latest = {}

# 1. POST: Sensor sendet eine neue Messung
@app.post("/measurements")
def add_measurement():
    data = request.get_json()

    if not data or "machine" not in data or "timestamp" not in data or "temperature" not in data:
        print("POST failed: invalid measurement received")
        return jsonify({"error": "Invalid measurement"}), 400
    
    latest[data["machine"]] = data
    print(f"POST successful: measurement received for machine {data['machine']}: {data[timestamp]} | {data[temperature]} °C")
    return jsonify(data), 201


# 2. GET: Letzte Messung einer Maschine abrufen
@app.get("/measurements/latest")
def get_latest_measurement():
    machine = request.args.get("machine")

    if machine not in latest:
        return jsonify({"error": "No measurements found"}), 404

    return jsonify(latest[machine]), 200


# 3. REST Server starten
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)