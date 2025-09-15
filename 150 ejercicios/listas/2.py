lista = []
def mostrar_menu():
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Buscar")
    print("4. Mostrar")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige opción: ")
    if opcion == '1':
        valor = input("Valor a agregar: ")
        lista.append(valor)
    elif opcion == '2':
        valor = input("Valor a eliminar: ")
        if valor in lista:
            lista.remove(valor)
        else:
            print("No está en la lista")
    elif opcion == '3':
        valor = input("Valor a buscar: ")
        if valor in lista:
            print("Está en la lista")
        else:
            print("No está")
    elif opcion == '4':
        print(lista)
    elif opcion == '5':
        break
    else:
        print("Opción incorrecta")