z = input().split()

a = int(z[0])
b = int(z[1])

prod = 1
for i in range(b):
    prod *= a

print(prod)