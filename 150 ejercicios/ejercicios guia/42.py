personas = {"Ana": 20, "Luis": 22, "Marta": 20, "Pedro": 22}
invertido = {}

for nombre, edad in personas.items():
    invertido.setdefault(edad, []).append(nombre)

print(invertido)

