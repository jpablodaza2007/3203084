compras = ["Pan","Leche","huevos"]
print("Lista inicial;")
print("compras")

# Agregar elementos
compras.append("queso")
compras.append("yogurt")
print("\ndespues de agrgar que y yogurd")
print("compras")

# Insertar en posición específica
compras.insert(1, "mantequilla") 
print("\nDespués de insertar mantequilla en posición 1:")
print(compras)

# Eliminar elementos
compras.remove("huevos") 
print("\nDespués de eliminar huevos:")
print(compras)

# Eliminar por posición
elemento_eliminado = compras.pop(0) 
print("\nEliminamos el primer elemento:", elemento_eliminado)
print("Lista final:", compras)
