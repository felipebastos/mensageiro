from flask import Blueprint, render_template

bp = Blueprint('sobre', __name__, url_prefix='/sobre', template_folder='templates')

@bp.get('/')
def raiz():
    return render_template('sobre/index.html')
