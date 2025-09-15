numsecreto = 7
intentomax = 3
intentosact = 1

print("Bienvenido al juego de adivinanza")
print("Tienes", intentomax, "intentos para adivinar el número del 1 al 10")

while intentosact <= intentomax:
    print("\n intento",intentosact,"de",intentomax,"...")
    if intentosact == 1:
        adivinanza = 3
    elif intentosact == 2:
        adivinanza = 8
    else:
        adivinanza = 7

    print("Tu adivinanza", adivinanza)

    if adivinanza == numsecreto:
        print("Ganaste el numero",numsecreto)
        break
    elif adivinanza < numsecreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")

    intentosact += 1

    if intentosact >intentomax:
        print("\nSe acabaron los intentos el numero secreto era",numsecreto)