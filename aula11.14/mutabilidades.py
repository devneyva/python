#alguns cuidados com dados mutaveis
#mutáveis são dados que podem ter seu valor alterado na memória do dispositivel
#imutáveis são dados que só podem ser copiados da memória do dispositivo


lista = ['Joaõ','Paulo']
lista[1] = 'Jose'
print(lista)

nome = 'Neyva'
novo_nome = nome 
nome = 'Loane'
print(nome)
print(novo_nome)

print(nome)