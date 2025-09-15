num = int(input("Ingresa un número: "))
es_primo = True
for i in range(2, num):
    if num % i == 0:
        es_primo = False
        break
print("Es primo" if es_primo and num > 1 else "No es primo")
