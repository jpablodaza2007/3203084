import csv
import statistics



archivo = input("Ingrese el nombre del archivo CSV (con extensión): ")

try:
    with open(archivo, newline='', encoding="utf-8") as f:
        lector = csv.reader(f)
        encabezados = next(lector) 
        datos = list(lector)

    print("\nArchivo cargado con éxito.\n")

except Exception as e:
    print("Error al leer el archivo:", e)
    exit()


print("=== INFORMACIÓN GENERAL ===")
print(f"Columnas: {encabezados}")
print(f"Cantidad de filas: {len(datos)}")


columnas = {encabezados[i]: [fila[i] for fila in datos if fila[i] != ""] for i in range(len(encabezados))}


print("\nColumnas disponibles:", list(columnas.keys()))
columna = input("Ingrese el nombre de una columna numérica para analizar: ")

if columna in columnas:
    try:
        numeros = [float(x) for x in columnas[columna]]

        print(f"\n=== ESTADÍSTICAS DE '{columna}' ===")
        print(f"Cantidad de datos: {len(numeros)}")
        print(f"Mínimo: {min(numeros)}")
        print(f"Máximo: {max(numeros)}")
        print(f"Media: {statistics.mean(numeros)}")
        print(f"Mediana: {statistics.median(numeros)}")
        print(f"Desviación estándar: {statistics.stdev(numeros) if len(numeros) > 1 else 'N/A'}")


        print("\n=== HISTOGRAMA (Texto) ===")
        bins = 10
        rango = max(numeros) - min(numeros)
        paso = rango / bins if rango > 0 else 1
        for i in range(bins):
            lim_inf = min(numeros) + i * paso
            lim_sup = lim_inf + paso
            cuenta = sum(1 for n in numeros if lim_inf <= n < lim_sup)
            barra = "█" * cuenta
            print(f"{lim_inf:8.2f} - {lim_sup:8.2f}: {barra}")

    except ValueError:
        print("La columna no contiene solo números.")
else:
    print("La columna seleccionada no existe.")
