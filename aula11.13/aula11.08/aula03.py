# operadores IN e NOT IN

nome = "paulo"
print("au" in nome)


print("=" * 20)
seu_nome = input("Informe seu nome:")
buscar = input("Informe o valor a ser encontrado:")

if buscar in nome:
    print(f"{buscar} está contido em {seu_nome}")
else:
    print(f"{buscar} está contido em {seu_nome}")


nao_nome = "joaozinho"
print("ao" not in nao_nome)
