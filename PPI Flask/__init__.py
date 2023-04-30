from flask import Flask
from flask_login import LoginManager
import mysql.connector

db = mysql.connector.connect(host='localhost',database='bd_progparcial',user='root',password='root')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '(ztu2h72t%u#t%1avh_a-i=%@7fdz19!_s1g1*(-nknq+b_op_'

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

    return app
