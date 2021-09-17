from datetime import datetime

from flask_login import UserMixin
from app import db, login_manager


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    passwd = db.Column(db.String(80), nullable=False)

    cadastro_em = db.Column(db.DateTime, default=datetime.now)


@login_manager.user_loader
def loadUsuario(id):
    return Usuario.query.get(id)
