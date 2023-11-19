
contagem = 20

while contagem <= 20:
    idade = int(input("Digite sua idade"))
    print(idade)
    if idade > 13:
        print("Voce tem mais de 13 anos")

#################################################

contador = 0
while contador < 3:
    idade = int(input("Informe sua idade:"))
    if idade > 13:
        print(f'O aluno {contador} é maior de 13 anos')
    contador +=1