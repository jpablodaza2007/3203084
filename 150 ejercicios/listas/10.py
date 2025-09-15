n = int(input("¿Cuántos números?: "))
lista = []
pos = 0
neg = 0
i = 0
while i < n:
    num = float(input("Número: "))
    lista.append(num)
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    i += 1
print("Lista:", lista)
print("Positivos:", pos)
print("Negativos:", neg)