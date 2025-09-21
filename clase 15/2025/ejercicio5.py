class granja:
    def __init__(self, animal, ectareas, capacidad):
        self.animal = animal
        self.ectareas = ectareas
        self.capacidad = capacidad

gran1 = granja("vacas", "50", "200")
gran2 = granja("ovejas", "20", "150")
gran3 = granja("pollos", "10", "500")
print(gran1.animal, gran1.ectareas, gran1.capacidad)
print(gran2.animal, gran2.ectareas, gran2.capacidad)
print(gran3.animal, gran3.ectareas, gran3.capacidad)