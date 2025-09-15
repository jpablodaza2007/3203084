lista = ['hola', 'mundo']
dic = {}
for palabra in lista:
    dic[palabra] = 0
    for _ in palabra:
        dic[palabra] += 1
print(dic)