print("Verificacion si un numero es par o impar ejrercicio1")
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

print("Categoría de un estudiante según su edad ejercicio2")
edad = int(input("Introduce la edad del estudiante: "))
if edad < 12:
    print("El estudiante es un niño.")
elif 12 <= edad < 18:
    print("El estudiante es un adolescente.")
else:
    print("El estudiante es un adulto.")

print("SIstema de calificación de notas ejercicio3")
nota = float(input("Introduce la nota del estudiante: "))
if nota >= 90:
    print("A")
elif 80 <= nota < 90:
    print("B")
elif 70 <= nota < 80:
    print("C")
elif 60 <= nota < 70:
    print("D")
else:
    print("F")
