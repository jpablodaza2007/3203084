dic1 = {"a": 2, "b": 3}
dic2 = {"a": 5, "c": 4}

# Suma de diccionarios
suma = {}

for clave in dic1:
    if clave in dic2:
        suma[clave] = dic1[clave] + dic2[clave]
    else:
        suma[clave] = dic1[clave]

for clave in dic2:
    if clave not in suma:
        suma[clave] = dic2[clave]

print("Suma:", suma)
