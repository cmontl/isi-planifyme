from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "9c756d8e4ef6d19c5ce12756ccfec5ac"

@app.route('/movies')
def get_movies():
    try:
        url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=es-ES&page=1"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        peliculas = []
        if "results" in data:
            for movie in data["results"][:5]:
                peliculas.append({
                    "titulo": movie.get("title", "Sin título"),
                    "fecha_estreno": movie.get("release_date", "Sin fecha"),
                    "puntuacion": movie.get("vote_average", "N/A")
                })

        return jsonify({"peliculas": peliculas})
    except Exception as e:
        print(f"❌ Error en el microservicio de películas: {e}")
        return jsonify({"error": "No se pudieron obtener películas"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
