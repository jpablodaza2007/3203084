
class enemigo:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, jugador):
        jugador.vida -= self.ataque
        print(f"{self.nombre} ataca a {jugador.nombre} por {self.ataque} puntos de daño.")

    def esta_vivo(self):
        return self.vida > 0
    
enemigo1 = enemigo