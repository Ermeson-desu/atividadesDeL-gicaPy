from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self,nome:str) -> None:
        self.nome = nome
    
    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome,salario:int) -> None:
        super().__init__(nome)
        self.__salario = salario

    def calcular_salario(self)->int:
        return self.__salario
    
class Operador(Funcionario):
    def __init__(self, nome,valor_hora:int,hora:int) -> None:
        super().__init__(nome)
        self.__valor_hora = valor_hora
        self.__hora = hora

    def calcular_salario(self)->int:
        return self.__hora* self.__valor_hora
    
gerente = Gerente("Maria",5000)
operador = Operador("José",20,50)
print(f"Salário de Maria: {gerente.calcular_salario()}")
print(f"Salário de José: {operador.calcular_salario()}")