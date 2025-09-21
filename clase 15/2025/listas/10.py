class equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def mostrar_miembros(self):
        for miembro in self.miembros:
            print(miembro)
e = equipo("Desarrolladores")
e.agregar_miembro("Ana")
e.agregar_miembro("Luis")
e.agregar_miembro("Carlos")
e.mostrar_miembros()