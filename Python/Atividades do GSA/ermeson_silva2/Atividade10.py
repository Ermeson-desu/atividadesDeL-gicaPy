linha = "--------------------------------------------"
print(linha)
print("|           Jogo da advinhação             |")
print(linha)

print("\nEscolha um número inteiro de 1 a 10: ")
valor_final = 6

while True:
    numero = int(input())
    if numero >= 1 and numero <=10:
        if numero < valor_final:
            print("Muito baixo.")
        elif numero == valor_final:
            print("Você acertou!!")
            break
        elif numero > valor_final:
            print("Muito alto.")
    else:
        print("Valor inválido!!")