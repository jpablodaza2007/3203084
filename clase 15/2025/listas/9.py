class Color:
    def __init__(self, nombre):
        self.nombre = nombre


colores = ["rojo", "azul", "verde", "amarillo"]


c1 = Color(colores)
c2 = Color(colores[1])
c3 = Color(colores)
c4 = Color(colores)


if c1.nombre == "azul":
    print("¿El color de c1 es azul? VERDADERO")
else:
    print("¿El color de c1 es azul? FALSO")

if c2.nombre == "azul":
    print("¿El color de c2 es azul? VERDADERO")
else:
    print("¿El color de c2 es azul? FALSO")

if c3.nombre == "azul":
    print("¿El color de c3 es azul? VERDADERO")
else:
    print("¿El color de c3 es azul? FALSO")

if c4.nombre == "azul":
    print("¿El color de c4 es azul? VERDADERO")
else:
    print("¿El color de c4 es azul? FALSO")