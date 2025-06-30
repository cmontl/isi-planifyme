import requests

def test_events_service():
    url = "http://localhost:5003/events?city=Madrid"
    response = requests.get(url)

    assert response.status_code == 200, f"Status code: {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "Expected a list of events"

    if data:
        event = data[0]
        assert "name" in event
        assert "date" in event
        assert "city" in event
        assert isinstance(event["name"], str)
        assert isinstance(event["date"], str)
        assert isinstance(event["city"], str)
