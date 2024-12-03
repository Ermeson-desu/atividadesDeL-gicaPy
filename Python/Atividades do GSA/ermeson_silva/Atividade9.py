temperaturas = [30, 25, 28, 35, 22, 27]

posicao = 0
somatorio = 0
while posicao < len(temperaturas):
    somatorio = somatorio + temperaturas[posicao]
    posicao+=1
resultado = somatorio/len(temperaturas)
print(resultado)