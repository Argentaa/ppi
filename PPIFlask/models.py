from . import db
from flask_login import UserMixin, AnonymousUserMixin
cursor = db.cursor()


class User(UserMixin):
    def __init__(self, id, cpf, siape, nome, email, senha, cppd):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.siape = siape
        self.email = email
        self.senha = senha
        self.cppd = cppd
    
    def get_id(self):
        return self.id
    
    def is_authenticated(self):
        return True

def docente_cookie(id):
    cursor.execute("""SELECT * FROM docente WHERE id=%s""", (id,))
    record = cursor.fetchone()
    return User(record[0], record[1], record[2], record[3], record[4], record[5], record[6])

    
