from random import randint

jogador = input('Escolhar par ou impar:').lower()
numero_jogador = int(input('Escolha seu número:'))
numero_computador = randint(0, 11)
resultado = numero_computador + jogador
if resultado % 2 ==0:
    if jogador == 'Par':
        print('Voce ganhou!')
    else:
        print('O computador ganhou!')
else:
    if jogador== 'Impar':
        print('Voce ganhou!')
    else:
        print('O computador ganhou!')


