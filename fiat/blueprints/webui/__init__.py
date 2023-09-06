from flask import Blueprint

from .views import index, carro

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index, endpoint="index")
bp.add_url_rule("/carro/<placa>", view_func=carro, endpoint="carroview")


def init_app(app):
    app.register_blueprint(bp)
