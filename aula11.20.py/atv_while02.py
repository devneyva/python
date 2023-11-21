#faça um código que leia o nome e a senha.Caso a senha for 
#igual ao nome do usuário, mestre uma menssagem de erro e pedindo
#as informaçoes novamente
while True:
    nome = input('Digite seu nome:')
    senha = input('Digite sua senha:')
    if senha == nome:
        print("Erro!")
    else:
       print("Acesso liberado!")
       break