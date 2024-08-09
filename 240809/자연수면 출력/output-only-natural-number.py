z = input().split()

a = int(z[0])
b = int(z[1])

if a > 0:
    for _ in range(b):
        print(a, end="")
else:
    print(0)