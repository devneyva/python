jogador1 = int(input('Escolha par ou impar:')).lower()
if jogador1 == 'par':
    jogador1 == 'Impar'
else:
    jogador2 = 'Par'
    
numero_jogador1 = int(input('Escolha um número:'))
numero_jogador2 = int(input('Escolha um número:'))

resultado = numero_jogador1 + numero_jogador2
if resultado % 2 ==0:
    if jogador1 == 'par':
        print('Jogador1. You Winn')
else:
    print('Jogador1. You loser')
