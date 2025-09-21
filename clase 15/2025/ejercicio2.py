class alumno:
    def __init__(self, Altura, curso, tipo_sangre):
        self.Altura = Altura
        self.curso = curso
        self.tipo_sangre = tipo_sangre

car1 = alumno("1.75m", "3ro", "O+")
print(car1.Altura, car1.curso, car1.tipo_sangre)