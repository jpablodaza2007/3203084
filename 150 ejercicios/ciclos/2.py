secreto = "mortadela"
while True:
    intento = input("Adivina la palabra secreta: ")
    if intento == secreto:
        print("correcto!")
        break
    else:
        print("intenta otra vez (pista : es una comida que va en sandwich)")