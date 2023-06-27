
'''pontosdictr = {'Parte 1: Atividade Docente': {'1 - Número de Horas Aula': [('Numero Periodos Aula', '02 pontos'), ('Número médio de disciplina semestrais', '01 pontos'), ('Número médio de turmas semestrais', '3 Pontos'), ('Semestres', '5 Pontos')], 
                                             '2 - Numeros semestresdsadasd': [('Curso de ate 20hfdsfdsf', '01 pontos'), ('Curso de afdsfsddsate 40h', '03 pontos'), ('Curso acidasdasdama de 40 horas', '01 pontos')]}, 
            'Parte 2: Treinamento Regulares': {'2 - Cursos de Capacitação': [('Curso de ate 20h', '01 pontos'), ('Curso de ate 40h', '03 pontos'), ('Curso acima de 40 horas', '01 pontos')]}}

partes = ['Parte 1: Atividade Docente', 'Parte 2: Treinamento Regulares','Parte 1: Atividade Docente']
categorias = ['1 - Número de Horas Aula', '2 - Cursos de Capacitação','2 - Numeros semestresdsadasd' ]
criterios_pontos = [[('Numero Periodos Aula', '02 pontos',2), ('Número médio de disciplina semestrais', '01 pontos',1), 
                     ('Número médio de turmas semestrais', '3 Pontos',3), ('Semestres', '5 Pontos',5)], 
                     [('Curso de ate 20h', '01 pontos',1), ('Curso de ate 40h', '03 pontos',3), ('Curso acima de 40 horas', '01 pontos',1)],
                     [('Curso de ate 20hfdsfdsf', '01 pontos',1), ('Curso de afdsfsddsate 40h', '03 pontos',3), ('Curso acidasdasdama de 40 horas', '01 pontos',1)]]

pontosdict = {}

p1 = ['1ponto', '2ponto', '3ponto']
p2 = ['ques1', 'quest2', 'quest3']



for i, parte in enumerate(partes):
    categoria = categorias[i]
    criterios = criterios_pontos[i]
    if parte not in pontosdict:
        pontosdict[parte] = {}
    pontosdict[parte][categoria] = criterios


for i,l in pontosdict.items():
    print('\nparte', i)
    for j, k in l.items():
        print('\ncategoria', j)
        for a in k:
            for p in a:
                print(p)'''

TokenDocente = ('324fgd2fdsfsdg343dsfsd2524363tetesd26426gdsgdfgdsg')
TokenDocente1 = ('')

if TokenDocente1:
    print('not none')
else:
    print('none')