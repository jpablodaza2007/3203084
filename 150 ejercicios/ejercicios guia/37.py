libros = {}
usuarios = {}
prestamos = []

print("=== BIBLIOTECA ===")

while True:
    print("\n1. Añadir libro")
    print("2. Añadir usuario") 
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Ver libros")
    print("6. Ver usuarios")
    print("7. Ver préstamos")
    print("0. Salir")
    
    op = input("Opción: ")
    
    if op == '0':
        print("Fin")
        break
    
    elif op == '1':
        id_libro = len(libros) + 1
        titulo = input("Título: ")
        autor = input("Autor: ")
        cantidad = int(input("Cantidad: "))
        libros[id_libro] = {"titulo": titulo, "autor": autor, "total": cantidad, "prestados": 0}
        print(f"Libro añadido con ID {id_libro}")
    
    elif op == '2':
        id_user = input("ID usuario: ")
        nombre = input("Nombre: ")
        usuarios[id_user] = {"nombre": nombre}
        print("Usuario añadido")
    
    elif op == '3':
        id_user = input("ID usuario: ")
        if id_user not in usuarios:
            print("Usuario no existe")
            continue
        id_libro = int(input("ID libro: "))
        if id_libro not in libros:
            print("Libro no existe")
            continue
        libro = libros[id_libro]
        if libro["prestados"] >= libro["total"]:
            print("No disponible")
            continue
        prestamos.append({"usuario": id_user, "libro": id_libro})
        libro["prestados"] += 1
        print("Libro prestado")
    
    elif op == '4':
        id_user = input("ID usuario: ")
        id_libro = int(input("ID libro: "))
        for i, p in enumerate(prestamos):
            if p["usuario"] == id_user and p["libro"] == id_libro:
                prestamos.pop(i)
                libros[id_libro]["prestados"] -= 1
                print("Libro devuelto")
                break
        else:
            print("Préstamo no encontrado")
    
    elif op == '5':
        print("\nLibros:")
        for id_libro, libro in libros.items():
            disponible = libro["total"] - libro["prestados"]
            print(f"{id_libro}. {libro['titulo']} - {libro['autor']} (Disponible: {disponible})")
    
    elif op == '6':
        print("\nUsuarios:")
        for id_user, usuario in usuarios.items():
            print(f"{id_user} - {usuario['nombre']}")
    
    elif op == '7':
        print("\nPréstamos:")
        for p in prestamos:
            usuario = usuarios[p["usuario"]]["nombre"]
            libro = libros[p["libro"]]["titulo"]
            print(f"{usuario} tiene '{libro}'")
    
    else:
        print("Opción inválida")