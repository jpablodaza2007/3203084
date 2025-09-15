nota = 8.5

if nota >=9.0:
    clasifcacion = "Exelente"
    mensaje = "Felicidades sigue asi"
elif nota >= 7.0: 
    clasificacion = "Buena"
    mensaje = "Buen trabajo, puedes mejorar"
else:
    clasificacion = "Necesita mejorar"
    mensaje = "Estudia más para la próxima"

print("Tu nota es:", nota)
print("Clasificación:", clasificacion)
print("Comentario:", mensaje)