from flask import render_template, Blueprint, url_for, redirect
from flask_login import current_user

main = Blueprint('main', __name__, template_folder='templates\home')

@main.route('/')
def principal():
    if current_user.is_authenticated:
        return redirect(url_for('docente.home_docente'))
    else:
        return render_template("home.html")

@main.route('/ajuda')
def ajuda():
    return render_template("ajuda.html")
