frase = input("Frase: ")
count = 0
for c in frase:
    if c == " ":
        count += 1
print("Espacios:", count)