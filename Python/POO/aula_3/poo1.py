class Carro:
    def __init__(self,nome, marca, velMax,velMin,valor):
        self.nome = nome
        self.marca = marca
        self.velMax = velMax
        self.velMin = velMin
        self.valor = valor


class Meu_carro(Carro):
    def __init__(self,dono):
        self.dono = dono


corola = Meu_carro
 
 #Essa prática não é legal, ela acessa diretamente as variáveis de uma classe
corola.nome = "Corola XEI 2.0 Aut Flex 2023"
corola.marca = "Toyota"
corola.velMax = 199
corola.velMin = 0  
corola.valor = 154.990

print(f"\nNome do carro: {corola.nome}")
print(f"Marca do carro: {corola.marca}")
print(f"Velocidade máxima: {corola.velMax}K/h")
print(f"Valor do carro: R${corola.valor}")
corola.dono = input("\nPara efetuar a compra digite seu nome: ")

print(f"PARABÉNS PELA COMPRA {corola.dono}!!\n")
