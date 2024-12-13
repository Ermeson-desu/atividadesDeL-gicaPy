import Exer1
import comandos

linha = "---------------------------------------------------------------------"

def cabecalho():
    print(linha)
    print("|                           JOGO DA VELHA                           |")
    print(linha)
    print()

def vitoria():
    ganhador = ""
    if comandos.turno == "x":
        ganhador = "O"
    else:
        ganhador = "x"
    print(f"                  PARABÉNS VITÓRIA JOGADOR '{ganhador}'!!           ")
    
"""
def empate():
    print("            Infelizmente deu empate. Quer jogar novamente?   ")
    jogar_novamente = input("                   Digite [1-SIM]  ou [2-NÃO]: ")
    if int(jogar_novamente) == 1:
        Exer1.iniciar()
    elif int(jogar_novamente) == 2:
        exit()
    else:
        print("           Opção inválida! Digite um valor válido.")
        empate() """