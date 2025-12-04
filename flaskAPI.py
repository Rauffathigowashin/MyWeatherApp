from flask import Flask, request, jsonify, render_template, send_from_directory  # send_from_directory əlavə edildi
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/style.css")
def serve_css():
    return send_from_directory('.', 'style.css')

@app.route("/api/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "city required"}), 400
    params = {'q': city, 'appid': API_KEY, 'units': 'metric', 'lang': 'az'}
    r = requests.get(BASE_URL, params=params, timeout=10)
    if r.status_code != 200:
        return jsonify(r.json()), r.status_code
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True)