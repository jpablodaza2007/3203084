palabras = ['ana', 'beto', 'ana', 'carlos', 'beto', 'ana']
frecuencias = {}
for p in palabras:
    if p in frecuencias:
        frecuencias[p] += 1
    else:
        frecuencias[p] = 1
print(frecuencias)