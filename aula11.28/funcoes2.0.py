def numero_reverso(numero):
    reverso = 0 

    while numero > 0:
        #pegar o ultimo valor do número
        ultimo_valor = numero % 10

        #add ultimo valor 
        reverso = (reverso * 10) + ultimo_valor

        #tira o ultimo valor
        numero = numero // 10
    return reverso #retorna o reverso


numero  = int(input('Digite um número: '))
resultado = numero_reverso(numero)
print(f'O número informado foi {numero} e o reverso dele é: {resultado}')