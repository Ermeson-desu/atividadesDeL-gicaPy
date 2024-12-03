palavras = ["peixe", "limão", "batata", "abacaxi", "melancia"]

contador =0
resultado = 0
while contador< len(palavras):
    if len(palavras[contador]) > 5:
        resultado +=1
    contador+=1
print(f"Quantidade de palavras com mais de 5 caracteres {resultado}")