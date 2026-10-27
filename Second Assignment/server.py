from threading import Lock
from flask import Flask, jsonify, request

app = Flask(__name__)
measurements= []
lock = Lock()

REQUIRED_FIELDS = ['timestamp', 'machine', 'temperature']

# GET
@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

app.run(host="0.0.0.0", port=5000, debug=True)
if __name__ == '__main__':
