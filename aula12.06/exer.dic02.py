# crie um cadrasto de clientes recebendo nome idade data de
#anovessário e endereço completo adc todas as informacocoes em um dc 
#imprima

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
dat_nascimento = input('Digite a sua data de nascimento:')
nome_rua = input('Digite o nome de sua rua:')
numero_casa = (int(input('Digite o número de sua casa:')))
bairro = input('Digite o bairro que voce mora:')

informacoes = {}
#informacoes.update([nome, idade, dat_nascimento, nome_rua, numero_casa, bairro])
informacoes.update([nome])
informacoes.update([idade])
informacoes.update([dat_nascimento])
informacoes.update([nome_rua])
informacoes.update([numero_casa])
informacoes.update([bairro])



print(informacoes)