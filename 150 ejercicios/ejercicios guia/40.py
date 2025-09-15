import json
import uuid
from datetime import datetime

inventario = {
    "P001": {"nombre": "Camiseta Egipcia", "precio": 25.0, "stock": 10, "desc": "Algodón, talla única"},
    "P002": {"nombre": "Anillo de Faraón (réplica)", "precio": 75.5, "stock": 3, "desc": "Baño dorado, talla ajustable"},
    "P003": {"nombre": "Mapa del Nilo", "precio": 12.0, "stock": 20, "desc": "Impreso en papel pergamino"},
}

ORDERS_FILE = "orders.jsonl"


def mostrar_inventario():
    print("\n=== INVENTARIO ===")
    print(f"{'ID':<6} {'Nombre':<30} {'Precio':>8} {'Stock':>6}")
    print("-" * 55)
    for pid, p in inventario.items():
        print(f"{pid:<6} {p['nombre']:<30} ${p['precio']:>7.2f} {p['stock']:>6}")
    print("-" * 55)

def generar_id_pedido():
    return str(uuid.uuid4())[:8]

def guardar_pedido(pedido):
    try:
        with open(ORDERS_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(pedido, ensure_ascii=False) + "\n")
    except Exception as e:
        print("Error guardando pedido:", e)


def agregar_producto():
    pid = input("Nuevo ID producto (ej. P010): ").strip()
    if not pid:
        print("ID inválido.")
        return
    if pid in inventario:
        print("Ese ID ya existe.")
        return
    nombre = input("Nombre: ").strip()
    try:
        precio = float(input("Precio: ").strip())
        stock = int(input("Stock inicial: ").strip())
    except ValueError:
        print("Precio o stock inválido.")
        return
    desc = input("Descripción (opcional): ").strip()
    inventario[pid] = {"nombre": nombre, "precio": precio, "stock": stock, "desc": desc}
    print("Producto agregado con éxito.")

def actualizar_producto():
    pid = input("ID del producto a actualizar: ").strip()
    if pid not in inventario:
        print("Producto no encontrado.")
        return
    p = inventario[pid]
    print("Dejar vacío para mantener el valor actual.")
    nombre = input(f"Nombre [{p['nombre']}]: ").strip()
    precio_in = input(f"Precio [{p['precio']}]: ").strip()
    stock_in = input(f"Stock [{p['stock']}]: ").strip()
    desc = input(f"Descripción [{p.get('desc','')}]: ").strip()
    if nombre:
        p['nombre'] = nombre
    if precio_in:
        try:
            p['precio'] = float(precio_in)
        except ValueError:
            print("Precio inválido, se mantiene el anterior.")
    if stock_in:
        try:
            p['stock'] = int(stock_in)
        except ValueError:
            print("Stock inválido, se mantiene el anterior.")
    if desc:
        p['desc'] = desc
    print("Producto actualizado.")

def eliminar_producto():
    pid = input("ID del producto a eliminar: ").strip()
    if pid in inventario:
        confirm = input(f"¿Confirmas eliminar {inventario[pid]['nombre']}? (sí/no): ").strip().lower()
        if confirm in ("sí", "si", "s"):
            del inventario[pid]
            print("Producto eliminado.")
    else:
        print("Producto no encontrado.")


def agregar_al_carrito(carrito):
    mostrar_inventario()
    pid = input("ID del producto para agregar al carrito: ").strip()
    if pid not in inventario:
        print("Producto no existe.")
        return
    try:
        cantidad = int(input("Cantidad: ").strip())
    except ValueError:
        print("Cantidad inválida.")
        return
    if cantidad <= 0:
        print("Cantidad debe ser mayor que 0.")
        return
    if inventario[pid]['stock'] < cantidad:
        print(f"No hay suficiente stock. Stock disponible: {inventario[pid]['stock']}")
        return
    # Añadir al carrito (suma cantidades si ya existía)
    carrito[pid] = carrito.get(pid, 0) + cantidad
    print(f"Añadido {cantidad} x {inventario[pid]['nombre']} al carrito.")

def ver_carrito(carrito):
    if not carrito:
        print("\nEl carrito está vacío.")
        return
    print("\n=== CARRITO ===")
    total = 0.0
    print(f"{'ID':<6} {'Nombre':<30} {'Cant':>5} {'Precio':>8} {'Subtotal':>10}")
    print("-" * 70)
    for pid, qty in carrito.items():
        p = inventario.get(pid)
        if not p:
            continue
        subtotal = p['precio'] * qty
        total += subtotal
        print(f"{pid:<6} {p['nombre']:<30} {qty:>5} ${p['precio']:>7.2f} ${subtotal:>9.2f}")
    print("-" * 70)
    print(f"{'':<43} Total: ${total:>9.2f}")
    return total

def quitar_del_carrito(carrito):
    if not carrito:
        print("El carrito está vacío.")
        return
    pid = input("ID del producto a quitar del carrito: ").strip()
    if pid not in carrito:
        print("No está en el carrito.")
        return
    try:
        cantidad = int(input("Cantidad a quitar (o 0 para eliminar todo): ").strip())
    except ValueError:
        print("Cantidad inválida.")
        return
    if cantidad <= 0 or cantidad >= carrito[pid]:
        del carrito[pid]
        print("Producto eliminado del carrito.")
    else:
        carrito[pid] -= cantidad
        print("Cantidad actualizada en el carrito.")

def vaciar_carrito(carrito):
    carrito.clear()
    print("Carrito vaciado.")

def checkout(carrito):
    if not carrito:
        print("No hay productos en el carrito.")
        return
    total = ver_carrito(carrito)
    confirm = input("¿Deseas proceder al pago? (sí/no): ").strip().lower()
    if confirm not in ("sí", "si", "s"):
        print("Pago cancelado.")
        return
  
    cliente = {}
    cliente['nombre'] = input("Nombre del cliente: ").strip() or "Cliente anónimo"
    cliente['direccion'] = input("Dirección de entrega: ").strip() or "No proporcionada"
    cliente['metodo_pago'] = input("Método de pago (tarjeta/efectivo): ").strip() or "efectivo"
   
    print("Procesando pago...")
  
    pedido_id = generar_id_pedido()
    fecha = datetime.utcnow().isoformat() + "Z"
    
    for pid, qty in carrito.items():
        if pid in inventario:
            inventario[pid]['stock'] -= qty
            if inventario[pid]['stock'] < 0:
                inventario[pid]['stock'] = 0

    pedido = {
        "id": pedido_id,
        "cliente": cliente,
        "items": [{"id": pid, "nombre": inventario.get(pid,{}).get("nombre",""), "cantidad": qty,
                   "precio_unit": inventario.get(pid,{}).get("precio",0)} for pid, qty in carrito.items()],
        "total": total,
        "fecha": fecha,
        "estado": "procesado"
    }
    guardar_pedido(pedido)
    print(f"Pago aceptado. Pedido #{pedido_id} creado. Total: ${total:.2f}")
    carrito.clear()


def menu_admin():
    while True:
        print("\n--- MODO ADMINISTRADOR ---")
        print("1. Ver inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("0. Volver")
        opcion = input("> ").strip()
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def menu_cliente():
    carrito = {}
    while True:
        print("\n--- TIENDA ONLINE (Cliente) ---")
        print("1. Ver inventario")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Quitar del carrito")
        print("5. Vaciar carrito")
        print("6. Checkout (pagar)")
        print("0. Salir al menú principal")
        opcion = input("> ").strip()
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_al_carrito(carrito)
        elif opcion == "3":
            ver_carrito(carrito)
        elif opcion == "4":
            quitar_del_carrito(carrito)
        elif opcion == "5":
            vaciar_carrito(carrito)
        elif opcion == "6":
            checkout(carrito)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def main():
    print("=== SIMULADOR DE TIENDA ONLINE ===")
    while True:
        print("\nSeleccione modo:")
        print("1. Cliente")
        print("2. Administrador")
        print("0. Salir")
        opcion = input("> ").strip()
        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            menu_admin()
        elif opcion == "0":
            print("Saliendo... ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
