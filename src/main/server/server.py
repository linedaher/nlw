from flask import Flask
from src.main.routes.trips_routes import trips_routes_bp

app = Flask(__name__)

app.register_blueprint(trips_routes_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)