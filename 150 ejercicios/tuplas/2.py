num = (3, 5, 1, 9, 7)
maximo = num[0]
minimo = num[0]
for n in num:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n
print("Máximo:", maximo, "Mínimo:", minimo)