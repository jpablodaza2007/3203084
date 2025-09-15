numero = 1
limite = 20
paresencontrados = 0
print("busca numeros pares entre 1 y", limite,":")
while numero <= limite:
    if numero %2 == 0:
        print("numero  es par")
        paresencontrados = paresencontrados +1
    numero += 1

print("\nResumen")
print("Se encontraron",paresencontrados,"numero de pares ")


