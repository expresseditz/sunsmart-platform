from flask import Flask
from flask_cors import CORS
from config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    @app.route("/")
    def home():
        return {"message": "Backend is running"}

    from app.routes.uv_routes import uv_bp
    app.register_blueprint(uv_bp)

    return app