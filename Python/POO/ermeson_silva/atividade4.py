class ErroIdade(Exception):
    def __init__(self, mensagem: str) -> None:
        self.mensagem = mensagem
        super().__init__(self.mensagem)

def tratamento(idade):
    if idade < 0:
        return f"Idade inválida! Por favor, digite um valor válido!"
    
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            raise ErroIdade("A idade não pode ser menor que zero!")
        tratamento(idade)
        print(f"Sua idade é {idade}")
        break
    except ErroIdade as e:
        print(e)
    except:
        print("Idade inválida, por favor digite um valor válido!")