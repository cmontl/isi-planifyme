import requests

def test_events_api():
    API_KEY = "J1WMoqJLOG1BUP72WhyGDBqCxGKqGpX4"
    city = "Madrid"
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}&city={city}&size=5"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error {response.status_code}")
        print(response.text)
        return

    data = response.json()

    if "_embedded" in data:
        eventos = data["_embedded"]["events"]
        print(f"Eventos en {city}:\n")
        for i, evento in enumerate(eventos, 1):
            nombre = evento["name"]
            fecha = evento["dates"]["start"].get("localDate", "sin fecha")
            lugar = evento["_embedded"]["venues"][0].get("city", {}).get("name", "desconocido")
            print(f"{i}. {nombre} – {fecha} – {lugar}")
    else:
        print("No se encontraron eventos para esa ciudad.")

if __name__ == "__main__":
    test_events_api()
