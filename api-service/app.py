from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "service": "library-api"})

@app.route("/api/documents")
def documents():
    return jsonify([
        {"id": 1, "title": "Пример документа", "author": "Иванов И.И."}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("API_PORT", "5000")))