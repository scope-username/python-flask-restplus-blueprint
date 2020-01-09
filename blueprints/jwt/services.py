from flask import request
from flask_jwt_extended import (
    jwt_required, create_access_token, jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, get_jwt_claims
)
from flask_restplus import Namespace, Resource, reqparse

from extensions import jwt
from blueprints.jwt.database import *
from blueprints.jwt.models import *

service = Namespace('JWT Services',
                    description='Services to get and refresh tokens to authenticate all the services in app')

login_request = service.model("login_request", login_request_model)
login_response = service.model("login_response", login_response_model)
protected_response = service.model("protected_response", protected_response_model)
refresh_response = service.model("refresh_response", refresh_response_model)

parser = reqparse.RequestParser()
parser.add_argument('Token', type=str, required=True, location='headers')


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    permission = access_lookup(identity)
    return {
        'identity': identity,
        'permissions': permission
    }


@service.route('/login')
@service.doc(login_request)
@service.expect(login_request)
@service.response(200, 'Success Response Received', login_response)
class login(Resource):
    def post(self):
        username = str(request.json['Username'])
        password = str(request.json['Password'])
        correct_username = username_lookup(username)

        if correct_username:
            correct_password = password_lookup(username)
            if password == correct_password:
                ret = {
                    'access_token': create_access_token(identity=username),
                    'refresh_token': create_refresh_token(identity=username)
                }
                return ret, 200
            else:
                return {'msg': 'Bad Credentials'}, 401
        else:
            return {'msg': 'Bad Credentials'}, 401


@service.route('/protected')
@service.expect(parser)
@service.response(200, 'Success Response Received', protected_response)
class protected(Resource):
    @jwt_required
    def get(self):
        claims = get_jwt_claims()
        return {"username": claims['identity'], "permissions": claims['permissions']}, 200


@service.route('/refresh')
@service.expect(parser)
@service.response(200, 'Success Response Received', refresh_response)
class refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        ret = {
            'access_token': create_access_token(identity=current_user)
        }
        return ret, 200
