class persona:
    def __init__(self, nombre, vida, estatura, peso, raza, genero, color_ojos, color_cabello, clase, musculatura, arma):
        self.nombre = nombre
        self.vida = vida
        self.estatura = estatura
        self.peso = peso
        self.raza = raza
        self.genero = genero
        self.color_ojos = color_ojos
        self.color_cabello = color_cabello
        self.clase = clase
        self.musculatura = musculatura
        self.arma = arma

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y soy un {self.clase} de la raza {self.raza}.")




p1 = persona("Leonidas", 31, "1.98m", "95kg", "Humano", "Masculino", "Gris", "Castaño", "Guerrero", "Atlética", "Espada")
p2 = persona("Robin", 600, "1.83m", "75kg", "Elfo", "Masculino", "Azul", "Rubio", "Arquero", "Arquero", "Arco y flechas")
p3 = persona("Tort", 139, "1.35m", "90kg", "Enano", "Masculino", "Marrón", "Pelirrojo", "Guerrero", "Robusta", "Hacha")
p4 = persona("Merlin", 60, "1.80m", "80kg", "Maiar", "Masculino", "Gris", "Blanco", "Mago", "Mago", "Bastón")
p5 = persona("Frodo", 39, "1.22m", "45kg", "Hobbit", "Masculino", "Marrón", "Castaño", "Granjero", "Delgada", "Daga")
p6 = persona("Sam", 38, "1.20m", "50kg", "Hobbit", "Masculino", "Marrón", "Castaño", "Jardinero", "Delgada", "Daga")
personajes = [p1, p2, p3, p4, p5, p6]
print(f"Nombre: {p1.nombre}, Edad: {p1.vida}, Estatura: {p1.estatura}, Peso: {p1.peso}, Raza: {p1.raza}, Género: {p1.genero}, Color de ojos: {p1.color_ojos}, Color de cabello: {p1.color_cabello}, Clase: {p1.clase}, Musculatura: {p1.musculatura}, Arma: {p1.arma}")
print(f"Nombre: {p2.nombre}, Edad: {p2.vida}, Estatura: {p2.estatura}, Peso: {p2.peso}, Raza: {p2.raza}, Género: {p2.genero}, Color de ojos: {p2.color_ojos}, Color de cabello: {p2.color_cabello}, Clase: {p2.clase}, Musculatura: {p2.musculatura}, Arma: {p2.arma}")
print(f"Nombre: {p3.nombre}, Edad: {p3.vida}, Estatura: {p3.estatura}, Peso: {p3.peso}, Raza: {p3.raza}, Género: {p3.genero}, Color de ojos: {p3.color_ojos}, Color de cabello: {p3.color_cabello}, Clase: {p3.clase}, Musculatura: {p3.musculatura}, Arma: {p3.arma}")
print(f"Nombre: {p4.nombre}, Edad: {p4.vida}, Estatura: {p4.estatura}, Peso: {p4.peso}, Raza: {p4.raza}, Género: {p4.genero}, Color de ojos: {p4.color_ojos}, Color de cabello: {p4.color_cabello}, Clase: {p4.clase}, Musculatura: {p4.musculatura}, Arma: {p4.arma}")
print(f"Nombre: {p5.nombre}, Edad: {p5.vida}, Estatura: {p5.estatura}, Peso: {p5.peso}, Raza: {p5.raza}, Género: {p5.genero}, Color de ojos: {p5.color_ojos}, Color de cabello: {p5.color_cabello}, Clase: {p5.clase}, Musculatura: {p5.musculatura}, Arma: {p5.arma}")
print(f"Nombre: {p6.nombre}, Edad: {p6.vida}, Estatura: {p6.estatura}, Peso: {p6.peso}, Raza: {p6.raza}, Género: {p6.genero}, Color de ojos: {p6.color_ojos}, Color de cabello: {p6.color_cabello}, Clase: {p6.clase}, Musculatura: {p6.musculatura}, Arma: {p6.arma}")

