import requests

def test_weather_service():
    city = "Madrid"
    url = f"http://localhost:5001/weather/{city}"
    response = requests.get(url)

    assert response.status_code == 200, f"Status code: {response.status_code}"
    
    data = response.json()
    assert "temperature" in data
    assert "humidity" in data
    assert "description" in data
    assert isinstance(data["temperature"], (int, float))
    assert isinstance(data["humidity"], int)
    assert isinstance(data["description"], str)
