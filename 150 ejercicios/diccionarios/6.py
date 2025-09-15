inventario = {}
while True:
    prod = input("Producto ('fin' para salir): ")
    if prod == 'fin':
        break
    cant = int(input("Cantidad: "))
    if prod in inventario:
        inventario[prod] += cant
    else:
        inventario[prod] = cant
print(inventario)