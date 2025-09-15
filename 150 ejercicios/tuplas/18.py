t = ("luna", "sol", "estrella")
longitudes = []
for p in t:
    count = 0
    for _ in p:
        count += 1
    longitudes.append(count)
print(longitudes)