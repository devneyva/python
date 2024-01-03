#CRUD: created , readed , updated and deleted
dic = {'Nome': 'Paulo,'} #created
dic2 = dict(Idade=23) #created
dic['Nome'] #readed
reading = dic2.get('idade') #readed
dic.update(sobrenome= 'Junior') #updated #inserindo intens #forma direta
print(dic)
dic.update({ 'idade' : 23 })
print(dic)
tupla = ('peso', 59),
#qnd adc uma tupla no dicionário temos que colocar uma virgula no final
dic.update(tupla) #update
print(dic)
lista = ['data','13/04/1996'], #em lista tbm temos que colocar uma virgula no final
dic.update(lista) #update
lista = ['data','13/04/1996'],['Numeros', [1,2,3,4]]
dic.update(lista) #update 
dic.clear() #deleted
print(f'dados dos dicionario: {dic}')
