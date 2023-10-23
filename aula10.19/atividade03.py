salario_atual = float(input("Digite seu salário atual:"))
reajuste_porcentagem = float(input("Digite a porcemtagem do reajuste:"))

valor_porcentagem = ((salario_atual * reajuste_porcentagem)) / 100

print(valor_porcentagem + salario_atual)