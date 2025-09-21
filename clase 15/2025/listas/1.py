class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  

    def agregar_producto(self, producto):
        self.productos.append(producto)  
        print(f"Se añadió '{producto}' a la tienda {self.nombre}")

    def listar_productos(self):
        print(f"Productos en {self.nombre}:")
        if not self.productos:
            print("No hay productos en la tienda.")
        else:
            for producto in self.productos:
                print(f"- {producto}")


mi_tienda = Tienda("Supermercado Local")
mi_tienda.agregar_producto("Manzanas")
mi_tienda.agregar_producto("Pan")
mi_tienda.listar_productos()