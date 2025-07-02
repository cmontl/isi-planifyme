from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "f90ec09814c003a7b8a297f6d78bff07"
CITY = "Madrid"

@app.route('/weather')
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=es"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Error en la solicitud:", e)
        return jsonify({"error": "Error en la solicitud"}), 500

    try:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()

        return jsonify({
            "ciudad": CITY,
            "temperatura": temp,
            "humedad": humidity,
            "estado": description
        })
    except KeyError as e:
        print("❌ Error al procesar la respuesta JSON:", e)
        return jsonify({"error": "No se pudo procesar la respuesta del clima"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
