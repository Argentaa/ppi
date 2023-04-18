perguntas = (['Aulas', 'Semestres', 'Periodos'], ['Aulas12', 'Semestres22', 'Periodos32','Periodos33'])
pontos = (['1 pontos por cada aula', '1 pontos por cada semestre', '1 pontos por cada periodo'], ['1 pontos por cada aula22', '1 pontos por cada semestre22', '1 pontos por cada periodo22','1 pontos por cada periodo22s'])

for i in range(0,len(perguntas)):
    print('\nfor perguntas\n')
    for l in range(0,len(perguntas[i])):
        print(perguntas[i][l])
        print(pontos[i][l])