from flask import Blueprint
from flask_restplus import Api
import os
import base64

from blueprints.blueprint1.namespace1.namespace1 import namespace as namespace1
from blueprints.blueprint1.namespace2.namespace2 import namespace as namespace2

username = os.environ.get("AUTHENTICATION_USERNAME")
password = os.environ.get("AUTHENTICATION_PASSWORD")

blueprint = Blueprint('blueprint2', __name__, url_prefix='/blueprint2')

api = Api(blueprint, version='1.0',
          title='blueprint2 APIs',
          description='more details of blueprint2 APIs'
          )

api.add_namespace(namespace1, path='/namespace1')
api.add_namespace(namespace2, path='/namespace2')
