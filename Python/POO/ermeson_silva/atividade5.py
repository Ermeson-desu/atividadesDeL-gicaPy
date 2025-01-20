class Produto:
    def __init__(self, nome="não listado", preco=0):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
produto1 = Produto()
produto2 = Produto("PÃO")
produto3 = Produto("coxinha",2.80)

print(produto1.get_nome())
print(produto2.get_nome())
print(f"Produto escolhido: {produto3.get_nome()} preço: {produto3.get_preco()}")
