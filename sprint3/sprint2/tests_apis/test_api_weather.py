import requests

def test_weather_api():
    API_KEY = "f90ec09814c003a7b8a297f6d78bff07"  # Sustituye con tu clave
    city = "Madrid"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza excepción si no es 2xx
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
        return

    data = response.json()

    # Comprobamos campos clave
    try:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"📍 Ciudad: {city}")
        print(f"🌡️  Temperatura: {temp} °C")
        print(f"💧 Humedad: {humidity}%")
        print(f"☁️  Estado: {description.capitalize()}")
    except KeyError:
        print("❌ No se pudo procesar la respuesta JSON:")
        print(data)

if __name__ == "__main__":
    test_weather_api()
