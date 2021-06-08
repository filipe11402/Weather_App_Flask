from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temperature.db'

db = SQLAlchemy(app)
from weather_app_flask import routes
