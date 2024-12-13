import comandos
import ui_interface


while comandos.game_over == False:
    ui_interface.cabecalho()
    comandos.Renderizar()
    comandos.input_user()
    comandos.mudar_turno()
    comandos.Renderizar()
    comandos.verificar_vitoria()
