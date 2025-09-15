alumnos = {}
n = int(input("Número de alumnos: "))
for _ in range(n):
    nombre = input("Nombre: ")
    notas = []
    while True:
        nota = float(input("Nota (negativa para terminar): "))
        if nota < 0:
            break
        notas.append(nota)
    alumnos[nombre] = notas
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas) if notas else 0
    print(f"{alumno}: nota media {promedio:.2f}")