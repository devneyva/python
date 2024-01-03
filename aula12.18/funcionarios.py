class Funcionarios:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

class Administrativo(Funcionarios):
        def __str__(self,):
              return f'O/A {self.nome} trabalha no adriministrativo e recebe o salário é de {self.salario} e tem {self.idade} anos de idade'

class ServicosGerais(Funcionarios):
        def __str__(self) :
              return f'O/A {self.nome} trabalha em servicos gerais e recebe o salário é de {self.salario} e tem {self.idade} anos de idade'

class Professores(Funcionarios):
        def __str__(self):
              return f'O/A {self.nome} é professor(a) e recebe o salário é de {self.salario} e tem {self.idade} anos de idade'

ju = ServicosGerais('Juliana', 23, 1400)
print(ju)
jonas = Administrativo('Jonas', 22, 1500)
print(jonas)
joao = Professores('Joao', 43, 3000)
print(joao)
