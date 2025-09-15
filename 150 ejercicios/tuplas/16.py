t = ("Ana", "Luis", "Marta")
vocales = "aeiouAEIOU"
total = 0
for palabra in t:
    for letra in palabra:
        if letra in vocales:
            total += 1
print("Total vocales:", total)