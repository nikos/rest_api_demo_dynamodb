#!/usr/bin/env python2

import os
from datetime import timedelta

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity

from auth import identity, authenticate
from models import User

app = Flask(__name__)
app.config["DEBUG"] = os.environ.get("DEBUG", True)
app.config["JWT_AUTH_USERNAME_KEY"] = "email"
app.config["JWT_EXPIRATION_DELTA"] = timedelta(7 * 24 * 60 * 60)
app.config["JWT_AUTH_URL_RULE"] = "/login"
app.config["SECRET_KEY"] = "Super duper secret"

CORS(app)
jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    print(User.count())
    #print(User.dumps())
    # User.query('Smith', first_name__begins_with='J'):
    first_user = None
    for user in User.scan():
        print(dict(user))
        first_user = user

    return jsonify(dict(user))
    #return '%s' % current_identity

@app.route('/mylogin', methods=['POST'])
def mylogin():
    print(request.get_json())
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run()
