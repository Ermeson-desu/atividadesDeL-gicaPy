frutas = ['maçã', 'banana', 'laranja', 'uva']
tamanho = len(frutas)
posicao = 0

while posicao < tamanho :
    print(f"Removendo {frutas[0]}")
    frutas.pop(0)
    posicao += 1
    