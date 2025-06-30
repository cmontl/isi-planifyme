from flask import Blueprint, jsonify, request
from app.services import events, movies, weather

api = Blueprint('api', __name__)

@api.route('/api/events', methods=['GET'])
def get_events():
    city = request.args.get('city', 'Madrid')
    try:
        result = events.get_events(city)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/movies', methods=['GET'])
def get_movies():
    try:
        result = movies.get_now_playing()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Madrid')
    try:
        result = weather.get_weather(city)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
