from flask import Blueprint, render_template, redirect, request, flash, url_for

from entities import conversas, usuarios

bp = Blueprint('chat', __name__, url_prefix='/chat_v2', template_folder='templates')

@bp.get('/cvs/<id>')
def conversa(id):
    conversa = None
    usuario = None
    for cnv in conversas:
        if cnv['id'] == id:
            conversa = cnv
            for usu in usuarios:
                if usu['id'] == cnv['dest']:
                    usuario = usu

    return render_template('chat/conversa.html', conversa=conversa, usuario=usuario)


@bp.post('/falar/<id>')
def falar(id):
    for cnv in conversas:
        if cnv['id'] == id:
            mensagem = {
                'rem': request.form['nome'],
                'msg': request.form['mensagem'],
            }
            cnv['msgs'].append(mensagem)
    return redirect(url_for('chat.conversa', id=id))


@bp.get('/conversas/<id>')
def lista_conversas(id):
    conversas_com_usuario = []
    for conversa in conversas:
        if conversa['dest'] == id:
            conversas_com_usuario.append(conversa)
    usuario = None
    for usu in usuarios:
        if usu['id'] == id:
            usuario = usu

    return render_template('chat/listadeconversas.html', conversas=conversas_com_usuario, usuario=usuario)


@bp.post('/crianovodest')
def crianovousuario():
    novo_id = str(len(usuarios)+1)
    novo_nick = request.form['novo']

    usuarios.append({'id': novo_id, 'nick': novo_nick})

    flash(f'Usuário {novo_nick} criado com sucesso!')

    return redirect('/')


@bp.post('/crianovaconversa')
def crianovaconversa():
    novo_id = str(len(conversas)+1)
    dest = request.form['dest']
    rem = request.form['rem']
    fala = request.form['primeira']

    nova = {'id': novo_id, 'dest': dest, 'msgs': [{'rem': rem,
                                                   'msg': fala}, ]}
    conversas.append(nova)

    return redirect(url_for('chat.conversa', id=novo_id))
