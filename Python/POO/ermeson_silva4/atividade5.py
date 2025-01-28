print("======| Calcular Soma |======")
while True:
    try:
        termo1 = int(input("Digite o primeiro número: "))
        termo2 = int(input("Digite o segundo número: "))
        resposta= termo1 + termo2
        print(f"Resultado da soma é {resposta}!")
        break
    except:
        print("Valor inválido!! Por favor, insira um valor válido.")
