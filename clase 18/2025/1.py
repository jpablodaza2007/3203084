class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

per = [
    p1 := persona("juan", "perez", 30),
    p2 := persona("ana", "gomez", 25),
    p3 := persona("luis", "martinez", 40)
]


p1.nombre = "pepe"
print(per[per.index(p1)].nombre, per[per.index(p1)].apellido, per[per.index(p1)].edad)
