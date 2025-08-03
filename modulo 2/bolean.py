#Una variable de tipo booleano es aquella que guarda condiciones de verdad como falso o verdadero los cuales son un valor bool(booleano)

hay_frutas = False
print(hay_frutas)
print(type(hay_frutas))
#En este caso hay_frutas es la variable y False un dato de tipo bool

#Se pregunta si la persona tiene mascotas
print("Usted tiene mascotas?")
rta = input()
if rta == "Si":
    pet = True
    print("Vaya, que bueno")
    if pet == True:
       print("Que tipo de mascota es?")
       rta2 = input()
       print(f"Que bueno que tengas de mascota a un {rta2}")
elif rta == "No":
     pet = False
     print("Pues, esta bien no tener mascota") 
