class Animal:
    def __init__(self, name):
        self.name = name

    def sonido(self):
        print(f"{self.name} hace un sonido.")


class Perro(Animal):
    def sonido(self):
        print(f"{self.name} ladra.")


perro = Perro("Firulais")
perro.sonido()
