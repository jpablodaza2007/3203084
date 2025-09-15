n = int(input("¿Cuántos números?: "))
numeros = []
i = 0
suma = 0
while i < n:
    num = float(input("Número: "))
    numeros.append(num)
    suma += num
    i += 1
promedio = suma / n
mayores = []
for num in numeros:
    if num > promedio:
        mayores.append(num)
print("Promedio:", promedio)
print("Mayores al promedio:", mayores)