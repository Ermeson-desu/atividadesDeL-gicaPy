print("    ==Dobrar números==")
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        numero+=numero
        print(f"O dobro do número q vc digitou é :{numero}")
        break
    except:
        print("Número invalido, tente novament:")