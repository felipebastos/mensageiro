from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user
from app import db, bcrypt

from auth.entitities import Usuario

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.post('/')
def registra_usuario():
    data = request.get_json()

    novo = Usuario()
    novo.username = data['username']
    novo.passwd = bcrypt.generate_password_hash(data['password'])

    db.session.add(novo)
    db.session.commit()

    return jsonify({'status': 'success'})
    
@bp.get('/login')
def user_login():
    data = request.get_json()

    usuario = Usuario.query.filter_by(username=data['username']).first()

    res = {}
    if usuario:
        if bcrypt.check_password_hash(usuario.passwd, data['password']):
            login_user(usuario)
            res["status"] = 'Success'
        else:
            res["status"] = 'Password mismatch'
    else:
        res["status"] = 'User name mismatch'

    return jsonify(res)


@bp.get('/logout')
def sair():
    logout_user()
    return jsonify({'status': 'disconnected'})