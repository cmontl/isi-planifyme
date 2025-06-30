import requests

def test_movies_api():
    API_KEY = "9c756d8e4ef6d19c5ce12756ccfec5ac"  # Sustituye por tu clave real
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=es-ES&page=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Error en la solicitud:", e)
        return

    data = response.json()

    if "results" in data:
        print("🎬 Primeras 5 películas en cartelera:\n")
        for i, movie in enumerate(data["results"][:5], 1):
            title = movie.get("title", "Sin título")
            release_date = movie.get("release_date", "Sin fecha")
            rating = movie.get("vote_average", "N/A")
            print(f"{i}. {title} – Fecha de estreno: {release_date} – Puntuación: {rating}/10")
    else:
        print("No se encontraron resultados válidos.")
        print(data)

if __name__ == "__main__":
    test_movies_api()
