numeros = [1,2,3,4,5,6,7,8,9,10]
dobrados = []
posicao = 0
multiplicacao = 0
while posicao < len(numeros):
    multiplicacao = numeros[posicao] *2
    dobrados.append(multiplicacao)
    posicao +=1
print(numeros)
print(dobrados)