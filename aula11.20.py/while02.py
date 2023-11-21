#peça idade de 20 alunos. avise quando for aluno que tem maior de que 13 anos

aluno = 1

while aluno <= 20:
    idade = int(input(f'Digite a idade do {aluno} '))
    if idade > 13:
        print(f'O {aluno} tem {idade} . Sendo assim tem mais de 13 anos')
    aluno = aluno + 1

print('Fim da questão 02')