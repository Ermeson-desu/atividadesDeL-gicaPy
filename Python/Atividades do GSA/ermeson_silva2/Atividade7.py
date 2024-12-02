print( "Calculadora: ")
numero1 = float(input("Digite o primeiro número da operação: "))
numero2 = float(input("Digite o segundo número da operação: "))

print("Digite [1]- somar; [2] - Subtrair; [3]- Dividir; [4] - multiplicar;")
operacao = int(input("Escolha uma das opções acima: "))

if operacao == 1:
    resultado = numero1 + numero2
    print(f"O resultado da soma é {resultado}")
elif operacao == 2: 
    resultado = numero1 - numero2
    print(f"O resultado da subtração é {resultado}")
elif operacao == 3:
    if numero1 == 0 or numero2 == 0:
        resultado = numero1/numero2
        print(f"O resultado da divisão é {resultado}")
    else:
        print("Operação inválida!!")
    
elif operacao == 4:
    resultado = numero1*numero2
    print(f"O resultado da multiplicação é {resultado}")
else:
    print("Operação inválida!!")