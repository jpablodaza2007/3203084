notas = {
    "Ana": (4.5, 3.8, 4.2),
    "Luis": (3.0, 3.5, 4.0),
    "Marta": (5.0, 4.8, 4.9)
}

promedios = {}
for estudiante, califs in notas.items():
    promedios[estudiante] = sum(califs) / len(califs)

print(promedios)
