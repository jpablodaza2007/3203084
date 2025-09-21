class ProcesadorDeListas:
    def __init__(self, nombre):
        self.nombre = nombre

    def contar_elementos_pares(self, lista_numeros):
        pares = [num for num in lista_numeros if num % 2 == 0] 
        print(f"En '{self.nombre}', la lista {lista_numeros} tiene {len(pares)} números pares.")

procesador = ProcesadorDeListas("Mi Procesador")
numeros_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8]
procesador.contar_elementos_pares(numeros_ejemplo)