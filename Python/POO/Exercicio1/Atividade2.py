numeros = [5, 8, 12, 20, 3]

def soma(lista):
    somatorio = 0
    for i in range(5):
        somatorio = somatorio + lista[i]
    return somatorio

print("A soma dos membros é: ")
print(soma(numeros))
