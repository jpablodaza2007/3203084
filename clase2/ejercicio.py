lista = ["Jose","Manuel","Luis","pedro","Pablo","ivan","juan"]
print(lista[0:3])
for i in lista:
    print(i)

lista2 = lista
print(lista2)

lista2 = lista[0:3]
print(lista2)

lista2 = lista[:]
print(lista2)

lista2 = lista[::-1]
print(lista2)

lista2 = lista[-3]
print(lista2)

lista2 = [1,2,5,7,9,8,10,12.15,20,30]
lista2[6]= "pepe"
print(lista2)

lista.append("pedro pablo")
print(lista)

lista.insert(6,"natalia")
print(lista)

lista.append("fabian pablo")
print(lista)

lista.extend(["jon","carlos","karen"])
print(lista)

lista.remove("pedro")
print(lista)

lista.pop(3)
print(lista)

for i in range(len(lista2)):
    print(i,":",lista2[i])

lista3 = "Jose" in lista
print(lista3)

lista4 = ["a","a","b","b","c","c","a"]
cantidad = lista4.count("a")
print(cantidad)

cantidad = lista.count("pedro pablo")
print(cantidad)

print(lista.sort())

lista5=(lista.sort())
print(lista)

lista6 = sorted(lista)
print(lista6)

lista = sorted(lista)
print(lista)

lista.reverse()
print(lista)

lista6 = lista.copy()
print(lista)

lista7 = list(lista)
print(lista6)

lista.clear()
print(lista)

