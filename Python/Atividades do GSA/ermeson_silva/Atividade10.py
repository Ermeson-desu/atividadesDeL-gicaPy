nomes = []

while True:
    nome_do_usuario = str(input("Digite nomes pessoais [ou digite 'sair' para cancelar a ação]: "))
    if nome_do_usuario == "sair":
        break
    nomes.append(nome_do_usuario)
    
nomes.sort()
print(nomes)