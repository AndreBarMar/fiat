from flask import Blueprint
from flask_restful import Api

from .resources import (
    CarrosResource,
    CarroItemResource,
    CarrosItemResource,
)

bp = Blueprint("restapi", __name__, url_prefix="/api/v2")
api = Api(bp)


def init_app(app):
    api.add_resource(CarrosResource, "/carros/")
    api.add_resource(CarroItemResource, "/carro/<placa>")
    api.add_resource(CarrosItemResource, "/carros/<nome>")
    app.register_blueprint(bp)
