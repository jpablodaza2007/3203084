numeros = []
for _ in range(5):
    numeros.append(int(input("Número: ")))
prom = sum(numeros)/len(numeros)
print("Promedio:", prom)