class Cafeteira:
    ligada = False
    cefe_pronto = False
    compartimento_filtro = False
    compartimento_agua = False
    def ligar(self):
        self.ligar = True
        print('está ligada')

    def desligar(self):
        self.ligada = False
        print('esta desligada')

    def verificar_agua(self):
        if self.ligada == True:
            if self.compartimento_agua == False:
                print('Favor colocar água no compartimento')
            else:
                self.compartimento_filtro = True

    def colocar_agua(self):
        self.verificar_agua()
