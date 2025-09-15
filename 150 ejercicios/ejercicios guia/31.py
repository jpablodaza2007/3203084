import random

class Animal:
    def __init__(self, nombre, tipo, energia=100, posicion_x=0, posicion_y=0):
        self.nombre = nombre
        self.tipo = tipo 
        self.energia = energia
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.vivo = True

    def mover(self):
        """Mueve el animal aleatoriamente"""
        if self.vivo:
            self.posicion_x += random.randint(-1, 1)
            self.posicion_y += random.randint(-1, 1)
            self.energia -= 5  

            if self.energia <= 0:
                self.vivo = False
                print(f"{self.nombre} ha muerto por falta de energía.")
            else:
                print(f"{self.nombre} se movió a ({self.posicion_x}, {self.posicion_y}). Energía: {self.energia}")

    def comer(self, cantidad):
        """El animal gana energía al comer"""
        if self.vivo:
            self.energia += cantidad
            print(f"{self.nombre} comió y ahora tiene {self.energia} de energía.")

    def estado(self):
        """Muestra el estado actual del animal"""
        estado = "vivo" if self.vivo else "muerto"
        return f"{self.nombre} ({self.tipo}) - Posición: ({self.posicion_x}, {self.posicion_y}) - Energía: {self.energia} - Estado: {estado}"



if __name__ == "__main__":
    leon = Animal("Simba", "carnívoro", energia=50)
    conejo = Animal("Bugs", "herbívoro", energia=30)

    print(leon.estado())
    print(conejo.estado())

  
    for _ in range(5):
        leon.mover()
        conejo.mover()

    
    conejo.comer(20)
    leon.comer(40)

    print("\nEstados finales:")
    print(leon.estado())
    print(conejo.estado())