class sena:
    def __init__(self, ubicacion, cursos, nombre):
        self.ubicacion = ubicacion
        self.cursos = cursos
        self.nombre = nombre

sena1 = sena("Calle 13", "gnaderia", "CBA")
print(sena1.ubicacion, sena1.cursos, sena1.nombre)