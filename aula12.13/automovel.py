class Automovel():
    def __init__(self, placa,cor):
        self.placa = placa
        self.cor = cor

    def get_placa(self):
        return self.cor
    
    def get_cor(self, nova_cor):
        self.cor = nova_cor
    
    def dirigir(self, velocidade):
        print(f'estou dirigindo a {velocidade} km/h')
#instancias
carro = Automovel('TYT-0033', 'Azul')
moto = Automovel('YTX-1233', 'rosa')
caminhao = Automovel('IUD-3833', 'Verde')
#cahamas get

print(carro.get_cor())
print(moto.get_cor())

#chamadas set (mudanças)