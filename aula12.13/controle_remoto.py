class ControleRemoto:
    def __init__(self,cor, marca, qtd_pilhas):
         self.cor = cor
         self.marca = marca
         self.qtd_pilhas = qtd_pilhas
         self.painel = False
         self.temperatura = 0
#metodos


    def get_temperatura(self):
         return self.temperatura
    
    def precionar_botao(self, tipo_de_botao):
         self.botao = tipo_de_botao
         if self.botao == 'Ligar' and self.temperatura == 0:
              print('Ar ligado')
              self.ligar
         elif self.botao == 'desligar':
              print('Ar ligado')
              self.set_temperatura(0)
              self.desligar()

controle =  ControleRemoto('Branca', 'elgin', 2)
controle.precionar_botao('Ligar')
controle.set_temperatura(20)
print(controle.get)
    

















    

#metodos
ligar e desligar

