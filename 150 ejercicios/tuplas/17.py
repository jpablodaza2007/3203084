t = ("python", "tupla", "ejercicio")
invertida = ()
for palabra in t:
    inv = ""
    i = len(palabra)-1
    while i >= 0:
        inv += palabra[i]
        i -= 1
    invertida += (inv,)
print(invertida)