class copo:

    # base: base do copo
    # altura: altura do copo
    # raio: raio do copo
    # estado: boca para cima ou boca para baixo
    def __init__(self, base: float, altura: float, raio: float, estado: str = "boca para cima"):
        self.__base = base
        self.__altura = altura
        self.__raio = raio
        self.__estado = estado 
    
    # Setters
    def set_base(self, base:float):
        self.__base = base

    def set_altura(self, altura:float):
        self.__altura = altura

    def set_raio(self, raio:float):
        self.__raio = raio

    def set_estado(self, estado:str):
        self.__estado = estado

    # Getters
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    def get_raio(self):
        return self.__raio

    def get_estado(self):
        return self.__estado
    
    # sobreposição
    def __str__(self):
        return f"Base: {self.__base}\nAltura: {self.__altura}\nRaio: {self.__raio}\nEstado: {self.__estado}"

    # métodos
    def mudar_estado(estado:str):
        if(estado == "boca para cima"):
            estado = "boca para baixo"
        elif(estado == "boca para baixo"):
            estado = "boca para cima"
        else:
            print("Erro: estado esperado ou incompleto!")

    def exibir_atributos():
        print(f"{copo.get_altura}")