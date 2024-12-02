idade = float(input(" Digite sua idade: "))

if idade < 12 and idade > 0:
    print("Você é uma criança.")
elif idade >= 12 and idade < 18:
    print("Você é um adolecente.")
elif idade >= 18:
    print("Você é um adulto.")
else:
    print("Valor inválido.")