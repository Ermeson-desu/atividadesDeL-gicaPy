class Login:
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = None
        self.set_senha(senha)

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        try:
            if len(senha) >= 6:
                self.__senha = senha
            else:
                raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        except ValueError as e:
            print(e)


login = Login("usuario_teste", "123456")
print(f"Usuário: {login.get_usuario()}, Senha: {login.get_senha()}")

login.set_senha("123")  
login.set_senha("senhaSegura123") 
print(f"Usuário: {login.get_usuario()}, Senha: {login.get_senha()}")
