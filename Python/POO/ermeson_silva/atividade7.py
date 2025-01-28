class Empregado:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = None
        self.set_salario(salario)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        try:
            if salario > 0:
                self.__salario = salario
            else:
                raise ValueError("O salário deve ser maior que zero.")
        except ValueError as e:
            print(e)

# Testando a classe Empregado
empregado = Empregado("Ana", 3500.00)
print(f"Empregado: {empregado.get_nome()}, Salário: {empregado.get_salario()}")

empregado.set_salario(-2000.00)  # Tentativa de definir um salário inválido
empregado.set_salario(4000.00)  # Definindo um salário válido
print(f"Empregado: {empregado.get_nome()}, Salário: {empregado.get_salario()}")
