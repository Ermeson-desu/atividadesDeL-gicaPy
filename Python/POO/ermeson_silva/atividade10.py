class Ponto:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self,outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __str__(self) -> str:
        return f"{self.x,self.y}"


ponto1= Ponto(1,2)
ponto2= Ponto(1,2)
resultado = ponto2 + ponto1
print(resultado)