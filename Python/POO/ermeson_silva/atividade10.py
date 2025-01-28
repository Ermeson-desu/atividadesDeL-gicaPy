class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        """Exibe os dados da pessoa."""
        print(f'Nome: {self.nome}, Idade: {self.idade}')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)  # Chama o construtor da classe base (Pessoa)
        self.salario = None  # Inicializa o atributo salario com um valor padrão
        self.set_salario(salario)

    def set_salario(self, salario):
        """Define o salário do funcionário, validando se é positivo."""
        try:
            if salario > 0:
                self.salario = salario
            else:
                raise ValueError("Salário inválido! O salário deve ser positivo.")
        except ValueError as e:
            print(f'Erro: {e}')

    def mostrar_dados(self):
        """Exibe os dados do funcionário, incluindo o salário."""
        super().mostrar_dados()
        if self.salario is not None:
            print(f'Salário: {self.salario}')
        else:
            print("Salário não definido.")


# Exemplo de uso
try:
    funcionario1 = Funcionario("Carlos", 30, 3000)
    funcionario1.mostrar_dados()

    funcionario2 = Funcionario("Ana", 25, -1500)  # Salário inválido, deve gerar erro
    funcionario2.mostrar_dados()
except ValueError as e:
    print(f'Erro ao criar o funcionário: {e}')
