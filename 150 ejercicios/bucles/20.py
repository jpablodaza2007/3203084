n = int(input("Ingresa un número: "))
while n >= 10:
    suma = 0
    for d in str(n):
        suma += int(d)
    n = suma
print("Resultado:", n)
