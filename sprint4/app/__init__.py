from flask import Flask
from routes import routes  # este sí lo usas

def create_app():
    app = Flask(__name__)
    app.secret_key = 'tu_clave_secreta'

    app.register_blueprint(routes)

    return app
