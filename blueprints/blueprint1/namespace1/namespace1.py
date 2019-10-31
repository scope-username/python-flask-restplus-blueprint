from flask import request
from flask_restplus import Namespace, Resource

from blueprints.blueprint1.namespace1.models.models import *
from blueprints.blueprint1.namespace1.services.get_service import get_service
from blueprints.blueprint1.namespace1.services.post_service import post_service

namespace = Namespace('namespace1', description='namespace1 related stuff')

namespace1_service2_request_data = namespace.model("namespace1_service2_request_data", namespace1_service2_request_data_model)

namespace1_service2_response_data = namespace.model("namespace1_service2_response_data", namespace1_service2_response_data_model)

error_response_data = namespace.model("error_response_data", error_response_data_model)


class DefaultErrorHandle(Exception):
    pass


@namespace.errorhandler(DefaultErrorHandle)
def default_error_handle():
    return error_response_data, 500


@namespace.route("/service1")
@namespace.doc(...)
class Service1(Resource):
    def get(self):
        try:
            get_response = get_service()
            return get_response
        except:
            return default_error_handle()


@namespace.route("/service2")
@namespace.doc(namespace1_service2_request_data)
class Service2(Resource):
    @namespace.expect(namespace1_service2_request_data)
    @namespace.response(200, 'Success Response Received', namespace1_service2_response_data)
    def post(self):
        try:
            post_data = request.json
            title = post_data['Title']
            description = post_data['Description']
            return post_service(title, description)
        except:
            return default_error_handle()
