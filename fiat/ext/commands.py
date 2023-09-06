import click
from fiat.ext.database import db
from fiat.ext.auth import create_user
from fiat.models import Fiatdata


def create_db():
    """Cria o banco de dados"""
    db.create_all()


def drop_db():
    """Limpa o banco de dados"""
    db.drop_all()


# def populate_db():
#     """Adiciona dados populando o banco para testes"""
#     data = [
#         Fiatdata(id=1, name="Ciabatta", price="10", description="Italian Bread"),
#         Fiatdata(id=2, name="Baguete", price="15", description="French Bread"),
#         Fiatdata(id=3, name="Pretzel", price="20", description="German Bread"),
#     ]
#     db.session.bulk_save_objects(data)
#     db.session.commit()
#     return Fiatdata.query.all()


def init_app(app):
    # for command in [create_db, drop_db, populate_db]:
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option("--username", "-u")
    @click.option("--password", "-p")
    def add_user(username, password):
        """Adiciona um novo usuario no banco de dados"""
        return create_user(username, password)
