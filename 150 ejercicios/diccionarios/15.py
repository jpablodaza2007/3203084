dic = {'a': 10, 'b': 5, 'c': 10, 'd': 3}
valor = int(input("Valor a buscar: "))
claves = []
for k, v in dic.items():
    if v == valor:
        claves.append(k)
print(f"Claves con valor {valor}: {claves}")