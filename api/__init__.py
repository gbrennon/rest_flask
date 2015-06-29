from flask import Flask
from flask.ext.restful import Api
from flask.ext.mongoengine import MongoEngine
from flask.ext.marshmallow import Marshmallow
from flask.ext.heroku import Heroku
from config import DevConfig

api = Api()
db = MongoEngine()
ma = Marshmallow()
heroku = Heroku()


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    heroku.init_app(app)
    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)
    return app

from controllers import *
