texto = input("Texto: ")
vocales = "aeiouAEIOU"
for c in texto:
    if c not in vocales:
        print(c, end='')
print() 