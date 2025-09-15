t = ("ana", "oso", "luz", "ala")
count = 0
for s in t:
    if s[0] == s[-1]:
        count += 1
print(count)