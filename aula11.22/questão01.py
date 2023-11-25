
contador_par = 0
contador_impar = 0

for i in range(1, 10):
    numero = int(input(f'Informe {i} numero:'))
    if numero  % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print(f'A quantidades de números pares é {contador_par}')
print(f'A quantidade de números impares é {contador_impar}')