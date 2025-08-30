# === SISTEMA DE INVENTARIO Y FACTURACIÓN ===

# --- Funciones Inventario ---
def cargar_inventario():
    inventario = []
    try:
        with open("inventario.txt", "r") as f:
            for linea in f:
                dato = linea.strip().split(",")
                inventario.append([dato[0], dato[1], float(dato[2]), int(dato[3])])
    except FileNotFoundError:
        pass
    return inventario

def guardar_inventario(inventario):
    with open("inventario.txt", "w") as f:
        for p in inventario:
            f.write(f"{p[0]},{p[1]},{p[2]},{p[3]}\n")

def añadir_producto(inventario):
    id_ = input("ID: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    inventario.append([id_, nombre, precio, stock])
    guardar_inventario(inventario)
    print("Producto agregado.")

def listar_productos(inventario):
    if not inventario:
        print("Inventario vacío.")
    else:
        for i in range(len(inventario)):
            p = inventario[i]
            print(f"{i+1}. ID:{p[0]} - {p[1]} - Precio:${p[2]} - Stock:{p[3]}")

def buscar_producto(inventario):
    buscar = input("Ingrese ID o nombre: ")
    encontrado = False
    for p in inventario:
        if buscar == p[0] or buscar.lower() in p[1].lower():
            print(f"Encontrado: ID:{p[0]} - {p[1]} - ${p[2]} - Stock:{p[3]}")
            encontrado = True
    if not encontrado:
        print("No encontrado.")

def actualizar_producto(inventario):
    listar_productos(inventario)
    if not inventario: return
    pos = int(input("Número de producto: ")) - 1
    if 0 <= pos < len(inventario):
        nuevo_precio = float(input("Nuevo precio: "))
        nuevo_stock = int(input("Nuevo stock: "))
        inventario[pos][2] = nuevo_precio
        inventario[pos][3] = nuevo_stock
        guardar_inventario(inventario)
        print("Producto actualizado.")

def eliminar_producto(inventario):
    listar_productos(inventario)
    if not inventario: return
    pos = int(input("Número de producto: ")) - 1
    if 0 <= pos < len(inventario):
        eliminado = inventario.pop(pos)
        guardar_inventario(inventario)
        print(f"Se eliminó: {eliminado[1]}")

# --- Funciones Facturación ---
def facturar(inventario):
    listar_productos(inventario)
    if not inventario: return
    pos = int(input("Seleccione producto: ")) - 1
    if 0 <= pos < len(inventario):
        cantidad = int(input("Cantidad: "))
        if cantidad <= inventario[pos][3]:
            total = cantidad * inventario[pos][2]
            factura = f"ID:{inventario[pos][0]}, {inventario[pos][1]}, Cant:{cantidad}, Total:{total}\n"
            
            # Guardar factura
            with open("facturas.txt", "a") as f:
                f.write(factura)

            # Actualizar stock
            inventario[pos][3] -= cantidad
            guardar_inventario(inventario)

            print("Factura generada:", factura)
        else:
            print("No hay stock suficiente.")

def listar_facturas():
    try:
        with open("facturas.txt", "r") as f:
            facturas = f.readlines()
        if not facturas:
            print("No hay facturas registradas.")
        else:
            print("=== FACTURAS ===")
            for i in range(len(facturas)):
                print(f"{i+1}. {facturas[i].strip()}")
    except FileNotFoundError:
        print("No hay facturas registradas.")


# --- Menú Principal ---
while True:
    inventario = cargar_inventario()
    print("\n=== MENÚ ===")
    print("1. Añadir producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Facturar")
    print("7. Listar facturas")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        añadir_producto(inventario)
    elif opcion == "2":
        listar_productos(inventario)
    elif opcion == "3":
        buscar_producto(inventario)
    elif opcion == "4":
        actualizar_producto(inventario)
    elif opcion == "5":
        eliminar_producto(inventario)
    elif opcion == "6":
        facturar(inventario)
    elif opcion == "7":
        listar_facturas()
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")