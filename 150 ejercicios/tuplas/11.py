t = (12, 34, 56, 78)
def suma_digitos(n):
    s = 0
    while n > 0:
        s += n %10
        n //=10
    return s

count = 0
for n in t:
    if suma_digitos(n) % 2 == 0:
        count += 1
print("Cantidad con suma de dígitos par:", count)