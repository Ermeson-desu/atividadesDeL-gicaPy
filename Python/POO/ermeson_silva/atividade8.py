class Estoque:
    def __init__(self):
     
        self.produtos = []

    def adicionar_produto(self, produto):
        """Adiciona um produto ao estoque."""
        self.produtos.append(produto)
        print(f'Produto "{produto}" adicionado ao estoque.')

    def remover_produto(self):
        """Remove o último produto do estoque."""
        try:
            if len(self.produtos) == 0:
                raise ValueError("O estoque está vazio. Não há produtos para remover.")
            produto_removido = self.produtos.pop()
            print(f'Produto "{produto_removido}" removido do estoque.')
        except ValueError as e:
            print(f'Erro: {e}')

    def mostrar_estoque(self):
        """Exibe todos os produtos no estoque."""
        if self.produtos:
            print("Produtos no estoque:")
            for produto in self.produtos:
                print(f'- {produto}')
        else:
            print("O estoque está vazio.")

estoque = Estoque()
estoque.adicionar_produto("Produto 1")
estoque.adicionar_produto("Produto 2")
estoque.mostrar_estoque()

estoque.remover_produto()
estoque.remover_produto()
estoque.remover_produto()  
estoque.mostrar_estoque()
