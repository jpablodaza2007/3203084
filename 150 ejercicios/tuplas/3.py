t = (1, 2, 3, 2, 4, 2, 5)
num = int(input("Número a contar: "))
cont = 0
for el in t:
    if el == num:
        cont += 1
print("Apariciones:", cont)