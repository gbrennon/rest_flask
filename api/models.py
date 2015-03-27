from api import db


class Atividade(db.Document):
    nome = db.StringField(required=True)
    descricao = db.StringField(required=True)


class Praia(db.Document):
    nome = db.StringField(required=True)
    descricao = db.StringField(required=True)
    atividades = db.ListField(db.ReferenceField('Atividade'))
