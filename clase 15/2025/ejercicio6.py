class producto:
    def __format__(self, format_spec):
        if format_spec == "Precio":
            return str(self.precio)
        return str(self)

    def __init__(self, precio, producto):
        self.precio = precio
        self.producto = producto

    def __str__(self):
        return f"El producto {self.producto} tiene un precio de {self.precio}"

van = producto(3000, "computadora")
print(van)
print(repr(van))
print(f"{van:Precio}")

