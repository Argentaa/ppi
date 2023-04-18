from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User

cppd = Blueprint('cppd', __name__, template_folder='templates\\cppd')

@cppd.route('/cppd')
@login_required

def cppd_home():
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM docente WHERE CPF=%s""", (current_user.cpf,))
    record = cursor.fetchone()
    
    if record[6] == 0:
        return redirect(url_for('docente.home_docente'))

    return render_template('home_cppd.html')

@cppd.route('/corrigir_requerimentos')
@login_required

def corrigir_requerimentos():
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM docente WHERE CPF=%s""", (current_user.cpf,))
    record = cursor.fetchone()
    
    if record[6] == 0:
        return redirect(url_for('main.principal'))

    return render_template('corrigir_requerimentos.html')

@cppd.route('/alterar_criterios')
@login_required

def alterar_requerimentos():
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM docente WHERE CPF=%s""", (current_user.cpf,))
    record = cursor.fetchone()
    
    if record[6] == 0:
        return redirect(url_for('main.principal'))
    
    perguntas = (['Aulas', 'Semestres', 'Periodos'], ['Aulas12', 'Semestres22', 'Periodos32'])
    pontos = (['1 pontos por cada aula', '1 pontos por cada semestre', '1 pontos por cada periodo'], ['1 pontos por cada aula22', '1 pontos por cada semestre22', '1 pontos por cada periodo22'])

    criterios = zip(perguntas, pontos)


    return render_template('alterar_requerimentos.html', criterios=criterios)
