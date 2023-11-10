entrada = input("[E] para entrar e [S] para passar: ")
senha_digitada = input("Digite a senha de acesso:")
senha = "1234"

if entrada == "E" or entrada == "e":
    if senha == senha_digitada:
        print("Sucesso, voce entrou")
    else:
        print("senha incorreta")
elif entrada == "S" or entrada == "s":
    if senha == senha_digitada:
        print("Sucesso, voce passou!")
    else:
        print("voce não passou,senha incorreta")
        print("Voce não selencionou uma opção válida")


