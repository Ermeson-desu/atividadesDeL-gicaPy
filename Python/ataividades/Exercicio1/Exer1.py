import comandos
while comandos.game_over == False:
    comandos.Renderizar()
    comandos.input_user()
    comandos.mudar_turno()
    comandos.Renderizar()
    comandos.verificar_vitoria()