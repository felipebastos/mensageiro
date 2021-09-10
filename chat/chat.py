from flask import Blueprint, render_template, redirect, request, flash, url_for

from app import db
from entities import Conversa, Usuario, Mensagem

bp = Blueprint('chat', __name__, url_prefix='/chat_v2', template_folder='templates')

@bp.get('/cvs/<id>')
def conversa(id):
    conversa = Conversa.query.get(id)

    return render_template('chat/conversa.html', conversa=conversa, usuario=conversa.usuario)


@bp.post('/falar/<id>')
def falar(id):
    conversa = Conversa.query.get(id)

    mensagem_nova = Mensagem()
    mensagem_nova.rem = request.form['nome']
    mensagem_nova.msg = request.form['mensagem']

    mensagem_nova.conversa_id = conversa.id

    db.session.add(mensagem_nova)
    db.session.commit()
    
    return redirect(url_for('chat.conversa', id=id))


@bp.get('/conversas/<id>')
def lista_conversas(id):
    usuario = Usuario.query.get(id)

    return render_template('chat/listadeconversas.html', conversas=usuario.conversas, usuario=usuario)


@bp.post('/crianovodest')
def crianovousuario():
    novo_nick = request.form['novo']

    novo = Usuario()
    novo.nick = novo_nick

    db.session.add(novo)
    db.session.commit()

    flash(f'Usuário {novo_nick} criado com sucesso!')

    return redirect('/')


@bp.post('/crianovaconversa')
def crianovaconversa():
    dest = request.form['dest']
    rem = request.form['rem']
    fala = request.form['primeira']

    usuario = Usuario.query.get(dest)

    cvs_nova = Conversa()
    cvs_nova.dest = usuario.id

    msg_nova = Mensagem()
    msg_nova.rem = rem
    msg_nova.msg = fala

    cvs_nova.mensagens.append(msg_nova)

    db.session.add(cvs_nova)
    db.session.commit()

    return redirect(url_for('chat.conversa', id=cvs_nova.id))
