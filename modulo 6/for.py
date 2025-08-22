for i in range(5):
    print(i)
    continue
print("esto continua") 

for i in range(3):
    print(i+3)

tabla = int(input("digite la tabla de multiplicar que desea ver"))
for i in range(11):
    print(f"{tabla} x {i} = {tabla*i}")