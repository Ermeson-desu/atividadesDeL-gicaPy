def tratamento(idade):
    if idade<0:
        return f"Idade inválida! Por favor, digite um valor válido!"
while True:
    try:
        idade = int(input("Digite sua idade: "))
        tratamento(idade)
        print(f"Sua idade é {idade}")
        break
    except:
        print("Idade inválida, por favor digite um valor válido!")