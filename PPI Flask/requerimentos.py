from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User

requerimentos = Blueprint('requerimentos', __name__, template_folder='templates\\requerimentos')
pagina = 'base_docente.html'

@requerimentos.route('/requerimento')
@login_required

def requerimento():
    cppd = current_user.cppd

    perguntas = ['Aulas', 'Semestres', 'Periodos']
    pontos = ['1 pontos por cada aula', '1 pontos por cada semestre', '1 pontos por cada periodo']

    return render_template('requerimento.html', cppd=cppd, perguntas=perguntas, pontos=pontos)
