palabras = ["python", "inteligencia", "sol", "matemáticas"]
longitudes = {}

for palabra in palabras:
    longitudes[palabra] = len(palabra)


mas_larga = max(longitudes, key=longitudes.get)

print(longitudes)
print("Palabra más larga:", mas_larga, "(", longitudes[mas_larga], "letras )")
