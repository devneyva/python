class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.comida = 100

    def get_nome(self):
        return self.nome
    
    def get_peso(self):
        return self.peso
    
    def get_fome(self):
        return self.fome
    
#Os SETS

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_fome(self, novo_fome):
        self.fome += novo_fome
        while novo_fome >= 99:
            print(f'Alimente o/a {self.nome}')
            nova_comida = int(input('Quanto de comida voce quer dar para seu pet'))
            self.comida -= nova_comida
            self.fome -= nova_comida

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def imprimir(self):
        print(f'Olá me chamo {self.nome}')
        print(f'Estou pesando {self.peso} kg')
        print(f'Minha fome está em  {self.fome}')

caozinho = Pet('Marie', 15)
caozinho.imprimir()
caozinho.set_fome(50)
caozinho.imprimir()
caozinho.set_fome(90)
caozinho.imprimir()
caozinho.set_fome(70)
caozinho.imprimir()