import requests

def test_weather_integration():
    response = requests.get("http://localhost:5000/api/weather?city=Madrid")
    assert response.status_code == 200
    data = response.json()
    assert "city" in data and "temperature" in data and "description" in data

def test_movies_integration():
    response = requests.get("http://localhost:5000/api/movies")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        movie = data[0]
        assert "title" in movie and "release_date" in movie

def test_events_integration():
    response = requests.get("http://localhost:5000/api/events?city=Madrid")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        event = data[0]
        assert "name" in event and "date" in event and "city" in event
