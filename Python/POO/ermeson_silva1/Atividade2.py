
def soma(lista):
    somatorio = 0
    for i in range(5):
        somatorio = somatorio + lista[i]
    return somatorio

numeros = [5, 8, 12, 20, 3]

print("A soma dos membros é: ")
print(soma(numeros))
