linha = "--------------------------------------------"
print(linha)
print("|         Indicador nota escolar           |")
print(linha)

nota = float(input("\nDigite sua nota: "))

if nota < 5 and nota >= 0:
    print("Reprovado!!")
elif nota >= 5 and nota < 7:
    print("Regular.")
elif nota >= 7 and nota < 9:
    print("Bom!")
elif nota >= 9:
    print("EXCELENTE!!")
else:
    print("Valor inválido!")
