from os import *
opcoes=["1-Somar", "2-Subtrair", "3-Dividir","4-Multiplicar", "5-Sair"]

def renderizar():
    print("---------------------------------------------------")
    print("|                   CALCULADORA                   |")
    print("---------------------------------------------------")
    i=0
    while i<4:
        print(opcoes[i])
        i+=1
    print("---------------------------------------------------")
       
def escolhaUser():
    entrada_do_usuario = input(" Escolha a operacao desejada.\n Insira um numero de 1 a 4: ")
    if entrada_do_usuario == "1":
        somar()

    if entrada_do_usuario == "2":
        subtrair()

    if entrada_do_usuario == "3":
        dividir()
        
    if entrada_do_usuario == "4":
        multiplicar() 
        

def somar():
    n1= int(input("Insira o primeiro numero da soma: "))
    n2= int(input("Insira o segundo valor da soma: "))
    res = n1+n2
    print(f"Resultado:{n1} + {n2} = {res}")

def subtrair():
    n1=int(input("Insira o primeiro numero da subitracao: "))
    n2= int(input("Insira o segundo valor da subitracao: "))
    res = n1-n2
    print(f"Resultado:{n1} - {n2} = {res}")

def dividir():
    n1=int(input("Insira o primeiro numero da divisao: "))
    n2= int(input("Insira o segundo valor da divisao: "))
    res = n1/n2
    print(f"Resultado:{n1} / {n2} = {res}")

def multiplicar():
    n1=int(input("Insira o primeiro numero da multiplicacao: "))
    n2= int(input("Insira o segundo valor da multiplicacao: "))    
    res = n1*n2
    print(f"Resultado:{n1} * {n2} = {res}")

def nova_operacao():
    print(" Deseja fazer alguma operacao??")
    novaEscolha = input("Pressione 1 para [sim] e 2 para [nao]: ")
    if novaEscolha == "1":
        return True
    if novaEscolha == "2":
        return False
    
def Clear():
    system('cls')