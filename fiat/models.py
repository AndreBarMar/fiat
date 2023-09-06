from fiat.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Fiatdata(db.Model, SerializerMixin):
    placa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250))
    detalhe = db.Column(db.String(250))
    preco = db.Column(db.Integer)



class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
