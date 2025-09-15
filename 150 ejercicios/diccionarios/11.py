palabra = "banana"
dic = {}
for letra in palabra:
    if letra in dic:
        dic[letra] += 1
    else:
        dic[letra] = 1
print(dic)