while True:
    try:
        numeros = [10,20,30]
        entrada = int(input("Escolha um dos indices a seguir: [0,1,2]: "))
        print(f"{numeros[entrada]}")
        break
    except:
        print("Opção inválido! Por favor, escolha uma opção válida!")