from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import  login_required, current_user
from . import db

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

            cursor.execute("""SELECT descricao, pontos_string, pontos FROM criterios WHERE categoria_id=%s""", (*idCategoria,))
            criterios = cursor.fetchall()
           
            if parte not in criteriosdict:
                criteriosdict[parte] = {}
            criteriosdict[parte][categoria] = criterios

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
        pontosMult = request.form['PontosMult']

        cursor = db.cursor()
        cursor.execute("""SELECT id FROM categorias WHERE descricao=%s""", (categoria,))
        catid = cursor.fetchone()
        try:
            cursor.execute("""INSERT INTO criterios (categoria_id, descricao, pontos, pontos_string) 
                            VALUES (%s, %s, %s, %s)""", (catid[0], criterio, int(pontosMult), pontos))
            db.commit()
        except:
            flash('Somente é permetido números nos pontos de multiplicação!')
            return redirect(url_for('cppd.alterar_requerimentos'))

        return redirect(url_for('cppd.alterar_requerimentos'))
    
@cppd.route('/alterar_parte', methods=['GET','POST'])
@login_required

def alterar_parte():
    if request.method=='POST':
        cursor = db.cursor()
        parte_mudar = request.form['Parte']
        parte = request.form['id']

        cursor.execute("""UPDATE partes SET descricao=%s WHERE descricao=%s""", (parte_mudar, parte))
        db.commit()

        return redirect(url_for('cppd.alterar_requerimentos'))

@cppd.route('/alterar_categoria', methods=['GET','POST'])
@login_required

def alterar_categoria():
    if request.method=='POST':
        cursor = db.cursor()
        categoria_mudar = request.form['Categoria']
        categoria = request.form['id']

        cursor.execute("""UPDATE categorias SET descricao=%s WHERE descricao=%s""", (categoria_mudar, categoria))
        db.commit()

        return redirect(url_for('cppd.alterar_requerimentos'))
    
@cppd.route('/alterar_criterio', methods=['GET','POST'])
@login_required

def alterar_criterio():
    if request.method=='POST':
        cursor = db.cursor()
        criterio = request.form['id']
        pontos = request.form['Pontos']
        criterio_mudar = request.form['Criterio']
        pontosMult = request.form['PontosMult']

        cursor.execute("""UPDATE criterios SET descricao=%s, pontos=%s, pontos_string=%s WHERE descricao=%s""", (criterio_mudar,int(pontosMult),pontos,criterio))
        db.commit()

        return redirect(url_for('cppd.alterar_requerimentos'))

@cppd.route('/excluir_parte/<string:Parte>')
@login_required

def excluir_parte(Parte):

    cursor = db.cursor()

    cursor.execute("""SELECT id FROM partes WHERE descricao=%s""",(Parte,))
    idparte = cursor.fetchone()

    cursor.execute("""SELECT id FROM categorias WHERE parte_id=%s""",(*idparte,))
    idcat = cursor.fetchall()
    print(idcat)

    for cat in idcat:
        cursor.execute("""DELETE FROM criterios WHERE categoria_id=%s""",(*cat,))
        cursor.execute("""DELETE FROM categorias WHERE id=%s""",(*cat,))
    
    cursor.execute("""DELETE FROM partes WHERE descricao=%s""",(Parte,))

    db.commit()

    return redirect(url_for('cppd.alterar_requerimentos'))

@cppd.route('/excluir_categoria/<string:Categoria>')
@login_required

def excluir_categoria(Categoria):
    cursor = db.cursor()

    cursor.execute("""SELECT id FROM categorias WHERE descricao=%s""",(Categoria,))
    idcat = cursor.fetchone()

    cursor.execute("""DELETE FROM criterios WHERE categoria_id=%s""",(*idcat,))
    cursor.execute("""DELETE FROM categorias WHERE descricao=%s""",(Categoria,))

    db.commit()

    return redirect(url_for('cppd.alterar_requerimentos'))

@cppd.route('/excluir_criterio/<string:Criterio>')
@login_required

def excluir_criterio(Criterio):
    cursor = db.cursor()

    cursor.execute("""DELETE FROM criterios WHERE descricao=%s""",(Criterio,))

    db.commit()

    return redirect(url_for('cppd.alterar_requerimentos'))