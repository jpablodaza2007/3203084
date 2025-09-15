dic = {'a': 0, 'b': 5, 'c': 0}
claves_a_eliminar = []
for k, v in dic.items():
    if v == 0:
        claves_a_eliminar.append(k)
for k in claves_a_eliminar:
    del dic[k]
print(dic)