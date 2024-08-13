z = input().split()

n = int(z[0])
m = int(z[1])

for _ in range(n):
    for _ in range(m):
        print('*', end=" ")
    print()