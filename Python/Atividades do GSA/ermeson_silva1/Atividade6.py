print("========================================")
print("      Calculadora de Descontos         ")
print("========================================")

preco = float(input("Digite o preço do produto em R$: "))
porcentagem_desconto = int(input("Digite a porcentagem do desconto: "))
total = porcentagem_desconto * 0.01 * preco
print("=====================================================")
print(f"O valor do desconto é: R${total}")