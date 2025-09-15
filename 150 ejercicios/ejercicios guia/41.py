palabras = ["sol", "luna", "sol", "estrella", "luna", "sol"]
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print(frecuencias)

