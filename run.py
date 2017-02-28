#!/usr/bin/env python2

import logging.config
from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT

import settings
from app.api import api
from app.auth import identity, authenticate
from app.models import init_db

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    # flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SERVER_HOST'] = settings.FLASK_SERVER_HOST
    flask_app.config['SERVER_PORT'] = settings.FLASK_SERVER_PORT
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

    flask_app.config['JWT_AUTH_URL_RULE'] = settings.JWT_AUTH_URL_RULE
    flask_app.config['JWT_AUTH_USERNAME_KEY'] = settings.JWT_AUTH_USERNAME_KEY
    flask_app.config['JWT_EXPIRATION_DELTA'] = timedelta(settings.JWT_EXPIRATION_DELTA)
    flask_app.config['SECRET_KEY'] = settings.SECRET_KEY


def initialize_app(flask_app):
    configure_app(flask_app)
    CORS(flask_app)
    JWT(flask_app, authenticate, identity)
    api.init_app(flask_app)
    init_db()


if __name__ == "__main__":
    initialize_app(app)
    app.run(host=settings.FLASK_SERVER_HOST, port=settings.FLASK_SERVER_PORT, debug=settings.FLASK_DEBUG)
