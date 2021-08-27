from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def raiz():
    return render_template('index.html')


@app.get('/outra')
def outra():
    return 'outra coisa'


@app.post('/digaola')
def diga():
    nome = request.form['nome']
    senha = request.form['senha']
    return f'Olá, {nome}! Sua senha é {senha}.'


@app.route('/pesquisa')
def pesquisar():
    res = ''
    for k, v in request.headers.items():
        res = res + f'{k} : {v}<br>'
    return res


@app.get('/pagina1')
def basica():
    return render_template('pagina1.html', titulo=request.args['titulo'], nome=request.args['nome'], mostrar=True)


@app.get('/filha1')
def filha1():
    return render_template('filha1.html', variavel='teste')

@app.get('/filha2')
def filha2():
    return render_template('filha2.html', variavel='teste')