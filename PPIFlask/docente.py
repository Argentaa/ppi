from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_required, current_user
from . import db

docente = Blueprint('docente', __name__, template_folder='templates\docente')

@docente.route('/home_docente')
@login_required
def home_docente():
    cppd = current_user.cppd

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM docente WHERE CPF=%s""", (current_user.cpf,))
    record = cursor.fetchone()
    
    if record[6] == 1:
        return redirect(url_for('cppd.cppd_home'))

    return render_template('home_docente.html', cppd=cppd)

@docente.route('/minha_conta')
@login_required
def minha_conta():

    nome = current_user.nome
    cpf = current_user.cpf
    siape = current_user.siape
    email = current_user.email
    senha = current_user.senha
    cppd = current_user.cppd

    return render_template('minha_conta.html', nome=nome, cpf=cpf, siape=siape, email=email, senha=senha, cppd=cppd)

@docente.route('/minha_conta', methods=["GET", "POST"])
@login_required
def minha_conta_post():
    
    cursor = db.cursor()

    if request.method == 'POST':
        CPF = request.form['CPF']
        SIAPE = request.form['SIAPE']
        Nome = request.form['Nome']
        Email = request.form['Email']

        cursor.execute("""UPDATE docente SET CPF=%s, SIAPE=%s, Nome=%s, Email=%s WHERE id=%s""", (CPF, SIAPE, Nome, Email, current_user.id))
        db.commit()
        return redirect(url_for('docente.minha_conta'))

@docente.route('/ajuda_docente')
@login_required
def ajuda_docente():
    cppd = current_user.cppd
    nome = current_user.nome

    return render_template('ajuda_docente.html', nome=nome, cppd=cppd)

@docente.route('/meus_requerimentos')
@login_required
def meus_requerimentos():
    cppd = current_user.cppd

    return render_template('meus_requerimentos.html',cppd=cppd)
