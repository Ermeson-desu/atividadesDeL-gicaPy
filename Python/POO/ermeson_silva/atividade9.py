class Animal:
    def fazer_som(som)->str:
        if som==None:
            print("Som genérico")
        else:
            print(som)


class Cachorro(Animal):
    def fazer_som(self) -> str:
        return super().fazer_som()