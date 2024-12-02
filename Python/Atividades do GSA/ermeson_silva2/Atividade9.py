linha = "--------------------------------------------"
print(linha)
print("|         Indicador de triângulo           |")
print(linha)

lado1 = float(input("\nDigite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do trinângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 >= 0:
    if lado1 == lado2 and lado3 == lado1:
        print("Tringulo equilátero.")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("Triângulo isóceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("Valor inválido!!")