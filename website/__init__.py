# __init__.py
from flask import Flask
from .views import app_blueprint

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(app_blueprint)

    return app
