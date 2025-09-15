total = int(input("¿Cuántas edades?: "))
edades = []
for i in range(total):
    edades.append(int(input("Edad: ")))
mayor = edades[0]
menor = edades[0]
suma = 0
for edad in edades:
    if edad > mayor: mayor = edad
    if edad < menor: menor = edad
    suma += edad
promedio = suma / total
print("Máxima:", mayor)
print("Mínima:", menor)
print("Promedio:", promedio)