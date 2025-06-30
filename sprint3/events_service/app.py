from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "J1WMoqJLOG1BUP72WhyGDBqCxGKqGpX4"

@app.route('/events')
def get_events():
    city = request.args.get('city', 'Madrid')
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}&city={city}&size=5"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        eventos = []
        if "_embedded" in data:
            for e in data["_embedded"]["events"]:
                eventos.append({
                    "name": e["name"],
                    "date": e["dates"]["start"].get("localDate", ""),
                    "city": e["_embedded"]["venues"][0].get("city", {}).get("name", "")
                })

        return jsonify({"events": eventos})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "No se pudieron obtener eventos"}), 500

if __name__ == '__main__':
    app.run(port=5003)
