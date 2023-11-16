letra1 = input("Digite a primeira letra:")
letra2 = input("Digite a segunda letra:")
letra3 = input("Digite a terceira letra:")
letra4 = input("Digite a quarta letra:")
letra5 = input("Digite a quinta letra:") 


letras_digitadas = letra1,letra2,letra3,letra4,letra5
vogais = ["A","a","E", "e","I","i","O","o","U","u"]
consoantes = ["B","C",'K',"D","F","G","H","L","M","N",'P']

lista_consoantes = []


if letras_digitadas != vogais:
    print("É consoante!")


lista_consoantes.append(consoantes)
print(lista_consoantes)