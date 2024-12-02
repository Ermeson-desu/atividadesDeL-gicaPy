print("===============================================")
print("      Descobridor de números impar e par       ")
print("===============================================")

n1 = int(input("Digite um número inteiro: "))
res = n1%2
print("===============================================")
if res == 0:
    print( "O número que você digitou é par!!")
else:
    print("O número que você digitou é impar!!")