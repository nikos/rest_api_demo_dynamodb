import logging
import traceback

from flask import request
from flask_jwt import jwt_required
from flask_restplus import Api, Resource
from pynamodb.exceptions import DoesNotExist

import settings
from models import User

log = logging.getLogger(__name__)

api = Api(version='1.0', title='My Blog API',
          description='A simple demonstration of a Flask RestPlus powered API')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(DoesNotExist)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/protected')
class Protected(Resource):
    @jwt_required()
    def get(self):
        print(User.count())
        # print(User.dumps())
        # User.query('Smith', first_name__begins_with='J'):
        first_user = None
        for user in User.scan():
            print(dict(user))
            first_user = user

        # return '%s' % current_identity
        return dict(first_user)


@api.route('/mylogin')
class Unprotected(Resource):
    def post(self):
        print(request.get_json(silent=True))
        return {'status': 'ok'}
