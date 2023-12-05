preco = float(input('Digite o preço:'))

desconto01 = 0.5
desconto02 = 0.2

if preco >= 100:
    preco_com_descoonto = preco * desconto01
    print(preco_com_descoonto)
else:
    preco_com_descoonto = preco * desconto02
    print(preco_com_descoonto)