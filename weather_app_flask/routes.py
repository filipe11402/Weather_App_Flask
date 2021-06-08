from flask import redirect, render_template, request
from weather_app_flask.models import City
from weather_app_flask import app


@app.route('/')
def index():
    cities = City.query.all()
    print(cities)

    return render_template('index.html')


"""
            data desired to get from API
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
"""