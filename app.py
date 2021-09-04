import os
from flask import Flask, render_template

from dotenv import load_dotenv

from sobre import sobre
from chat import chat
import views

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ['SECRET_KEY']

    app.register_blueprint(sobre.bp)
    app.register_blueprint(chat.bp)

    app.add_url_rule('/', view_func=views.raiz)

    return app