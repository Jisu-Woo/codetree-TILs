n = int(input())

z = [0] * n
for i in range(0, n):
    z[i] = int(input())


for i in range(n):
    if z[i] % 2 == 1 and z[i] % 3 == 0:
        print(z[i])