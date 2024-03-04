from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()

# relative path: src/backend/app/data/sp500_p1_sm.sqlite
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLITE_DB_FILE = os.path.join(BASE_DIR, 'data', 'sp500_p1_sm.sqlite') 
SQLITE_DB_URI = f'sqlite:///{SQLITE_DB_FILE}'

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLITE_DB_URI
    db.init_app(app)
    return app

