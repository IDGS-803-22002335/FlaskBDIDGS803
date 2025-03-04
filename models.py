# nos permite crear objetos y mapear objetos
from flask_sqlalchemy import SQLAlchemy


import datetime

db = SQLAlchemy()


class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    # cada una de las tablas debe tener un clave primaria
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    created_date = db.Column(db.DateTime,
                             default=datetime.datetime.now)  # cada que inserto un registro me inserta la fecha
