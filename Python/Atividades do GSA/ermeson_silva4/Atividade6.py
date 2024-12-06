numeros_inseridos = []

while True:
    numero = int(input("Digite um número para adicionar a lista [ou digite 0 para sair]: "))
    if numero != 0:
        numeros_inseridos.append(numero)
    else:
        break
posicao = 0
somatorio = 0
while posicao < len(numeros_inseridos):
    somatorio = somatorio + numeros_inseridos[posicao]
    posicao+=1
print(f"Somatório da lista é {somatorio}")