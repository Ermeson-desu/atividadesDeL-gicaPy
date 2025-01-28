class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.set_nota(nota)

    def set_nota(self, nota):
        """Define a nota do aluno, validando se está entre 0 e 10."""
        if 0 <= nota <= 10:
            self.nota = nota
        else:
            raise ValueError("Nota inválida! A nota deve estar entre 0 e 10.")

    def mostrar_dados(self):
        """Exibe os dados do aluno."""
        print(f'Nome: {self.nome}, Nota: {self.nota}')


try:
    aluno1 = Aluno("João", 8)
    aluno1.mostrar_dados()

    aluno2 = Aluno("Maria", 12)  
    aluno2.mostrar_dados()
except ValueError as e:
    print(f'Erro: {e}')
