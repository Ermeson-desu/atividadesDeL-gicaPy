class Endereco:
    def __init__(self,rua:str,cidade:str,estado:str):
        self.__rua = rua 
        self.__cidade = cidade
        self.__estado = estado
    
    # getters
    def get_rua(self)->str:
        return self.__rua
    
    def get_cidade(self)->str:
        return self.__cidade
    
    def get_estado(self)->str:
        return self.__estado
    
    def get_dados(self) -> str:
        return f"\nRua: {self.__rua.capitalize()}\nCidade: {self.__cidade.capitalize()}\nEstado: {self.__estado.capitalize()}"
    
class Pessoa:
    def __init__(self,nome:str,idade:int,endereco:Endereco):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco

    # getters
    def get_nome(self)-> str:
        return self.__nome
    
    def get_idade(self)->int:
        return self.__idade

    def get_endereco(self)->Endereco:
        return self.__endereco
    
    
    def exibir_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Idade: {self.get_idade()}")
        print(f"\nEndereço: {self.get_endereco().get_dados()}")

endereco = Endereco("azul-marinho","azul-bebê","azul")
pessoa = Pessoa("Kemirson",79,endereco)
pessoa.exibir_dados()