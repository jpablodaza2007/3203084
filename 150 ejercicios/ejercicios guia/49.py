frutas = {
    "rojas": ["fresa", "cereza"],
    "verdes": ["manzana", "kiwi"],
    "amarillas": ["plátano", "piña"]
}

inverso = {}
for color, lista_frutas in frutas.items():
    for fruta in lista_frutas:
        inverso[fruta] = color

print(inverso)

