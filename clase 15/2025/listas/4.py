class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []  

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0



e1 = Estudiante("Juan")
e1.agregar_nota(4.5)
e1.agregar_nota(3.8)
print(f"Notas de {e1.nombre}: {e1.notas}")
print("Promedio:", e1.promedio())
