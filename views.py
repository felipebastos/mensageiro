from flask import render_template
from entities import usuarios
 
def raiz():
    return render_template('index.html', usuarios=usuarios)