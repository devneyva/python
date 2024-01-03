print('Bom dia! Informe seus dados para realizar seu cadrastro')
class Cadrastro:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class comprimentar(Cadrastro):
        def __init__(self, nome, idade, cpf):
            super().__init__(nome, idade, cpf)
            print(f'Olá {self.nome}! Sua idade é {self.idade}. Seu cpf é {self.cpf}')

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
cpf = int(input('Digite seu  cpf: '))
#('Neyva', 9,2)
c = comprimentar(nome, idade,cpf)
print(c)
print(f'O seu cadrastro {nome} foi concluído!')


#get set no nome e cpf e tudo que pode mudar com o tempo
#estanciar criar e relacionar alguma classe