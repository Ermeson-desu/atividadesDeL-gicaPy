class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # getters
    def Get_nome(self):
        return f"{self.__nome}"
    
    def Get_idade(self):
        return self.__idade
    
    def Cumprimentar(self):
        print(f"Olá! Meu nome é {self.Get_idade()}, tenho {self.Get_idade()}anos.")