# api_routes.py
import requests

WEATHER_API_URL = "http://127.0.0.1:5002/weather"
MOVIES_API_URL = "http://127.0.0.1:5001/movies"
EVENTS_API_URL = "http://127.0.0.1:5003/events?city=Madrid"

def get_weather():
    try:
        res = requests.get(WEATHER_API_URL)
        return res.json()
    except Exception as e:
        print(f"[❌ ERROR clima]: {e}")
        return {"error": "No se pudo obtener el clima"}

def get_movies():
    try:
        res = requests.get(MOVIES_API_URL)
        return res.json()
    except Exception as e:
        print(f"[❌ ERROR películas]: {e}")
        return {"error": "No se pudieron obtener películas"}

def get_events():
    try:
        res = requests.get(EVENTS_API_URL)
        return res.json()
    except Exception as e:
        print(f"[❌ ERROR eventos]: {e}")
        return {"error": "No se pudieron obtener eventos"}
