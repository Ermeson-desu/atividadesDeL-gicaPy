class FormaGeometrica:
    def calcular_area(self):
        return None
        
class Retangulo(FormaGeometrica):
    def __init__(self, largura:float, altura:float):
        self.__largura = largura
        self.__altura = altura
    
    def get_largura(self)->float:
        return self.__largura
    
    def get_altura(self)->float:
        return self.__altura
    
    def calcular_area(self)->str:
        return f"A área do retângulo é: {self.get_largura() * self.get_altura()};"
    
class Circulo(FormaGeometrica):
    def __init__(self,raio:float):
        self.__raio = raio 

    def get_raio(self)->float:
        return self.__raio
    
    def calcular_area(self)->str:   
        return f"A área do círculo é: {3.14159 * (self.get_raio() ** 2)};"

retangulo = Retangulo(39,30)
circulo = Circulo(43)
print(retangulo.calcular_area())
print(circulo.calcular_area())