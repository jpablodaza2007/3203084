n = int(input("¿Cuántas edades?: "))
edades = []
i = 0
while i < n:
    edad = int(input("Edad: "))
    edades.append(edad)
    i += 1
impares = []
for edad in edades:
    if edad % 2 == 1:
        impares.append(edad)
print("Impares:", impares)