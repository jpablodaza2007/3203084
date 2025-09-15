preciototal = 120
descuento = 0

if preciototal > 100:
    descuento = preciototal*0.10
    preciofinal= preciototal-descuento
    print("Felicidades tienes un descuento del 10%")
    print("Descuento aplicado del $",descuento)
else:
    preciofinal = preciototal
    print("No hay descuento disponible")

print("Precio original: $", preciototal)
print("Precio final: $", preciofinal)




