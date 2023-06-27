from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User

requerimentos = Blueprint('requerimentos', __name__, template_folder='templates\\requerimentos')
pagina = 'base_docente.html'

@requerimentos.route('/requerimento')
@login_required

def requerimento():
    criteriosdict = {}

    cursor = db.cursor()
    cursor.execute("""SELECT descricao FROM partes""")
    dados_p = cursor.fetchall()
    partes = [item for t in dados_p for item in t]

    for parte in partes:
        cursor.execute("""SELECT id FROM partes WHERE descricao=%s""", (parte,))
        idPartelist = cursor.fetchall()
        idParte, *x = idPartelist

        cursor.execute("""SELECT descricao FROM categorias WHERE parte_id=%s""", (*idParte,))

        categoriastuple = cursor.fetchall()
        categoriaslist = [item for t in categoriastuple for item in t]

        for categoria in categoriaslist:
            cursor.execute("""SELECT id FROM categorias WHERE descricao=%s""", (categoria,))
            idCategorialist = cursor.fetchall()
            idCategoria, *x = idCategorialist

            cursor.execute("""SELECT descricao, pontos_string, pontos FROM criterios WHERE categoria_id=%s""", (*idCategoria,))
            criterios = cursor.fetchall()
           
            if parte not in criteriosdict:
                criteriosdict[parte] = {}
            criteriosdict[parte][categoria] = criterios

    return render_template('requerimento.html', criteriosdict=criteriosdict, cppd = current_user.cppd)

@requerimentos.route('/requerimento', methods=["GET", "POST"])
@login_required

def requerimento_post():
    if request.method == 'POST':
        for key, val in request.form.items():
            if key.startswith("criterio"):
                print(key, val)
    
    return redirect(url_for('docente.meus_requerimentos'))