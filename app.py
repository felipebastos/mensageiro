import os
from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

usuarios = [
    {'id': '1', 'nick': 'cumbuca'},
    {'id': '2', 'nick': 'potinho'},
]

conversas = [
    {'id': '1', 'dest': '1', 'msgs': [
        {'rem': 'Visitante 1', 'msg': 'Tou com fome.'}, ]},
    {'id': '2', 'dest': '2', 'msgs': [{'rem': 'Visitante 2',
                                       'msg': 'Te vira, plebeu.'}, ]},
]


@app.get('/')
def raiz():
    return render_template('index.html', usuarios=usuarios)


@app.get('/conversa/<id>')
def conversa(id):
    conversa = None
    usuario = None
    for cnv in conversas:
        if cnv['id'] == id:
            conversa = cnv
            for usu in usuarios:
                if usu['id'] == cnv['dest']:
                    usuario = usu

    return render_template('conversa.html', conversa=conversa, usuario=usuario)


@app.post('/falar/<id>')
def falar(id):
    for cnv in conversas:
        if cnv['id'] == id:
            mensagem = {
                'rem': request.form['nome'],
                'msg': request.form['mensagem'],
            }
            cnv['msgs'].append(mensagem)
    return redirect(f'/conversa/{id}')


@app.get('/conversas/<id>')
def lista_conversas(id):
    conversas_com_usuario = []
    for conversa in conversas:
        if conversa['dest'] == id:
            conversas_com_usuario.append(conversa)
    usuario = None
    for usu in usuarios:
        if usu['id'] == id:
            usuario = usu

    return render_template('listadeconversas.html', conversas=conversas_com_usuario, usuario=usuario)


@app.post('/crianovodest')
def crianovousuario():
    novo_id = str(len(usuarios)+1)
    novo_nick = request.form['novo']

    usuarios.append({'id': novo_id, 'nick': novo_nick})

    flash(f'Usuário {novo_nick} criado com sucesso!')

    return redirect('/')


@app.post('/crianovaconversa')
def crianovaconversa():
    novo_id = str(len(conversas)+1)
    dest = request.form['dest']
    rem = request.form['rem']
    fala = request.form['primeira']

    nova = {'id': novo_id, 'dest': dest, 'msgs': [{'rem': rem,
                                                   'msg': fala}, ]}
    conversas.append(nova)

    return redirect(f'/conversa/{novo_id}')
