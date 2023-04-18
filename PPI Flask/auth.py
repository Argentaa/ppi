from flask import render_template, request, redirect, url_for, Blueprint, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User

auth = Blueprint('auth', __name__, template_folder='templates\home')

@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('docente.home_docente'))
    else:
        return render_template("login.html")

@auth.route('/login', methods=["GET", "POST"])
def login_post():
    cursor = db.cursor()

    if request.method=='POST':
        CPF = request.form['CPF']
        Senha = request.form['Senha']
        lembrar = True if request.form.get('lembrarSenha') else False

        cursor.execute("""SELECT * FROM docente WHERE CPF=%s""", (CPF,))
        record = cursor.fetchone()
        
        if record and check_password_hash(record[5], Senha):
            login_user(User(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
            
            if record[6] == 1:
                return redirect(url_for('cppd.cppd_home'))

            return redirect(url_for('docente.home_docente'))
        
        else:
            flash('Dados Incorretos, Verifique seus dados.')
            return redirect(url_for('auth.login'))

    return render_template("login.html")

@auth.route('/registrar')
def registrar():
    if current_user.is_authenticated:
        return redirect(url_for('docente.home_docente'))
    else:
        return render_template("registrar.html")

@auth.route('/registrar', methods=["GET", "POST"])
def registrar_post():
    cursor = db.cursor()
    if request.method == 'POST':
        CPF = request.form['CPF']
        SIAPE = request.form['SIAPE']
        Nome = request.form['Nome']
        Email = request.form['Email']
        Senha = request.form['Senha']
        CPPD = 0

    cursor.execute("""SELECT * FROM docente WHERE CPF=%s""", (CPF,))
    info = cursor.fetchone()

    if info is None:
        cursor.execute("""INSERT INTO docente (CPF, SIAPE, Nome, Email, Senha, CPPD) VALUES (%s,%s,%s,%s,%s,%s)""", 
                        (CPF,SIAPE,Nome,Email,generate_password_hash(Senha, method='sha256'),CPPD))
        db.commit()
        return redirect(url_for('auth.login'))
    else:
        flash('CPF ja cadastrado!')
        return redirect(url_for('auth.registrar'))
        
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.principal'))