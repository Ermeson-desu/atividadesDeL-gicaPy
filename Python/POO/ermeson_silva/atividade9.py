while True:
    try:
        entrada_usuario = input("Digite números separado por [, ] vírgulas: ")
        lista_usuario = entrada_usuario.split(",")
        soma = sum(int(numeros) for numeros in lista_usuario)
        print(f"A soma dos números é {soma}")
        break
    except:
        print("Valor inválido, por favor, digite somente números.")
