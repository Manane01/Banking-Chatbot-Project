# Initialise Flask + config DB

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from config import Config
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Initialiser SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Charger la configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialiser la base de données
    db.init_app(app)

    @app.route('/')
    def home():
        return "Flask + PostgreSQL connectés avec succèes !"

    return app
