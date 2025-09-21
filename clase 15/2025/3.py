class veiculo:
    def __init__(self, motor, velocidad, capacidade):
        self.motor = motor
        self.velocidade = velocidad
        self.capacidade = capacidade

car1 = veiculo("V8", "200km/h", "5 pessoas")
print(car1.motor, car1.velocidade, car1.capacidade)

    