import requests

API_KEY = "f90ec09814c003a7b8a297f6d78bff07"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return {
        "ciudad": city,
        "temperatura": data["main"]["temp"],
        "humedad": data["main"]["humidity"],
        "estado": data["weather"][0]["description"].capitalize()
    }
    