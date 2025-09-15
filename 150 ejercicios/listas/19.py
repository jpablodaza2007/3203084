entrada = input("Palabras separadas por espacio: ")
palabras = []
inicio = 0
for i in range(len(entrada)):
    if entrada[i] == " " or i == len(entrada) - 1:
        final = i
        if i == len(entrada) - 1:
            final = i + 1
        palabras.append(entrada[inicio:final])
        inicio = i + 1
mayor = palabras[0]
longitud_mayor = 0
for p in palabras:
    tam = 0
    for _ in p:
        tam += 1
    if tam > longitud_mayor:
        longitud_mayor = tam
        mayor = p
print("Palabra más larga:", mayor)
print("Longitud:", longitud_mayor)