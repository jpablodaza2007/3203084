from inventario import *
from facturas import *

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Inventario")
        print("2. Facturación")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            menu_inventario()
        elif opcion == "2":
            menu_facturas()
        elif opcion == "3":
            print("Hasta luego")
            break
        else:
            print("Opción inválida.")

def menu_inventario():
    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Volver")
        op = input("Opción: ")

        if op == "1":
            pid = input("ID: ")
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            stock = input("Stock: ")
            add_producto(pid, nombre, precio, stock)
        elif op == "2":
            listar_productos()
        elif op == "3":
            busqueda = input("Ingrese ID o nombre: ")
            buscar_producto(busqueda)
        elif op == "4":
            pid = input("ID del producto: ")
            nuevo_precio = input("Nuevo precio (dejar vacío si no cambia): ")
            nuevo_stock = input("Nuevo stock (dejar vacío si no cambia): ")
            actualizar_producto(pid, nuevo_precio or None, nuevo_stock or None)
        elif op == "5":
            pid = input("ID a eliminar: ")
            eliminar_producto(pid)
        elif op == "6":
            break
        else:
            print("Opción inválida.")

def menu_facturas():
    while True:
        print("\n--- MENÚ FACTURAS ---")
        print("1. Crear factura")
        print("2. Listar facturas")
        print("3. Eliminar factura")
        print("4. Volver")
        op = input("Opción: ")

        if op == "1":
            fid = input("ID Factura: ")
            items = []
            while True:
                pid = input("ID producto (enter para finalizar): ")
                if not pid:
                    break
                cant = int(input("Cantidad: "))
                precio = float(input("Precio unitario: "))
                items.append((pid, cant, precio))
            crear_factura(fid, items)
        elif op == "2":
            listar_facturas()
        elif op == "3":
            fid = input("ID Factura a eliminar: ")
            eliminar_factura(fid)
        elif op == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "main":
    menu()