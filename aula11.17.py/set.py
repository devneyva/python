#Set - conjuntos
set1 = set('Paulo')
set2 = {"Paulo","Laura","Anny"}
print(set1)
print(set2)

lista = [1,2,3,4,5,6,7,8,77,77,77]
set03 = set(lista)
print(set03)
print(lista)
print(7 in set03)
print(7 not in set03)
print(77 in lista)
print(88 not in lista)

set03.add('Paulo')
set03.add(1)
set03.add(6)
set03.update("Paulo")
set03.discard("Paulo")
set03.clear()
print(set03)

set04 = {1,2,3,4,5}
set05 = {4,5,6,7,8}

set06 = set04 | set05 #união de conjuntos 
print(set06)

set06 = set04 & set05 #interseção de conjuntos 
print(set06)

set06 = set04 - set05 #diferença de conjuntos (o que está no primeiro que não está no segundo)
print(set06)


