palabras = ["sol", "luna", "estrella", "sol", "luna", "sol"]
frecuencia = {}

for p in palabras:
    if p in frecuencia:
        frecuencia[p] += 1
    else:
        frecuencia[p] = 1

for clave in frecuencia:
    print(clave, ":", frecuencia[clave])
