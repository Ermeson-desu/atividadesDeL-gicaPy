
print("      ===CALCULADORA DIVISÃO===")
while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1/numero2
        print(f"Resultado: {resultado}")
        break
    except ZeroDivisionError:
        print("Impossível dividir por 0")
    except ValueError:
        print("Valor inválido, digite um valor válido!!")