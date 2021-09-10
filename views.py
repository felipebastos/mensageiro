from flask import render_template
from entities import Usuario
 
def raiz():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)