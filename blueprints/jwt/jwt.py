from flask import Blueprint
from flask_restplus import Api

from blueprints.jwt.services import service

jwt_bp = Blueprint('jwt_bp', __name__, url_prefix='/jwt')

api = Api(jwt_bp, version='1.0',
          title='jwt',
          description='JSON Web Token Blueprint'
          )

api.add_namespace(service, path='/service')
