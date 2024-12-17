def numeros_pares_lista(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print(lista[i])


numeros = [2, 7, 10, 15, 20, 33, 42]

numeros_pares_lista(numeros)