numeros = [5, 8, 12, 20, 3]

def soma():
    somatorio = 0
    for i in range(1,5):
        somatorio = somatorio + numeros[i]
    print(somatorio)
soma()