import math 
class ErroNumeroNegativo(Exception):
    def __init__(self,mensagem):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
def tratamento(numero):
    if numero < 0:
        return f"Raiz quadrada indefinida!"
print("========= CALCULAR RAIZ QUADRADA =========")
while True:
    try:
        numero = float(input("Digite os número da operação: "))
        resultado = math.sqrt(numero)
        if numero < 0:
            raise ErroNumeroNegativo("Não existe raiz quadrada de números negativos.")
        tratamento(numero)
        print(f"A raiz quadrada de {numero} é {resultado}")
        break
    except ErroNumeroNegativo as e :
        print(e)
    except:
        print("Número inválido, por favor, digite um valor válido.")
