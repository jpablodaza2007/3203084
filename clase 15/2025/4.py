class persona:
    def __new__(cls,nombre,edad):
        return super().__new__(cls)

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Eliminando objeto {self.nombre}")

ana = persona("Ana", 30)
carlos = persona("Carlos", 25)
print(ana.nombre, ana.edad)
print(carlos.nombre, carlos.edad)
