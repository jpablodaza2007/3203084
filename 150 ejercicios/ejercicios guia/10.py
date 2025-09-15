contraseña = "Miclave123"
longitudmin = 8

print("Contraseña a validar",contraseña)
print("Longitud de la contraseña",len(contraseña))
if len(contraseña) >= longitudmin:
    print("Contraseña válida")

if contraseña.islower():
    print("La contraseña debe tener al menos una letra mayúscula")