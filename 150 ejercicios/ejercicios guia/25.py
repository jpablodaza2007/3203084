estudiantes = [] 

def agregar_estudiante(nombre, edad, grado):
    """Agrega un nuevo estudiante al sistema"""
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "grado": grado,
        "calificaciones": []
    }
    estudiantes.append(estudiante)
    print(f"✅ Estudiante {nombre} agregado exitosamente")

def buscar_estudiante(nombre):
    """Busca un estudiante por nombre"""
    for i, estudiante in enumerate(estudiantes):
        if estudiante["nombre"].lower() == nombre.lower():
            return i 
    return -1 

def agregar_calificacion(nombre, materia, nota):
    """Agrega una calificación a un estudiante"""
    posicion = buscar_estudiante(nombre)
    if posicion != -1:
        calificacion = {"materia": materia, "nota": nota}
        estudiantes[posicion]["calificaciones"].append(calificacion)
        print(f" Calificación agregada a {nombre}: {materia} = {nota}")
    else:
        print(f" Estudiante {nombre} no encontrado")
    
def calcular_promedio(nombre):
    """Calcula el promedio de un estudiante"""
    posicion = buscar_estudiante(nombre)
    if posicion != -1:
        calificaciones = estudiantes[posicion]["calificaciones"]
        if calificaciones:
            suma = sum(cal["nota"] for cal in calificaciones)
            promedio = suma / len(calificaciones)
            return round(promedio, 2)
        else:
            return 0
    return None

def mostrar_reporte():
    """Muestra un reporte completo de todos los estudiantes"""
    print("\n" + "="*50)
    print(" REPORTE DE ESTUDIANTES")
    print("="*50)
    for estudiante in estudiantes:
        print(f"\nNombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']} años")
        print(f"Grado: {estudiante['grado']}")
        
        if estudiante["calificaciones"]:
            print("Calificaciones:")
            for cal in estudiante["calificaciones"]:
                print(f" - {cal['materia']}: {cal['nota']}")
            promedio = calcular_promedio(estudiante['nombre'])
            print(f"Promedio general: {promedio}")
        else:
            print("Sin calificaciones registradas")

# Ejemplo de uso
print("-" * 30)
print("🎓 SISTEMA DE REGISTRO DE ESTUDIANTES")

agregar_estudiante("Ana García", 16, "10°")
agregar_estudiante("Carlos López", 15, "9°")
agregar_estudiante("María Rodríguez", 17, "11°")

agregar_calificacion("Ana García", "Matemáticas", 9.2)
agregar_calificacion("Ana García", "Historia", 8.8)
agregar_calificacion("Ana García", "Ciencias", 9.5)
agregar_calificacion("Carlos López", "Matemáticas", 7.5)
agregar_calificacion("Carlos López", "Historia", 8.2)
agregar_calificacion("Pedro Martín", "Matemáticas", 8.0)  # Este no existe

mostrar_reporte()
