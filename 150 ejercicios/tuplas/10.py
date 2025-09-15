lista = [1, 2, 3]
t = tuple(lista)
lista2 = []
for i in range(len(t)):
    lista2.append(t[i])
lista2.append(4)
t2 = tuple(lista2)
print(t2)