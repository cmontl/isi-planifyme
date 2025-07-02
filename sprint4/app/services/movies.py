import requests

API_KEY = "9c756d8e4ef6d19c5ce12756ccfec5ac"

def get_now_playing():
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=es-ES&page=1"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return [
        {
            "titulo": movie.get("title", ""),
            "fecha_estreno": movie.get("release_date", ""),
            "puntuacion": movie.get("vote_average", "N/A")
        }
        for movie in data.get("results", [])[:5]
    ]
    