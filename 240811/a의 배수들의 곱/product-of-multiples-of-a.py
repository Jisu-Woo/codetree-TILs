z = input().split()

a = int(z[0])
b = int(z[1])

prod = 1
for i in range(1, b + 1):
    if i % a == 0:
        prod *= i

print(prod)