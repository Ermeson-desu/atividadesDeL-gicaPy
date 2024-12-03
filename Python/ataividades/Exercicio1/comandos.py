import os

posicoes = [1,2,3,4,5,6,7,8,9]
game_over = False
turno = "x"

def clear():
    os.system("cls")
def Renderizar():
    clear()
    print(f"_{posicoes[0]}_|_{posicoes[1]}_|_{posicoes[2]}_\n_{posicoes[3]}_|_{posicoes[4]}_|_{posicoes[5]}_\n {posicoes[6]} | {posicoes[7]} | {posicoes[8]} ")
def input_user():
    input_user_local = int(input("Insira um numero de 1 a 9: "))
    controle = 0
    i = -1
    while True:
        if controle <=9:
            if input_user_local == controle:
                posicoes[i] = turno
        elif controle >9:
            break
        controle +=1
        i+=1
def mudar_turno(this):
    this.turno = turno
    if this.turno == "x":
        this.turno = "O"
    elif this.turno == "O":
        this.turno = "x"
