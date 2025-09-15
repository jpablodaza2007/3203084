factoriales = []
num = 1
while num <= 7:
    fact = 1
    i = 1
    while i <= num:
        fact *= i
        i += 1
    factoriales.append(fact)
    num += 1
print(factoriales)