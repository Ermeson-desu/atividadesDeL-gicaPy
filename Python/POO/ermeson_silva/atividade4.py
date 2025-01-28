class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = None
        self.set_email(email)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        try:
            if "@" in email and ".com" in email:
                self.__email = email
            else:
                raise ValueError("Email inválido. Certifique-se de que contém '@' e '.com'.")
        except ValueError as e:
            print(e)


usuario = Usuario("João", "joao@example.com")
print(f"Nome: {usuario.get_nome()}, Email: {usuario.get_email()}")

usuario.set_email("joaoexample") 
usuario.set_email("joao@exemplo.com") 
print(f"Nome: {usuario.get_nome()}, Email: {usuario.get_email()}")
