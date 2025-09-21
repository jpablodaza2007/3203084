class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []  

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total(self):
        return sum(p.precio for p in self.productos)



c = Carrito()
c.agregar_producto(Producto("Pan", 1500))
c.agregar_producto(Producto("Leche", 3200))
print("Total a pagar:", c.total())
