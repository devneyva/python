salario = int(input('Digite seu salário: '))
variavel_controle = 'IR será cobrado' if salario >= 2500 else 'IR não será cobrado'
print(variavel_controle)

vr_controle = 'Ok 1' if True else 'Ok 2'

if True:
    print('Ok 1')
elif True:
    print('Ok 2')
else:
    print('Fim')