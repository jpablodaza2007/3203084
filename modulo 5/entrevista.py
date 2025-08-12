import random


preguntas = [
    "¿Cuál es tu nombre?",
    "¿Qué edad tienes?",
    "¿Cuál es tu comida favorita?",
    "¿Qué te gusta hacer en tu tiempo libre?"
]

respuestas_generales = [
    "Interesante.",
    "Eso suena interesante.",
]

datos_usuario = []

print("Entrevistador: Hola, vamos a hacerte unas preguntas. Responde lo que quieras.")
print("Escribe 'salir' en cualquier momento para terminar la entrevista.\n")

for pregunta in preguntas:
    respuesta = input(f"Entrevistador: {pregunta}\nTú: ").strip().lower()

    if respuesta == "salir":
        print("Entrevistador: Entiendo, gracias por tu tiempo. ¡Hasta pronto!")
        break

    datos_usuario.append(respuesta)


    print("Entrevistador:", random.choice(respuestas_generales), "\n")


if len(datos_usuario) == len(preguntas):
    print("Entrevistador: Gracias por responder todas las preguntas.")
    print("Esto fue lo que me contaste:")
    for i in range(len(preguntas)):
        print(f"- {preguntas[i]} {datos_usuario[i].capitalize()}")
