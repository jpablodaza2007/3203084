class tarea:
    def __init__(self, completar):
        self.completar = completar
        self.estado = False
        
    def marcar_como_completada(self):
        self.estado = True 
    
    def __str__(self):
        return (f"Tarea: {self.completar}, Completada: {self.estado}")
# Uso
t1 = tarea("Hacer la cama") 
t2 = tarea("Estudiar para el examen")
t3 = tarea("Comprar alimentos") 
t4 = tarea("Llamar a mamá")
t5 = tarea("Leer un libro")
print(t1)
t1.marcar_como_completada() 
print(t2)
print(t3)
t3.marcar_como_completada()
print(t4)
print(t5)