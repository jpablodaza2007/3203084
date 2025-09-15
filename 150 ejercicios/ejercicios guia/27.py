def busqueda_binaria(lista, elemento_buscado):
    """
    Implementa búsqueda binaria para encontrar un elemento
    La lista debe estar ordenada previamente
    """
    izquierda = 0
    derecha = len(lista) - 1
    iteraciones = 0

    print(f"Buscando {elemento_buscado} en: {lista}")
    print("\nProceso de búsqueda:")

    while izquierda <= derecha:
        iteraciones += 1
        medio = (izquierda + derecha) // 2 
        elemento_medio = lista[medio]

        print(f"\nIteración {iteraciones}:")
        print(f" Rango: posiciones {izquierda} a {derecha}")
        print(f" Medio: posición {medio}, valor {elemento_medio}")

        if elemento_medio == elemento_buscado:
            print(f" ¡Encontrado! {elemento_buscado} está en posición {medio}")
            print(f"Total de iteraciones: {iteraciones}")
            return medio
        elif elemento_medio < elemento_buscado:
            print(f" {elemento_medio} < {elemento_buscado}, buscar en mitad derecha")
            izquierda = medio + 1
        else:
            print(f" {elemento_medio} > {elemento_buscado}, buscar en mitad izquierda")
            derecha = medio - 1

    print(f"\n {elemento_buscado} no está en la lista")
    print(f"Total de iteraciones: {iteraciones}")
    return -1


def busqueda_lineal(lista, elemento_buscado):
    """Búsqueda lineal para comparar eficiencia"""
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == elemento_buscado:
            return i, comparaciones
    return -1, comparaciones


# Ejemplo de uso
numeros_ordenados = [11, 22, 25, 34, 44, 55, 66, 77, 88, 99]
buscar = 55

print("🔍 COMPARACIÓN DE ALGORITMOS DE BÚSQUEDA")
print("=" * 45)
print("Lista ordenada:", numeros_ordenados)
print(f"Elemento a buscar: {buscar}")

print("\n1. BÚSQUEDA BINARIA:")
print("-" * 25)
posicion_binaria = busqueda_binaria(numeros_ordenados, buscar)

print("\n2. BÚSQUEDA LINEAL:")
print("-" * 25)
posicion_lineal, comparaciones_lineales = busqueda_lineal(numeros_ordenados, buscar)
print(f"Búsqueda lineal: {comparaciones_lineales} comparaciones")
if posicion_lineal != -1:
    print(f"Elemento encontrado en posición {posicion_lineal}")

print(f"\n Ventaja de búsqueda binaria: Menos comparaciones en listas grandes")
