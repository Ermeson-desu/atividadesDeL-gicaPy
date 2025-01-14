class ContaBancaria:
    def __init__(self,nome: str, saldo: int):
        self.__nome = nome
        self.__saldo = saldo

    #  getters 
    def get_nome(self)-> str:
        return f"{self.__nome}"
    
    def get_saldo(self)-> int:
        return self.__saldo
    
    #  setters
    def set_nome(self,nome:str):
        self.__nome = nome

    def set_saldo(self,saldo:int):
        self.__saldo = saldo

    #  soma o valor que o usuário inseriu com o valor do saldo anterior
    def depositar(self,deposito:int)->int:
        self.set_saldo(self.get_saldo() + deposito)

    #  subtrai o valor que o usuário inseriu com o valor do saldo anterior
    def sacar(self,saque:int):
        if self.get_saldo() >= 0:
            self.set_saldo(self.get_saldo() - saque)
        else:
            print("Saldo insuficiente!!")
            
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
print(f"saldo da conta: {conta.get_saldo()}")