from flask import abort, jsonify
from flask_restful import Resource

from fiat.models import Fiatdata


class CarrosResource(Resource):
    def get(self):
        carros = Fiatdata.query.all() or abort(204)
        return jsonify({"carros": [carro.to_dict() for carro in carros]})


class CarroItemResource(Resource):
    def get(self, placa):
        carro = Fiatdata.query.filter_by(placa=placa).first() or abort(404)
        print(carro)
        return jsonify(carro.to_dict())


class CarrosItemResource(Resource):
    def get(self, nome):
        carros = Fiatdata.query.filter_by(nome=str(nome).title()).all() or abort(404)
        Carros_dict = {
            "carros": [carro.to_dict() for carro in carros],
            "total": len(carros),
        }
        return jsonify(Carros_dict)
