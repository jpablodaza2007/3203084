tablero = {
    (0, 0): "ocupado",
    (0, 1): "libre",
    (1, 0): "ocupado",
    (1, 1): "libre"
}

for coord, estado in tablero.items():
    if estado == "ocupado":
        print("Punto", coord, "está ocupado")
