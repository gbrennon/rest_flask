from api import db


class Ranking(db.Document):
    nome = db.StringField(required=True)
    email = db.EmailField(required=True)
    avatar = db.StringField(required=True)
    pontos = db.IntField(required=True)
