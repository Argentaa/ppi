from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User

cppd = Blueprint('cppd', __name__, template_folder='templates\\cppd')

@cppd.route('/cppd')
@login_required

def cppd_home():
    
    if current_user.cppd == 0:
        return redirect(url_for('docente.home_docente'))

    return render_template('home_cppd.html')

@cppd.route('/corrigir_requerimentos')
@login_required

def corrigir_requerimentos():
    
    if current_user.cppd == 0:
        return redirect(url_for('main.principal'))

    return render_template('corrigir_requerimentos.html')

@cppd.route('/alterar_requerimentos')
@login_required

def alterar_requerimentos():

    if current_user.cppd == 0:
        return redirect(url_for('main.principal'))
    
    criteriosdict = {}

    cursor = db.cursor()
    cursor.execute("""SELECT descricao FROM partes""")
    dados_p = cursor.fetchall()
    partes = [item for t in dados_p for item in t]

    cursor.execute("""SELECT descricao FROM categorias""")
    dados_p = cursor.fetchall()
    categoriasalt = [item for t in dados_p for item in t]


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

            cursor.execute("""SELECT descricao, pontos_string FROM criterios WHERE categoria_id=%s""", (*idCategoria,))
            criterios = cursor.fetchall()
           
            if parte not in criteriosdict:
                criteriosdict[parte] = {}
            criteriosdict[parte][categoria] = criterios
            
    print(criteriosdict)
            



    return render_template('alterar_requerimentos.html', partesalt=partes, categoriasalt= categoriasalt, criteriosdict=criteriosdict)

@cppd.route('/adicionar_parte', methods=["GET", "POST"])
@login_required

def adicionar_parte():
    if request.method=='POST':
        parte = request.form['Parte']

        cursor = db.cursor()
        cursor.execute("""INSERT INTO partes (descricao) VALUES (%s)""", (parte,))
        db.commit()

        return redirect(url_for('cppd.alterar_requerimentos'))

@cppd.route('/adicionar_categoria', methods=["GET", "POST"])
@login_required

def adicionar_categoria():
    if request.method=='POST':
        categoria = request.form['Categoria']
        parte = request.form['Parte']

        cursor = db.cursor()
        cursor.execute("""SELECT id FROM partes WHERE descricao=%s""", (parte,))
        parteid = cursor.fetchone()

        cursor.execute("""INSERT INTO categorias (parte_id, descricao) VALUES (%s, %s)""", (parteid[0], categoria))
        db.commit()

        return redirect(url_for('cppd.alterar_requerimentos'))
    
@cppd.route('/adicionar_criterio', methods=["GET", "POST"])
@login_required

def adicionar_criterio():
    if request.method=='POST':
        pontos = request.form['Pontos']
        criterio = request.form['Criterio']
        categoria = request.form['Categoria']

        cursor = db.cursor()
        cursor.execute("""SELECT id FROM categorias WHERE descricao=%s""", (categoria,))
        catid = cursor.fetchone()

        cursor.execute("""INSERT INTO criterios (categoria_id, descricao, pontos, pontos_string) 
                        VALUES (%s, %s, %s, %s)""", (catid[0], criterio, int(pontos[0:2]), pontos ))
        db.commit()

        return redirect(url_for('cppd.alterar_requerimentos'))