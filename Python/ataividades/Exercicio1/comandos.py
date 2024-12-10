import os

posicoes = [1,2,3,4,5,6,7,8,9]
game_over = False
turno = "x"
numero_turnos = 0

# Limpa o terminal
def clear():
    os.system("cls")

def Renderizar():
    tab = "                "
    clear()
    print(f"{tab}_{posicoes[0]}_|_{posicoes[1]}_|_{posicoes[2]}_\n{tab}_{posicoes[3]}_|_{posicoes[4]}_|_{posicoes[5]}_\n{tab} {posicoes[6]} | {posicoes[7]} | {posicoes[8]} ")

def input_user():
    # o try vai verificar se o número digitado foi uma string
    try:
        input_user_local = int(input("Insira um numero de 1 a 9: "))
    except:
        Renderizar()
        print("Número inválido!! Por favor digite um valor válido!!")
        input_user()
        return
    validar_input(input_user_local)
    imprimir_na_tabela(input_user_local)

def validar_input(input_user_local):
    if input_user_local < 1 or input_user_local > 9:
            Renderizar()
            print("Número inválido!! Por favor digite um valor válido!!")
            input_user() 
    
        
def imprimir_na_tabela(input_user_local):
    global numero_turnos 
    # controle verifica o valor q esta na tabale com o valor do input
    controle = 0
    # posicao vai sincronizar com o controle
    posicao = -1 
    while True:
        # manipula o loop
        if 1 <= controle <=9:
            # procura a posição na tabela para marcar
            if  input_user_local == controle:
                # verifica se o espaço já foi preenchido
                if "x" != posicoes[posicao] != "O":
                    posicoes[posicao] = turno
                    numero_turnos += 1
                else:
                    Renderizar()
                    print("Número inválido!! Por favor digite um valor válido!!")
                    input_user() 
            
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
    elif empate() == True:
        game_over =True
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
def empate():
    if numero_turnos == 9:
        return True
    return False