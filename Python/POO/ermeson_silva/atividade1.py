class ContaBancaria:
    def __init__(self,titular:str, saldo:float = 0.0):
        self.__titular = titular
        self.__saldo = saldo
    
    def get_titular(self)-> str:
        return self.__titular

    def get_saldo(self)-> float:
        return self.__saldo

    def set_saldo(self,valor):
        self.__saldo = valor

    def validar_saldo(self,saque):
        if saque > self.get_saldo():
            raise ValueError("Saldo insuficiente!!\n")
        else:
            self.set_saldo(self.get_saldo() - saque) 

def app():
    try:
        titular = ContaBancaria("Mateus",35)
        print(f"Titular: {titular.get_titular()} \nSaldo: R${titular.get_saldo()}")
        saque = float(input("Digite o valor do saque: "))
        if saque < 0:
            raise ValueError("Valor inválido! Você não pode sacar um valor negativo.")
        titular.validar_saldo(saque)
        print(f"Titular: {titular.get_titular()} \nSaldo: R${titular.get_saldo()}")
    except ValueError as e :
        print(f"Erro de valor: {e}")

app()