secreta = "abc123"
while True:
    p = input("Contraseña: ")
    if p == secreta:
        print("Correcto")
        break
    else:
        print("Intenta de nuevo")