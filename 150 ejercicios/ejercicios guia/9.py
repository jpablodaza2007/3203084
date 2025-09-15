numsecreto = 7
adivinanza = 5

print("El numero secreto es",numsecreto)
print("Tu adivinanza es",adivinanza)

if adivinanza == numsecreto:
    print("Felicidades adivinaste el numero")
elif adivinanza < numsecreto:
    print("Tu numero es menor.Intenta con uno mas grande")
else:
    print("Tu numero es mayor.Intenta con una mas pequeño")

