from flask import request
from flask_restplus import Namespace, Resource, fields

from blueprints.blueprint1.namespace1.services.get_service import get_service
from blueprints.blueprint1.namespace1.services.post_service import post_service

namespace = Namespace('namespace1', description='namespace1 related stuff')

namespace1_service2_request_data = namespace.model("namespace1_service2_request_data", {
    "Title": fields.String(description="Title", required=True, example='John Smith', type=str),
    "Description": fields.String(description="Description", required=True, example='Its working.', type=str)
})


# @namespace.errorhandler
# def namespace_error_handler(error):
#     return {'message': str(error)}, 500


@namespace.route("/service1")
@namespace.doc(...)
class Service1(Resource):
    def get(self):
        try:
            get_response = get_service()
            return get_response
        except:
            return Exception


@namespace.route("/service2")
@namespace.doc(...)
class Service2(Resource):
    @namespace.expect(namespace1_service2_request_data)
    def post(self):
        try:
            post_data = request.json
            title = post_data['Title']
            description = post_data['Description']
            return post_service(title, description)
        except:
            return Exception
