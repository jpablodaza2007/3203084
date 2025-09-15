notas = []
for i in range(5):
    while True:
            nota = float(input("Ingrese la nota (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
media = sum(notas)
nota_max = max(notas)
nota_min = min(notas)

print("\nNotas ingresadas:", notas)
print(f"Nota media: {media / len(notas) if notas else 0}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")