import requests

def test_movies_service():
    url = "http://localhost:5002/movies"
    response = requests.get(url)

    assert response.status_code == 200, f"Status code: {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "Expected a list of movies"

    if data:
        movie = data[0]
        assert "title" in movie
        assert "release_date" in movie
        assert "rating" in movie
        assert isinstance(movie["title"], str)
        assert isinstance(movie["release_date"], str)
        assert isinstance(movie["rating"], (int, float))

