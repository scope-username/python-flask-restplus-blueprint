from flask_restplus import Namespace, Resource

from blueprints.blueprint2.namespace2.services.get_service import get_service
from blueprints.blueprint2.namespace2.services.post_service import post_service

namespace = Namespace('namespace2', description='namespace1 related stuff')


@namespace.route("/service1")
@namespace.doc(...)
class Service1(Resource):
    def get(self):
        return get_service()


@namespace.route("/service2")
@namespace.doc(...)
class Service2(Resource):
    def post(self):
        return post_service()
