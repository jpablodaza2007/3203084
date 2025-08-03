nombre = "Juan"
print(nombre)
print(type(nombre))
#En este caso nombre es la variable y "Juan" un dato de tipo string

#Se quiere aprobar para un trabajo 
print("Ingrese su nombre")
nombre = input()
print("Ingrese su edad")
edad = int(input())
print("Usted sabe comunicarse en grupo?")
rta = input()
print("Es capaz de manejarse en situaciones de estres?")
rta2 = input()

if rta and rta2 == "Si" and edad > 18:
    print("\n ==== Datos del Postulado ====")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print("\n Esta aprobado para el trabajo")
else:
   print("\n ==== Datos del Postulado ====")
   print(f"Nombre: {nombre}")
   print(f"Edad: {edad}")
   print("\n Usted no aprueba para el trabajo")
  