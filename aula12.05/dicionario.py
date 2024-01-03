#dicionários possuem chaves(KEYS) e valores(VALUES)
#parametro: {} ou dict()
#o valor pode se repetir, mas as chaves não.
#
pessoa = {'nome:': 'Paulo',
          'Sobrenome':'Junior'
          }
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())

#imprir uma chave
print(pessoa['Sobrenome'])

print(pessoa['Sobrenome'])
#sempre quando criar um dc colocar virgulas 
d1 = { 'valor1': 100,
       'valor2': 200,
       'valor3': 300
       }
d2 = d1

print(d1)
d2['valor2'] = 'Jefferson'
print(d1)
print(type(d2))

print(d2.get('valor2'))

d3 = d1.pop('valor3')
print(d1)

outro_nome = {'valor5': 5,
              'valor6': 6,}
d1.update(outro_nome)
print(d1)

print(d1.has_key('valor1'))



#como criar um diciobario
#dic = {} or dic = dict{chave = valor}

#############################################################
#MÉTODOSSS
#clear = limpa o dicionário
#del = excluir uma chave del.dic[chave] exclui chaves e valores
#keys - entrega todas das cahves do dicionário
#values - entrega todos os valores
#items - ele entrega todos os itens com chave e valor
#get - entrega um valor refenciado pelo a chave
#update - ele utilixado para inserir itens no dicionário
#copy - ele faz uma cópia do dicionario garantido um novo endereço de memória
#sorted - ordena um dicionário pelas suas chaves 
