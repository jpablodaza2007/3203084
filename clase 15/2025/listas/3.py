class Inventario:
    def __init__(self):
        self.items = ["manzana", "banana", "naranja"]

    def obtener_items_por_longitud(self, longitud_minima):
        items_filtrados = [item for item in self.items if len(item) >= longitud_minima]
        return items_filtrados 

inventario = Inventario()
items_largos = inventario.obtener_items_por_longitud(6)
print(f"Items con longitud de 6 o más: {items_largos}")