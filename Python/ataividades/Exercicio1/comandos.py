import os

posicoes = ["1","2","3","4","5","6","7","8","9"]
gameOver = False
turno = "x"
jogador2= "O"

def clear():
    os.system("cls")
def Renderizar():
    clear()
    print(f"_{posicoes[0]}_|_{posicoes[1]}_|_{posicoes[2]}_\n_{posicoes[3]}_|_{posicoes[4]}_|_{posicoes[5]}_\n {posicoes[6]} | {posicoes[7]} | {posicoes[8]} ")
def input_user():
    input_user_local = input("Insira um numero de 1 a 9: ")
    i = 0
    while i < 9:
        if input_user_local == posicoes[i]:
            posicoes[i]= turno
            aux = jogador2
            jogador2 = turno
            turno = aux
      
        i+=1