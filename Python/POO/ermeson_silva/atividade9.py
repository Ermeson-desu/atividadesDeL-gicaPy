class Animal:
    def fazer_som(self):
        print("som genérico")

class Cachorro(Animal):
    def fazer_som(self):
        super().fazer_som()
        print("Auau!!")

cachorro = Cachorro()
cachorro.fazer_som()