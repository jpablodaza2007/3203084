dic = {'a': 12, 'b': 7, 'c': 25, 'd': 3}
count = 0
for v in dic.values():
    if v > 10:
        count += 1
print("Valores mayores que 10:", count)