frutas = ["maçã", "banana", "laranja"]
def exibir_lista(frutas):
    indices = 0
    for fruta in frutas:    
        print(f"{indices}- {fruta};")
        indices +=1

exibir_lista(frutas)
while True:
    try:

        entrada = int(input("Digite um número correspondente a fruta para remove-la: "))
        frutas.pop(entrada)
        exibir_lista(frutas)
    except IndexError:
        print("Indice inválido! Por favor, insira um valor válido!")