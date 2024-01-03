class Filme:
    def __init__(self, nome, ano , duração):
        self.nome = nome
        self.ano = ano
        self.duração = duração

class Séries:
    def __init__(self, nome, ano , temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

caatinga = Séries('Caatinga é do nordeste',1020, 140)
print(caatinga.nome)


vingadores = Filme('Vinga1', 2013, 123)
print(vingadores.ano)