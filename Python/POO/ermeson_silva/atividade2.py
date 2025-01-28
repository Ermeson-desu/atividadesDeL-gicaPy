from abc import ABC,abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        ...

class Carro(Veiculo):
    def mover(self):
        print("O carro está movendo.")

class Bicicleta(Veiculo):
    def mover(self):
        print("A bicicleta está movendo.")

try:
    veiculo = Veiculo()  
except TypeError as e:
    print(f"Erro ao criar uma instância de Veiculo: {e}")


carro = Carro()
carro.mover()

bicicleta = Bicicleta()
bicicleta.mover()
