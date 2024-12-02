print("========================================")
print("         Calculadora de IMC             ")
print("========================================")

peso = float(input("Digite o seu peso em kilograma (Kg): "))
altura = float(input("Digite sua altura em metros (m):  "))
imc = peso/(altura*altura) 
print("=========================================")
print(f"O seu indice de massa corporal(imc) é: {imc} ")