from flask import Flask, redirect, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city_name')
        try:
            url = ("http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=505ae3ba084fe03f0b8071d9da4d6836").format(city_name)
            data = requests.get(url).json()
        except requests.exceptions.HTTPError:
            pass
        #choosing data from the json response
        print(data['weather'][0]['description'])

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)