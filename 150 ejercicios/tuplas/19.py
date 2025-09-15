t = ("Hola", "mundo", "Python")
cadena = ""
for i in range(len(t)):
    cadena += t[i]
    if i < len(t)-1:
        cadena += " "
print(cadena)