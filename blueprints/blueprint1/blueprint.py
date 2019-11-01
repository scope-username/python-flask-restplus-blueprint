from flask import Blueprint, jsonify
from flask_restplus import Api

from blueprints.blueprint1.namespace1.namespace1 import namespace as namespace1
from blueprints.blueprint1.namespace2.namespace2 import namespace as namespace2

blueprint = Blueprint('blueprint1', __name__, url_prefix='/blueprint1')


@blueprint.errorhandler(404)
def route_not_found(e):
    return jsonify(error=str(e)), 404


api = Api(blueprint, version='1.0',
          title='blueprint1 APIs',
          description='more details of blueprint1 APIs'
          )

api.add_namespace(namespace1, path='/namespace1')
api.add_namespace(namespace2, path='/namespace2')
