class Televisão:
    def __init__(self, tamanho, canal):
        self.tamanho = tamanho
        self.canal = canal
        self.ligar = False

    def get_tamanho(self):
        return self.tamanho
    
    def get_canal(self):
        return self.canal

    def get_ligar(self):
        self.ligar = True
        return 'A tv está ligada!'
    
    def get_desligar(self):
        if self.desligar == True:
            print('Sua tv está liagada')
        else:
            print('Sua tv esta desligada')
    
    def set_tamanho(self, novo_tamanho):
         self.tamanho = novo_tamanho
    
    def set_canal(self, novo_canal):
        self.canal = novo_canal

    def get_ligar(self):
        self.ligar = True
        return 'A tv está ligada!'
    
    def get_desligar(self):
        self.desligar = True
        return 'A tv será desligada'

Televisão(3, 4)