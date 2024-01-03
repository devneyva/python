#cria uma lista com notas e adiciona de em um dicionário e imprima
lista = [['Aluno1',10],['Aluno2',3],['Aluno3',8]]
dic = {}
dic.update(lista)
print(dic)
 
 # insedir mais 4 alunos e suas notas no dicionário

dic.update(aluno4 = 9, aluno5= 10, aluno6= 5, aluno7 = 9)
print(dic)

#faça um codigo  que pede a marce e o modelo insere ele em uma lista 
# e depois insere em um dicionário e imprima os dois resultados
 
marca = input('Qual a marca do carro?')
modelo = input('Qual é o modelo?')
lista01 = []
lista01.append(marca)
lista01.append(modelo)
print(lista01)
dic01 = {}
dic01.update([lista01]) #transformar a lista da lista
print(dic01)

dic01['Posche'] = 'Opa' #adicionando
print(dic01)













