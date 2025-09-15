t = tuple(range(1, 16))
mult4 = ()
for n in t:
    if n % 4 == 0:
        mult4 += (n,)
print(mult4)