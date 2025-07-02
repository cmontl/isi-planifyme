import requests

API_KEY = "J1WMoqJLOG1BUP72WhyGDBqCxGKqGpX4"

def get_events(city):
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}&city={city}&size=5"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    eventos = []
    if "_embedded" in data:
        for e in data["_embedded"]["events"]:
            eventos.append({
                "nombre": e["name"],
                "fecha": e["dates"]["start"].get("localDate", ""),
                "lugar": e["_embedded"]["venues"][0].get("city", {}).get("name", "")
            })
    return eventos
