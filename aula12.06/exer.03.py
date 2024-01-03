#crie um sistema de login e senha
#crie um dic contendo os acessos dos colaboradores com nome de usuário e senha
#em seguida peça as informacoes e valide o logindo do usuário

#nome = input('Digite seu nome: ')
#senha = input('Digite sua senha: ')
#dic = {}
#dic.update([nome])
#dic.update(senha)
#print(dic)
#colaboradores = {'Ney','Neyva'}

#if nome == colaboradores:
  #  print('Acesso liberado!')
#else:
#    print('Acesso negado')

dic_acesso = {'Paulo': '1234', 'Joao': '1211'}

usuario_senha = {}
usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

usuario_senha[usuario] = senha #há tres formas diferentes adc no dic sem métodos#1
#usuario_senha = {usuario: senha} #2
#usuario_senha = dict(usuario, senha) #3
for chaves in dic_acesso.keys():
    if chaves == usuario and dic_acesso[chaves] == senha:
            print('Acesso liberado!')
            break
    else:
         print(f'Senha incorreta para o usuário {usuario}')
         break
else:
      print('Usiário incorreto!')





















