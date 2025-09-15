fib = [0, 1]
i = 2
while i < 10:
    fib.append(fib[i-1] + fib[i-2])
    i += 1
suma = 0
for num in fib:
    suma += num
print(fib)
print("Suma:", suma)