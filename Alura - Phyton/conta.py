class Conta:
    def __init__(self):
        pass
    def cria_conta(numero, titular, saldo, limite):
        conta = {"numero" : numero ,"titular": titular,"saldo" : saldo, "limite" : limite }
        return conta
        
    def deposita(conta, valor):
        conta['conta'] += valor

    def saca(conta,valor):
        conta['conta'] -= valor



    