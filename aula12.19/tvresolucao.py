class Televisão:
    def __init__(self, tamanho):
        pass
        self.tamanho = tamanho
        self.canal = 0
        self.ligada = False

    def get_tamanho(self):
        return self.tamanho

    def get_canal(self):
        return self.canal
#sets
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def set_canal(self, novo_canal):
        if novo_canal < 0 or novo_canal > 999:
            if self.ligada == True and:
                self.canal = novo_canal
            print('Canal inesxistente')
        else:
            if self.ligada == True:
                self.canal = novo_canal
            else:
                print('Ligue sua tv para mudar de canal')

            self.canal = novo_canal
#proprios
    def ligar(self):
        self.ligada = True
        print('Sua tv está ligada')

    def desligar(self):
        self.ligada = False
        print('sua tv esta desligada')

#chamadas de criacao

minha_tv = Televisão(32)
minha_tv.ligar()

minha_tv.set_canal()
print(minha_tv.get_canal())