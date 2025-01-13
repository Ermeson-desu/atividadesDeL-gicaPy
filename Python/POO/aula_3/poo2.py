class Pessoa:
    def __init__(self, nome:str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    def se_apresente(self):
        print(f"\nNome:{self.get_nome()}\nCPF: {self.get_cpf()}")

    def get_nome(self) -> str:
        return f"{self.__nome}"
    
    def get_cpf(self) -> str:
        return f"{self.__cpf}"
    
    def set_nome(self,novo_nome):
        self.__nome = novo_nome
  

class Eleitor(Pessoa):
    def __init__(self, nome,cpf, titulo_eleitor):
        super().__init__(nome,cpf)
        self.__titulo_eleitor = titulo_eleitor

    def se_apresente(self):
        print(f"\nNome:{self.get_nome()}\nCPF: {self.get_cpf()} \nTitulo de eleitor: {self.get_titulo_eleitor()}\n")

    def get_titulo_eleitor(self) -> str:
        return f"{self.__titulo_eleitor}"

class Partido:
    def __init__(self, nome:str, numero:int) -> None:
        self.__nome = nome
        self.__numero = numero
    
    def get_nome_partido(self)->str:
        return self.__nome
    
    def get_numero_partido(self)->int:
        return self.__numero
    
    def dados(self):
        print(f"Nome: {self.get_nome_partido()} - {self.get_numero_partido}")
        
  
    
class Candidato(Pessoa):
    def __init__(self,nome:str,cpf:str,partido:Partido):
        super().__init__(nome,cpf)
        self.__partido = partido
    
    def se_apresente(self):
        print(f"Candidato: {self.get_nome()}")
        print(f"Partido: {self.__partido.get_nome_partido()}")
        print(f"N°{self.__partido.get_numero_partido()}")


if __name__ == "__main__":
    pessoa1 = Pessoa("Ermeson","039480934")
    pessoa1.se_apresente()
    eleitor1 = Eleitor("Camille","230948202", "0983483")
    eleitor1.se_apresente()
    pl= Partido("Partido Liberal",22)
    pt = Partido("Partido dos Trabalhadores", 13)
    candidato1 = Candidato("Brunosonaro","000.111.222-33",pl)
    candidato1.se_apresente()
