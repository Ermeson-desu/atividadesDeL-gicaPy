from abc import ABC,abstractmethod

class Conta(ABC):
    def __init__(self, saldo):
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def sacar(self, valor):
        if valor + 2.50 <= self.saldo:
            self.saldo -= (valor + 2.50)
            print(f"Saque de R${valor:.2f} realizado com sucesso. Taxa de R$2.50 aplicada.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

class ContaPoupanca(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)
        self.saques_gratuitos = 3

    def sacar(self, valor):
        if self.saques_gratuitos > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.saques_gratuitos -= 1
                print(f"Saque de R${valor:.2f} realizado com sucesso. Saques gratuitos restantes: {self.saques_gratuitos}.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            if valor + 5.00 <= self.saldo:
                self.saldo -= (valor + 5.00)
                print(f"Saque de R${valor:.2f} realizado com sucesso. Taxa de R$5.00 aplicada.")
            else:
                print("Saldo insuficiente para realizar o saque.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")


contaCorrente = ContaCorrente(1000)
contaCorrente.depositar(500)
contaCorrente.sacar(200)
contaCorrente.sacar(1500) 

contaPoupanca = ContaPoupanca(1000)
contaPoupanca.depositar(500)
contaPoupanca.sacar(200)
contaPoupanca.sacar(300)
contaPoupanca.sacar(400)
contaPoupanca.sacar(100)  