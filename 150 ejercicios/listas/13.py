palabras = []
while True:
    p = input("Palabra (stop para terminar): ")
    if p == "stop":
        break
    palabras.append(p)
print("Palabras ingresadas:", palabras)