class Estudante:
    nome = 'Paulo'
    matricula = 353637

class EstudanteGraduacao(Estudante): #todos estudante de graduacao é um estudanete  #pacal case
    curso = 'Ads'

class EstudantePos(Estudante): #conexao ente a subclasse com a classe
    nivel = 1
    orientador = 'Professor Carlos'

aluno =  EstudanteGraduacao()
#print(f'Olá, {aluno.nome} seu curso de Graduaçaõ é o de {aluno.curso}  e sua matrícula de acesso é {aluno.matricula}')
#print(aluno.curso)

class Pessoa:
    def __init__(self):
        pass
    nome = "ana"
    print(f'Nome: {nome}')

class Empregado(Pessoa):
    cargo = 'Engenheiro'
    salario = 5000

class Estudante(Pessoa):
    matricula = 1232
    def __str__(self):
        return f'O estudante {self.nome} o número da sua matrícula é {self.matricula}'

class Estudante_graduacao(Estudante):
    curso = 'Gastronomia'
    print(f'O seu curso é {curso}')

class EstudantePos:
    orientador = 'Paulo'
    nivel = 2
    print(f'O seu orientador é {orientador}. seu nível é {nivel}')