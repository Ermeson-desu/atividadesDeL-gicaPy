entrada_usuario = int(input("Digite um numero inteiro: "))

def tabuada(numero_usuario):
    for i in range(11):
        resultado = numero_usuario * i
        print(f"{numero_usuario} * {i} = {resultado}")

tabuada(entrada_usuario)