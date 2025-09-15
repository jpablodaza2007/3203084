dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
sin_fin = []
for dia in dias:
    if dia != "sábado" and dia != "domingo":
        sin_fin.append(dia)
print(sin_fin)