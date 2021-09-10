from sqlalchemy.orm import backref
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(20), unique=True, nullable=False)

    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'))

    conversas = db.relationship('Conversa', backref='usuario', lazy=True)

#usuarios = [
#    {'id': '1', 'nick': 'cumbuca'},
#    {'id': '2', 'nick': 'potinho'},
#]

class Conversa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dest = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    mensagens = db.relationship('Mensagem', backref='conversa', lazy=True)

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rem = db.Column(db.String(20), default="anômimo")
    msg = db.Column(db.String(144), nullable=False)

    conversa_id = db.Column(db.Integer, db.ForeignKey('conversa.id'), nullable=False)


#conversas = [
#    {'id': '1', 'dest': '1', 'msgs': [
#        {'rem': 'Visitante 1', 'msg': 'Tou com fome.'}, ]},
#    {'id': '2', 'dest': '2', 'msgs': [{'rem': 'Visitante 2',
#                                       'msg': 'Te vira, plebeu.'}, ]},
#]

class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False, unique=True)