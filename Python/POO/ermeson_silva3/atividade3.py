class Pessoa:
    def __init__(self, nome:str, idade:str):
        self.__nome = nome
        self.__idade = idade

    # getters
    def get_nome(self)->str:
        return f"{self.__nome}"
    
    def get_idade(self)->str:
        return self.__idade
    
    def cumprimentar(self):
        print(f"Olá! Meu nome é {self.get_idade()}, tenho {self.get_idade()}anos.")

class Estudante(Pessoa):
    def __init__(self,nome:str,idade:int,matricula:str):
        super().__init__(nome, idade)
        self.__matricula = matricula

    def get_matricula(self)->str:
        return f"{self.__matricula}"
    
    def cumprimentar(self):
        print(f"Olá! Meu nome é {self.get_nome()}, tenho {self.get_idade()} anos, aluno da matricula {self.get_matricula()}.")


estudante = Estudante("Ana",21,"20230001")
estudante.cumprimentar()