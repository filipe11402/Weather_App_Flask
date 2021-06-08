from weather_app_flask import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(50), unique=True)
    temperature = db.Column(db.Float)
    description = db.Column(db.String(50))
    icon = db.Column(db.String(20))

    def __str__(self):
        return self.city_name
