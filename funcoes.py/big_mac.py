#def big_mac():
#    print('Seu lanche está sendo preparado')

#big_mac()

def fazer_mac(nome):
    print(f'Seu mac está sendo preparado, {nome}!')
#fazer_mac('Ana')


def fazer_batata(tamanho):
    print(f'Sua batata é no tamanho {tamanho} !')

def preparar_refrir(tipo, tamanho):
    print(f'o tipo de refri é {tipo} no tamanho {tamanho}')

#fazer_mac('Neyva')
#preparar_refrir('Peps', 'Pequeno')
#fazer_batata('Grande')

def combo_big_mac(nome,tamanho_batata, tipo_refri, tamanho_refri):
    fazer_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrir(tipo_refri, tamanho_refri)

#combo_big_mac('Neyva', 'Media','peps', 'grande')

def somar_numeros(n1,n2):
    return n1 + n2

#r = somar_numeros(1,2)
#print(r)

def nmr_maior(n1,n2):
    if n1 > n2:
        return f'O número {n1} é maior que o número {n2}!'
    else:
        return f'O número {n2} é maior que o número {n1}!'
    
#print(nmr_maior(1,4))
#print('Bem vindo!')
#nome = input('Digite seu nome: ')

def comprar_colar(tamanho, cor):
    print(f' Ecolheu o colar do tamanho {tamanho} da cor {cor}')

def comprar_brimco(tamanho, cor):
    print(f'Ecolheu brinco do tamanho {tamanho} da cor {cor}')

def comprar_pulseira( cor):
    print(f'Ecolheu pulseira da cor {cor}')

#comprar_colar('médio', 'Dourado')
#comprar_pulseira('Prata')
#comprar_brimco('pequeno','Dourado')

def comprar_combo(tamanho_colar,cor_colar, pulseira, tamanho_brinco, cor_brinco):
    comprar_colar(tamanho_colar,cor_colar)
    comprar_pulseira(pulseira)
    comprar_brimco(tamanho_brinco, cor_brinco)
    #print(f'Parabens! {nome} voce recebeu um desconto de 25%')

#comprar_combo('Grande','Dourada','Dourada', 'Pequeno','Prata')

def digitar_nome(nome):
    print(f'{nome}')

def digitar_idade(idade):
    print(f'Tem {idade} anos de idade')

def dgitar_estado(estado):
    print(f'Nasceu no estado de {estado}')

def digitar_genero(gereno):
    print(f'O genrero é {gereno}')

def infor_user(username, year_old, state, gerere):
    digitar_nome(username)
    digitar_idade(year_old)
    dgitar_estado(state)
    digitar_genero(gerere)

infor_user('Neyva', 19 , 'Ceará', 'Feminino')

def division(n1, n2):
    division = n1 / n2
    return division

resultado = division(8,4)
#print(resultado)