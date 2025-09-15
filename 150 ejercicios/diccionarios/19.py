palabras = ['casa', 'auto', 'casa', 'bicicleta']
dic = {}
for p in palabras:
    longitud = len(p)
    if longitud in dic:
        dic[longitud] += 1
    else:
        dic[longitud] = 1
print(dic)