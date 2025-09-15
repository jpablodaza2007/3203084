precios = []
i = 0
while i < 7:
    precios.append(float(input("Precio: ")))
    i += 1
minimo = maximo = precios[0]
for p in precios:
    if p > maximo:
        maximo = p
    if p < minimo:
        minimo = p
dif = maximo - minimo
print("Min:", minimo)
print("Max:", maximo)
print("Diferencia:", dif)