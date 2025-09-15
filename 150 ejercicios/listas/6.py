numeros = []
for i in range(10):
    n = int(input("Num: "))
    numeros.append(n)
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print("Original:", numeros)
print("Pares:", pares)