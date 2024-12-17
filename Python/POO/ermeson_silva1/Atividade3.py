def tabuada(numero_usuario):
    for i in range(1,11):
        resultado = numero_usuario * i
        print(f"{numero_usuario} * {i} = {resultado}")

entrada_usuario = int(input("Digite um numero inteiro: "))

tabuada(entrada_usuario)