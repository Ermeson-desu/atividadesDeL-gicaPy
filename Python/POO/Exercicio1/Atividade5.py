notas = [7.5, 8.0, 6.5, 9.0, 7.0]

def calcular_media(lista):
    somatorio = 0
    for i in lista:
        somatorio = somatorio + i    
    print(f"A média da lista é {somatorio/len(lista)}")

calcular_media(notas)