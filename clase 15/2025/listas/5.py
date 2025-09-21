class Biblioteca:
    def __init__(self):
        self.libros = []  

    def agregar_libro(self, titulo):
        self.libros.append(titulo)

    def mostrar_libros(self):
        return self.libros

    def eliminar_libro(self, titulo):
        if titulo in self.libros:
            self.libros.remove(titulo)



b = Biblioteca()
b.agregar_libro("Don Quijote")
b.agregar_libro("Cien años de soledad")
print("Libros:", b.mostrar_libros())
b.eliminar_libro("Don Quijote")
print("Libros después de eliminar:", b.mostrar_libros())
