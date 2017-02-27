#!/usr/bin/env python2

import os
from datetime import timedelta
import logging.config
import settings

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt import JWT, jwt_required
from flask_restplus import Api

from auth import identity, authenticate
from models import User

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
    Api(flask_app)
    #init_db()


@app.route('/protected')
@jwt_required()
def protected():
    print(User.count())
    # print(User.dumps())
    # User.query('Smith', first_name__begins_with='J'):
    first_user = None
    for user in User.scan():
        print(dict(user))
        first_user = user

    return jsonify(dict(first_user))
    # return '%s' % current_identity


@app.route('/mylogin', methods=['POST'])
def mylogin():
    print(request.get_json())
    return jsonify({'status': 'ok'})


if __name__ == "__main__":
    initialize_app(app)
    app.run(host=settings.FLASK_SERVER_HOST, port=settings.FLASK_SERVER_PORT, debug=settings.FLASK_DEBUG)
