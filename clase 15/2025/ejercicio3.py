class empresa:
    def __init__(self, nombre, sector, empleados):
        self.nombre = nombre
        self.sector = sector
        self.empleados = empleados

car1 = empresa("Empresa1", "Tecnología", 100)
print(car1.nombre, car1.sector, car1.empleados)