t = ("perro", "gato", "elefante", "ratón")
corta = t[0]
for p in t:
    if len(p) < len(corta):
        corta = p
print("Palabra más corta:", corta)