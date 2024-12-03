valores = []

while True:
    numero = int(input("Digite um número para adicionar a lista [ou digite -1 para sair]: "))
    if numero != -1:
        valores.append(numero)
    else:
        break
contador = 0
while contador < len(valores):
    print(f"{valores[contador]}")
    contador+=1