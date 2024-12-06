import os

posicoes = [1,2,3,4,5,6,7,8,9]
game_over = False
turno = "x"

# Limpa o terminal
def clear():
    os.system("cls")

def Renderizar():
    clear()
    print(f"_{posicoes[0]}_|_{posicoes[1]}_|_{posicoes[2]}_\n_{posicoes[3]}_|_{posicoes[4]}_|_{posicoes[5]}_\n {posicoes[6]} | {posicoes[7]} | {posicoes[8]} ")

def input_user():
    input_user_local = int(input("Insira um numero de 1 a 9: "))
    # controle verifica o valor q esta na tabale com o valor do input
    controle = 0
    # posicao vai sincronizar com o controle
    posicao = -1 
    while True:
        if controle <=9:
            if input_user_local == controle:
                posicoes[posicao] = turno
        elif controle >9:
            break
        controle +=1
        posicao+=1

def mudar_turno():
    global turno
    if turno == "x":
        turno = "O"
    elif turno == "O":
        turno = "x"

def verificar_vitoria():
    global game_over 
    if vitoria_horizontal() == True:
        game_over = True
    elif vitoria_vertical() == True:
        game_over = True
    elif vitoria_diagonal() == True:
        game_over = True
    return False

def vitoria_horizontal():
    if posicoes[0] == posicoes[1] == posicoes[2]:
        return True
    elif posicoes[3] == posicoes[4] == posicoes[5]:
        return True
    elif posicoes[6] == posicoes[7] == posicoes[8]:
        return True
    return False

def vitoria_vertical():
    if posicoes[0] == posicoes[3] == posicoes[6]:
        return True
    elif posicoes[1] == posicoes[4] == posicoes[7]:
        return True
    elif posicoes[2] == posicoes[5] == posicoes[8]:
        return True
    return False

def vitoria_diagonal():
    if posicoes[0] == posicoes[4] == posicoes[8]:
        return True
    elif posicoes[2] == posicoes[4] == posicoes[6]:
        return True
    return False