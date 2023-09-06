from flask import abort, render_template
from fiat.models import Fiatdata


def index():
    carros = Fiatdata.query.all()
    return render_template("index.html", carros=carros)


def carro(placa):
    carro = Fiatdata.query.filter_by(placa=placa).first() or abort(
        404, "Carro nao encontrado"
    )
    return render_template("carro.html", carro=carro)
