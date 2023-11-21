#faça um código que peça uma nota se for menor do que zero ou maior de 10 saia do while 

contador = 0 
while contador <=10: 
    nota = float(input("Digite uma nota")) #mensagem imprimida
    if nota < 0 or nota > 10: #condição
        print('Sua nota não foi suficiente para continuar') #mensagem caso a condição seja falsa
        break #sai do loop
    contador = contador +1 #

