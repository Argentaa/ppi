import os
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
import mysql.connector

db = mysql.connector.connect(host='localhost',database='bd_progparcial',user='root',password='root')

app = Flask(__name__)
app.config['SECRET_KEY'] = '(ztu2h72t%u#t%1avh_a-i=%@7fdz19!_s1g1*(-nknq+b_op_'

serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cppd.iffar@gmail.com'
app.config['MAIL_PASSWORD'] = 'mqcpgfkwtdywveyb'

mail = Mail(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app) 
login_manager.login_message = u'Você precisa estar logado para acessar essa página'

from . import models

@login_manager.user_loader
def load_user(user_id):
    return models.docente_cookie(user_id)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .docente import docente as docente_blueprint
app.register_blueprint(docente_blueprint)

from .requerimentos import requerimentos as requerimentos_blueprint
app.register_blueprint(requerimentos_blueprint)

from .cppd import cppd as cppd_blueprint
app.register_blueprint(cppd_blueprint)
