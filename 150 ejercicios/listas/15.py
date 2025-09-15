n = int(input("Cantidad de países: "))
paises = []
i = 0
while i < n:
    paises.append(input("País: "))
    i += 1
invertido = []
j = n - 1
while j >= 0:
    invertido.append(paises[j])
    j -= 1
print(invertido)