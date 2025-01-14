class Carro:
    def __init__(self,marca: str, modelo: str,ano: int):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    # exibir dados do carro
    def exibir_dados(self):
        print(f"Modelo do carro: {self.__modelo};")
        print(f"Marca do carro: {self.__marca};")
        print(f"Ano do carro: {self.__ano}; ")

meu_carro = Carro("Toyota","Corolla",2020)
meu_carro.exibir_dados()