class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade} e Cpf {self.cpf}'
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina,cpf ):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina
        self.__cpf = cpf
    
class Aluno(Pessoa):
    pass

paulo = Professor('Paulo Junior', 29, 1400, 'Back end', 12345644)
print(paulo.get_cpf)