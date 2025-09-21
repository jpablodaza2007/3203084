class peliculas:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
class cine:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            print(f"{pelicula.titulo} - {pelicula.genero}")
c = cine()
c.agregar_pelicula(peliculas("Inception", "Ciencia Ficción"))       
c.agregar_pelicula(peliculas("The Godfather", "Crimen"))
c.mostrar_peliculas()