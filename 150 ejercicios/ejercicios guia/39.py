

def intro():
    print("=== AVENTURA EN EL ANTIGUO EGIPTO ===")
    nombre = input("¿Cuál es tu nombre, viajero del Nilo? ")
    if not nombre.strip():
        nombre = "Errante"
    print(f"\nBienvenido, {nombre}. Estás en Tebas, tierra de faraones y misterios.\n")
    return nombre

def piramide(nombre):
    print("\nLlegas a una gran pirámide, su entrada está medio oculta por la arena.")
    print("¿Qué haces?")
    print("1. Entrar en la pirámide")
    print("2. Rodearla y buscar otra entrada")
    opcion = input("> ")

    if opcion == "1":
        print(f"\n{nombre}, entras y encuentras un sarcófago dorado.")
        final_rico(nombre)
    else:
        print(f"\n{nombre}, una trampa de arena se abre bajo tus pies. No logras escapar.")
        final_tragico(nombre)

def desierto(nombre):
    print("\nCruzas el desierto ardiente. El sol quema sin piedad.")
    print("¿Qué haces?")
    print("1. Seguir caminando sin detenerte")
    print("2. Buscar sombra bajo unas ruinas cercanas")
    opcion = input("> ")

    if opcion == "1":
        print(f"\n{nombre}, el calor te vence y caes en la arena.")
        final_tragico(nombre)
    else:
        print(f"\n{nombre}, bajo las ruinas encuentras un oasis secreto con palmeras y agua fresca.")
        final_feliz(nombre)

def nilo(nombre):
    print("\nLlegas al majestuoso río Nilo. Un pequeño bote está amarrado en la orilla.")
    print("¿Qué haces?")
    print("1. Subirte al bote y navegar")
    print("2. Nadar por tu cuenta")
    opcion = input("> ")

    if opcion == "1":
        print(f"\n{nombre}, el bote te lleva hasta una aldea donde te reciben con ofrendas.")
        final_feliz(nombre)
    else:
        print(f"\n{nombre}, los cocodrilos del Nilo emergen... No logras sobrevivir.")
        final_tragico(nombre)

def final_feliz(nombre):
    print(f"\n🌟 ¡Felicidades, {nombre}! Has encontrado un final feliz en el Antiguo Egipto.\n")

def final_tragico(nombre):
    print(f"\n💀 {nombre}, tu aventura en Egipto termina de forma trágica...\n")

def final_rico(nombre):
    print(f"\n💰 {nombre}, te conviertes en el viajero más rico del Antiguo Egipto.\n")

def main():
    nombre = intro()

    print("El camino se divide en tres:")
    print("1. Ir a la pirámide")
    print("2. Cruzar el desierto")
    print("3. Ir hacia el río Nilo")

    opcion = input("> ")

    if opcion == "1":
        piramide(nombre)
    elif opcion == "2":
        desierto(nombre)
    elif opcion == "3":
        nilo(nombre)
    else:
        print("\nNo elegiste un camino válido. Tu aventura termina antes de empezar...")

if __name__ == "__main__":
    main()
