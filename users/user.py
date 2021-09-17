from flask import Blueprint, jsonify
from flask_login import login_required, current_user

from auth.entitities import Usuario

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.get('/')
@login_required
def perfil():
    return jsonify({"id": current_user.id, "username": current_user.username, "cadastro_em": current_user.cadastro_em})
